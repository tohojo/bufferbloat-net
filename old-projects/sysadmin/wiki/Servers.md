
---
title: Servers
date: 2011-03-19T09:00:52
lastmod: 2011-04-25T14:25:33
type: wiki
---
Server Information
==================

Most of the servers currently in operation are hosted by isc.org in
their redwood city facility. ISC has a mechanism for <link>coping with
crashes</link> using RT that you can use for outright server failure,
however they are not capable of doing more than power cycling a machine.

<link>IP address assignment</link>

Physical Servers
----------------

### siwa.bufferbloat.net

Intended as a backup DNS and email server, this machine has been
somewhat flaky (two crashes in 2 months) and we plan to retire it.\
Its primary purpose at present is to manage the <link>mailing
lists</link>.

### shipka.bufferbloat.net

This is currently the principal <link>web and database server</link> for
our <link>projects</link>.

### toutatis.teklibre.com

Functions as a mirror for mirrors.bufferbloat.net, and serves as a
network monitoring console (rt and nagios) for various services.

It is also running the debris from teklibre itself and Dave Täht's own
websites.

### backup.bufferbloat.net

An atom box located at Jim Gettys house and available only via
<link>ipv6</link>.

### huchra.bufferbloat.net

The first in a series (we hope) of significantly more capable servers.
It is an 8 core 2U machine, with mirrored drives. The primary intent of
this server is to do builds of various OSes, but it needs to become
stable first, which thus far, it hasn't.

### git.infradead.org

The debloat-testing kernel tree is hosted at git.infradead.org due to
the kind contribution of David Woodhouse

I think it's in MIT's facilities.

### Virtual Servers

Some services are being hosted at github.com

Server History
--------------

### In the beginning...

Dave Täht had the first two servers sitting in a box at ISC for nearly a
year, relics of the <link>bloat:wisp6</link> project. When he was
convinced of the severity of the problem (Jan 10), he pulled some
strings, and got them up and running with the core services we needed to
get off the ground by Feb 1. In that haste some fundamental
help-me-sleep-better-at-night things like <link>disaster planning</link>
were skipped.

They are very weak machines- pentium IIIs - which among other things
have poor support for virtualization.

We hope to start working more with virtualization with the advent of
huchra, and the other things that need to be addressed can be seen on
ticket \#35.

The servers are all configured by the <link>bloat:Dogfood
Principle</link> - and amazingly, we've survived multiple slashdottings
without a hitch.

### OSes

All servers are running ubuntu 10.10. Why? It was what jg and dave taht
had on our laptops. Whether this was a good choice or not remains to be
seen. Certainly redhat would be more stable.

### Naming scheme

All machines are named after asteroids. Given the quantity of asteroids
available, we don't expect to run out of names any time soon.

(We hope to get an asteroid named after [John
Huchra](http://en.wikipedia.org/wiki/John_Huchra) , if there isn't one
already)

### Security

All bufferbloat machines have <link>ssh</link> on port 222, rather than
port 22. This cuts the script kiddie issues by 99.999% and is easily
managed by those on the sysadmin team by adding a:

    Host *.bufferbloat.net
         Port 222

to your \~/.ssh/ssh\_config file

What firewalling exists is weak to non-existent, but there are very few
routes into each machine, so it's easier to sleep at night. That can be
improved, obviously.

Aside from that password files are currently shared manually, and the
passwords are distributed to only three people at present, according to
the two man rule. We've tried to make it possible to divide work by
having passwords on nearly every major subsystem distinct from the
others.

/etc is managed via etckeeper (\#3)

### IPv6 support

<link>IPv6</link> support is integral to the entire system. All systems
are managed via IPv6. Some (internal) web sites can only be managed via
IPv6.

### DNS

Principal <link>DNS</link> is currently provided by name.com, which
"features" a bug in their NXDOMAIN lookup for ipv6 that results in
invalid DNS lookups. (\#25) To work around this, all servers actually
are using teklibre.com as their domain in the resolver. In the future,
we will re-take control of DNS and use ISC.org as secondary name
service.

Future infrastructure choices
-----------------------------

... opening this up to debate ...

### Upcoming machines

huchra.bufferbloat.net is the primary machine we hope to get online in
April.

### Virtual Servers

We hope to establish mirrors for openwrt based builds in various
locations in the world, off of the virt.bufferbloat.net subdomain.

Moving towards a more virtual server architecture has many benefits but
additional management and security overhead. One key thing to address
early is to make sure we can get accurate time across whatever virtual
solutions we chose.

### Test servers

### VOIP server

Due to the large number of people involved all over the world, and the
difficulty in co-ordinating across 24 time zones, we hope to establish a
good IPv6 server on the East coast somewhere that can also do voip
conference calls and act as a central PBX for more folk.
