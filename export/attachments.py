## -*- coding: utf-8 -*-
##
## attachments.py
##
## Author:   Toke Høiland-Jørgensen (toke@toke.dk)
## Date:     11 June 2016
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

import sys, json, re, os, pathlib, csv
from itertools import chain

titlemap = json.load(open("titlemap.json"))
attachments = csv.DictReader(open("wiki-attachments.csv"))
sourcedir = pathlib.Path("files/")
outdir = pathlib.Path("../static/attachments/")
contentdir = pathlib.Path("../content/")

header = """
### Attachments
"""

item_template = '{{{{< attachment name="{name}" type="{mimetype}" description="{description}" filename="{filename}" >}}}}\n'

for a in attachments:
    found = False
    for proj in chain(titlemap.values()):
        for n,p in proj.items():
            if p['id'] == a['wiki_page_id']:
                found = True
                break
        if found:
            break
    if not found:
        print("Couldn't find page for attachment %s with id %s" % (a['filename'], a['id']))
        continue

    sourcefile = sourcedir / a['disk_filename']
    if not sourcefile.exists():
        print("Source file %s doesn't exist." % sourcefile)
        continue

    outfile = outdir / a['disk_filename']
    with sourcefile.open("rb") as fps:
        with outfile.open("wb") as fpd:
            fpd.write(fps.read())

    page = contentdir / p['project'] / 'wiki' / ("%s.md" % n)
    if not page.exists():
        print("Page doesn't exist: %s" % page)
        continue

    with page.open("r") as fp:
        content = fp.read()

    if not header in content:
        content = content + header
    content = content + item_template.format(name=a['filename'], mimetype=a['content_type'], filename=a['disk_filename'], description=a['description'].replace('"', '\\"'))

    with page.open("w") as fp:
        fp.write(content)

    print("Processed %s (page %s)" % (a['filename'],p['title']))
