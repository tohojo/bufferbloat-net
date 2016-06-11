
---
title: Web and database server
date: 2011-03-19T09:18:39
lastmod: 2011-03-19T11:12:33
type: wiki
---
Web and database server information
===================================

The web servers are all apache-event based rather than apache-prefork,
using fcgi, according to the <link>bloat:Dogfood Principle</link>.

This has worked astoundingly well thus far, ramping up and down to
handle workloads with very little extra memory use, and no failures to
date. While passenger has been recommended, fastcgi offers the potential
of more and different kinds of non-ruby services, so I'm inclined to
stick with that.

Also, given the dependence on fastcgi, it may be possible to switch to
lighttpd for some services at a later date.

Database server(s)
------------------

Postgres 8.4. It would be good to move to postgres 9.X (\#4) due to the
support for streaming replication, however, due to the enormous number
of supporting libraries that need to be made to work, this has proven
difficult.

Originally many services used mysql. While mysql is more popular in many
ways, postgres is more capable, and we would prefer to standardize on
one database type for all backends, if possible.

Continuous Build System
-----------------------

The openwrt project uses buildbot. Jenkins is supposedly superior, but
is undergoing a project fork. After <link>huchra</link> goes up, it
would be good to start figuring \#36 and \#32 out.

System Management Services
--------------------------

These have not been deployed yet as of the original <link>Servers</link>
(<link>siwa</link>) has proven the flakiest of the bunch.

-   Web server statistics - \#5

Collating the data across the mirrors is proving difficult.

-   Bandwidth/Usage statistics

Cacti, probably, or mrtg. \#6 Suggestions wanted

-   Uptime/Failure notification

Nagios probably. \#6

-   Remote Routers

Statistics collection
---------------------

-   Cosmic Background NTP

<!-- -->

-   bismark

