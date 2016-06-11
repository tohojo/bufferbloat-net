## -*- coding: utf-8 -*-
##
## convert.py
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

import csv, re, subprocess, os, json, sys, pathlib

content_map = {}
pages = csv.DictReader(open("wikidump.csv"))

interesting_wikis = ["bloat", "cerowrt", "make-wifi-fast", "codel"]

outpath = pathlib.Path("../content/projects")
tmpdir = pathlib.Path("textile")

if not tmpdir.is_dir():
    tmpdir.mkdir()

header = """
---
title: {title}
date: {date}
lastmod: {updated}
type: wiki
---
"""

titlemap = {}

outlist = []

for p in pages:
    project = p['project']
    if not project in interesting_wikis:
        continue
    title = p['title'].replace("_", " ")
    name = p['title']
    titlemap[name] = {'title':title,'project':project}
    text = p['text'].replace("[[", "<link>").replace("]]","</link>").replace("{{>toc}}", "")
    outfile = "textile/{}:{}.textile".format(project,name)
    mdfile = "textile/{}:{}.md".format(p['project'],name)

    date = p['created_on'].split(".")[0].replace(" ","T")
    updated = p['updated_on'].split(".")[0].replace(" ","T")

    with open(outfile, "w") as fp:
        fp.write(text)
    subprocess.run(['pandoc', outfile, '-o', mdfile])
    mdtext = open(mdfile).read()
    mdtext = header.format(title=title, date=date, updated=updated) + mdtext


    outdir = outpath / project / 'wiki'
    if not outdir.is_dir():
        outdir.mkdir(parents=True)
    finalmd = outdir / "{}.md".format(name)
    with finalmd.open("w") as fp:
        fp.write(mdtext)
    outlist.append(finalmd)

json.dump(titlemap, open("titlemap.json", "w"))

subprocess.run(['python', 'fix_links.py'] + list(map(str,outlist)), stdout=sys.stdout)
