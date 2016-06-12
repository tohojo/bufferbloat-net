## -*- coding: utf-8 -*-
##
## convert_news.py
##
## Author:   Toke Høiland-Jørgensen (toke@toke.dk)
## Date:     12 June 2016
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
news = csv.DictReader(open("newsdump.csv"))

interesting_projects = ["bloat", "cerowrt", "make-wifi-fast", "codel"]

outpath = pathlib.Path("../content")
oldpath = pathlib.Path("../old-projects")
tmpdir = pathlib.Path("textile/news")

if not tmpdir.is_dir():
    tmpdir.mkdir(parents=True)

header = """
---
title: "{title}"
date: {date}
type: news
author: {author}
aliases:
    - /news/{id}
---
"""

titlemap = {}
for w in interesting_projects:
    titlemap[w] = {}

outlist = []

for n in news:
    project = n['project']
    title = n['title']
    name = re.sub("[^a-z0-9-]", "-", title, 0, re.I)
    while "--" in name:
        name = name.replace("--","-")
    if name.endswith("-"):
        name = name[:-1]
    text = n['description'].replace("[[", "<link>").replace("]]","</link>").replace("{{>toc}}", "")
    outfile = tmpdir / "{}:{}.textile".format(project,name)
    mdfile = tmpdir / "{}:{}.md".format(project,name)

    date = n['created_on'].split(".")[0].replace(" ","T")
    pathdate = n['created_on'].split(" ")[0]

    with outfile.open("w") as fp:
        fp.write(text)
    subprocess.run(['pandoc', str(outfile), '-o', str(mdfile)])
    mdtext = mdfile.open("r").read()
    mdtext = header.format(title=title, date=date, author=n['author'], id=n['id']) + mdtext

    if not project in interesting_projects:
        outdir = oldpath / project / 'news'
    else:
        outdir = outpath / project / 'news'

    if not outdir.is_dir():
        outdir.mkdir(parents=True)
    finalmd = outdir / "{}-{}.md".format(pathdate, name)
    with finalmd.open("w") as fp:
        fp.write(mdtext)
