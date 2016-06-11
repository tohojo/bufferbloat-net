## -*- coding: utf-8 -*-
##
## fix_links.py
##
## Author:   Toke Høiland-Jørgensen (toke@toke.dk)
## Date:      9 June 2016
## Copyright (c) 2016, Toke Høiland-Jørgensen
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function, unicode_literals

import sys, json, re, os, pathlib

titlemap = json.load(open("titlemap.json"))

for f in sys.argv[1:]:
    c = open(f).read()
    path = pathlib.PurePath(f)
    myproject = path.parts[-3]
    newtext = c
    pos = 0
    while True:
        start = c.find("<link>", pos)
        if start < 0:
            break
        end = c.find("</link>", start)
        if end < 0:
            break
        pos = end+7

        label = None
        project = myproject
        link = linktext = c[start+6:end].replace("\n", " ")
        if link.startswith("http"):
            print("Found verbatim link: %s" % linktext)
            newtext = newtext.replace(c[start:end+7], "[%s](%s)" % (linktext,linktext))
            continue
        linktext = link
        if ":" in linktext:
            project,linktext = linktext.split(":")
        if "|" in linktext:
            linktext,label = linktext.split("|")
        if "\#" in linktext:
            linktext = linktext.split("\#")[0]
        linktext = linktext.replace("\_", " ")
        while "  " in linktext:
            linktext = linktext.replace("  ", " ")
        linktext = linktext.strip()
        if linktext == "Wiki":
            linktext = "index"
        if not linktext:
            continue
        found = False
        if not project in titlemap:
            print("Warning: Found link to non-existant project: %s" % project)
            continue
        for n,t in titlemap[project].items():
            if t['title'].lower() == linktext.lower() or n.lower() == linktext.lower():
                newtext = newtext.replace(c[start:end+7], '[%s]({{< relref "%s/wiki/%s.md" >}})' % (label or linktext, t['project'], n))
                found = True
                break
        if not found:
            print("Warning: Couldn't find target for %s" % link)
    with open(f, 'w') as fp:
        fp.write(newtext)
