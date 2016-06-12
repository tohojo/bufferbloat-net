## -*- coding: utf-8 -*-
##
## convert_issues.py
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

issues = csv.DictReader(open("issuesdump.csv"))
interesting_projects = ["bloat", "cerowrt", "make-wifi-fast", "codel"]
outpath = pathlib.Path("../content")
oldpath = pathlib.Path("../old-projects")
header = """
---
title: "Bug #{id}: {title}"
subject: "{title}"
date: {date}
updated: {updated}
type: issue
author: {author}
id: {id}
issue_status: {status}
priority: {priority}
assignee: {assignee}
aliases:
    - /issues/{id}
---

{{{{< issue_description >}}}}
{text}
{{{{< /issue_description >}}}}

## History
"""

def convert_textile(text):
    res = subprocess.run(['pandoc', '-f', 'textile', '-t', 'markdown'], input=text, stdout=subprocess.PIPE,
                         universal_newlines=True, check=True)
    return res.stdout

for i in issues:
    project = i['project']
    title = i['subject']
    name = i['id']
    text = convert_textile(i['description'].replace("[[", "<link>").replace("]]","</link>"))
    date = i['created_on'].split(".")[0].replace(" ","T")
    updated = i['updated_on'].split(".")[0].replace(" ","T")

    text = header.format(title=title.replace('"', '\\"'), date=date, updated=updated, author=i['author'],
                         id=i['id'], status=i['status'], priority=i['priority'], assignee=i['assignee'],
                         text=text)

    if not project in interesting_projects:
        outdir = oldpath / project / 'issues'
    else:
        outdir = outpath / project / 'issues'

    if not outdir.is_dir():
        outdir.mkdir(parents=True)
    outfile = outdir / "{}.md".format(name)

    with outfile.open("w") as fp:
        fp.write(text)
