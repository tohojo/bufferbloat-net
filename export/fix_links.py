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

import sys, json, re, os

titlemap = json.load(open("titlemap.json"))

for f in sys.argv[1:]:
    c = open(f).read()
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
        linktext = c[start+6:end].replace("\n", " ")
        if ":" in linktext:
            linktext = linktext.split(":")[1]
        if "|" in linktext:
            linktext,label = linktext.split("|")
        if "\#" in linktext:
            linktext = linktext.split("\#")[0]
        linktext = linktext.replace("\_", " ")
        while "  " in linktext:
            linktext = linktext.replace("  ", " ")
        linktext = linktext.strip()
        if not linktext:
            continue
        found = False
        for n,t in titlemap.items():
            if t['title'].lower() == linktext.lower():
                newtext = newtext.replace(c[start:end+7], '[%s]({{< relref "wiki/%s/%s.md" >}})' % (label or linktext, t['project'], n))
                found = True
                break
        if not found:
            print("Warning: Couldn't find target for %s" % linktext)
    with open(f, 'w') as fp:
        fp.write(newtext)
