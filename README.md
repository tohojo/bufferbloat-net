# Bufferbloat.net web site source

This repo contains the source files for the bufferbloat.net web site
(https://www.bufferbloat.net). The site is built using the Hugo static
site generator (https://gohugo.io) and most of the content is
automatically converted from the old bufferbloat.net redmine
installation.

Contributions to improve the content are very welcome. See below for
some pointers on how the content is organised and how to contribute.

## Organisation of this repository

The content shown on the site is all in the `content` directory. Each
subdirectory is a project, which in turn has subdirectories
corresponding to the different types of content. Currently, these are
`wiki` for Wiki pages, `news` for news items and `issues` for the
exported bug reports from the old site. The latter is mainly kept for
archival purposes, and is probably not worth editing.

The scripts used to convert the content from the old site live in the
`export` directory, which also contains the csv files with the data.
Hopefully, there shouldn't be a need to run these anymore. The
`old-projects` directory contains exported data for projects that it was
not deemed relevant to move over to the new site. This data is here for
archival purposes and is not used when generating the site.

Finally, the `static` directory contains resources such as images and
CSS files used for the site layout, and the `layouts` directory contains
the templates Hugo uses to build the site. For more information on how
the latter works, consult the documentation at https://gohugo.io.

## Contributing to the Site

To contribute to the site, simply clone the repository, make your
changes to the markdown file corresponding to the page you wish to edit,
commit the results and open a pull request against this repository.
It is also possible to file issues to point out errors or omissions, or
give suggestions for the content.

The site is build using the [Hugo static site generator.](https://gohugo.io/) Version 0.16 or higher is required to build the site.

### Live Editing

When making changes, you can see a local version of the site by
installing Hugo and running `hugo serve` in this directory. That will
run a web server on localhost, which you can navigate to and see a live
version of the site.

### Creating a new News Item

You can use the hugo binary to create a new news item with appropriate
front matter (the stuff in the top that tells Hugo that this is a news
item). First, decide which project the news item should belong to, then
issue a command like

  `hugo new -k news bloat/news/2016-06-12-my-news-heading.md`

to create the new file (the `-k news` tells Hugo to create a news item).

The new item will be marked as a draft and appear in the
`content/bloat/news` directory. You can then edit the file (don't forget
to the title and add your name as author). While you are editing, you
can run `hugo -D serve` to see the changes in real-time (the `-D` means
'show drafts'). When you are done you can either manually change the
draft status at the top of the file, or you can use the `hugo undraft`
command to do it for you. Then add the file to git and submit a pull
request to have your news item included on the site.
