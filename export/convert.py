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

import csv, re, subprocess, os, json

content_map = {}
pages = csv.DictReader(open("wiki_pages.csv"))
content = csv.DictReader(open("wiki_contents.csv"))

interesting_wikis = ["3","4","5","13","16"]

outdir = "../content/wiki"

header = """
---
title: {title}
date: {date}
lastmod: {updated}
---
"""

titlemap = {}

for c in content:
    content_map[c['page_id']] = c

for p in pages:
    if not p['wiki_id'] in interesting_wikis:
        continue
    title = re.sub("[^a-z0-9-]", "_", p['title'].replace(" ","-"), 0, re.I)
    titlemap[title] = p['title']
    c = content_map[p['id']]
    text = c['text'].replace("[[", "<link>").replace("]]","</link>")
    outfile = "textile/{}.textile".format(title)
    mdfile = "textile/{}.md".format(title)

    date = p['created_on'].split(".")[0].replace(" ","T")
    updated = c['updated_on'].split(".")[0].replace(" ","T")

    with open(outfile, "w") as fp:
        fp.write(text)
    subprocess.run(['pandoc', outfile, '-o', mdfile])
    mdtext = open(mdfile).read()
    mdtext = header.format(title=p['title'], date=date, updated=updated) + mdtext

    with open(os.path.join(outdir, "{}.md".format(title)), "w") as fp:
        fp.write(mdtext)

json.dump(titlemap, open("titlemap.json", "w"))
