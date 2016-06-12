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
attachments = list(csv.DictReader(open("issue-attachments.csv")))
journals = list(csv.DictReader(open("issue-journals.csv")))
interesting_projects = ["bloat", "cerowrt", "make-wifi-fast", "codel"]
outpath = pathlib.Path("../content")
oldpath = pathlib.Path("../old-projects")
attachdir = pathlib.Path("../static/attachments/")
sourcedir = pathlib.Path("files/")
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
{attachments}
{{{{< /issue_description >}}}}

## History
{history}
"""
attachment_template = '{{{{< attachment name="{name}" type="{mimetype}" size="{size}" description="{description}" filename="{filename}" date="{date}" author="{author}" >}}}}\n'

journal_template = """{{{{< issue_journal date="{date}" author="{author}" >}}}}
{text}
{{{{< /issue_journal >}}}}
"""

def convert_textile(text):
    res = subprocess.run(['pandoc', '-f', 'textile', '-t', 'markdown'], input=text, stdout=subprocess.PIPE,
                         universal_newlines=True, check=True)
    return res.stdout

def do_attachments(issue_id):
    output = ""
    i = 0
    for a in attachments:
        found = False
        if not a['issue_id'] == issue_id:
            continue

        sourcefile = sourcedir / a['disk_filename']
        if not sourcefile.exists():
            print("Source file %s doesn't exist." % sourcefile)
            continue

        outfile = attachdir / a['disk_filename']
        if not outfile.exists() and False:
            with sourcefile.open("rb") as fps:
                with outfile.open("wb") as fpd:
                    fpd.write(fps.read())

        size = int(a['filesize'])
        if size > 2**20:
            size = "%.1f MiB" % (size/2**20)
        elif size > 2**10:
            size = "%.1f kiB" % (size/2**10)
        else:
            size = "%d bytes" % size

        date = a['created_on'].split(".")[0].replace(" ","T")
        output = output + attachment_template.format(name=a['filename'], mimetype=a['content_type'],
                                                     date=date, author=a['name'], size=size,
                                                     filename=a['disk_filename'], description=a['description'].replace('"', '\\"'))
        i += 1

    if output:
        output = "### Attachments\n" + output
    return output

def do_journals(issue_id):
    output = ""
    i = 0
    for j in journals:
        if not j['issue_id'] == issue_id:
            continue
        i += 1
        date = j['created_on'].split(".")[0].replace(" ","T")
        text = convert_textile(j['notes'].replace("[[", "<link>").replace("]]","</link>"))
        newtext = []
        for l in text.splitlines():
            if l.startswith("&gt;"):
                l = l.replace("&gt;", ">")
            l = re.sub(r"(http[^ ]+)\\", "\\1", l)
            newtext.append(l)
        output = output + journal_template.format(date=date,author=j['author'],
                                                  text="\n".join(newtext))

    print("Found %d journal entries for issue %s" %(i, issue_id))
    return output



for i in issues:
    project = i['project']
    title = i['subject']
    name = i['id']
    text = convert_textile(i['description'].replace("[[", "<link>").replace("]]","</link>"))
    date = i['created_on'].split(".")[0].replace(" ","T")
    updated = i['updated_on'].split(".")[0].replace(" ","T")
    attach = ""

    if project in interesting_projects:
        attach = do_attachments(i['id'])

    text = header.format(title=title.replace('"', '\\"'), date=date, updated=updated, author=i['author'],
                         id=i['id'], status=i['status'], priority=i['priority'], assignee=i['assignee'],
                         text=text, attachments=attach, history=do_journals(i['id']))

    if not project in interesting_projects:
        outdir = oldpath / project / 'issues'
    else:
        outdir = outpath / project / 'issues'

    if not outdir.is_dir():
        outdir.mkdir(parents=True)
    outfile = outdir / "{}.md".format(name)

    with outfile.open("w") as fp:
        fp.write(text)
