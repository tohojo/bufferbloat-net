
---
title: Custom homepage
date: 2011-09-05T11:24:57
lastmod: 2011-09-05T11:34:31
---
Custom homepage
===============

Cerowrt has a fast, but basic web server, installed. There is, for
example, no php support, so only static web pages are supported at
present.\
(python, fastcgi, etc are available as options)

You can customize your landing page by uploading a new index.html into
/etc/www.

If you intend to have lots of data stored on the router, however, it is
best to change /etc/lighttpd/cerowrt.conf to point it's home dir onto a
usb stick or hard disk,\
and upload your pages there.
