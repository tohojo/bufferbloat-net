---
title: Using Bonjour mDNS or ZeroConf with CeroWrt
date: 2012-09-10T19:23:47
lastmod: 2013-03-16T12:05:08
type: wiki
---
Using Bonjour, mDNS, or ZeroConf with CeroWrt
=============================================

CeroWrt ships with the Avahi daemon enabled to act as a mDNS reflector.
mDNS is an extension to the DNS concept that allows resources such as
printers, file servers, web servers, iTunes, etc. to advertise a name
along with a description, and of course, the machine's IP address. You
can browse your local network to see what resources are available, then
configure your computer to use that resource. For example, CeroWrt
advertises its SSH and Web services using mDNS/Bonjour.

CeroWrt's default configuration does not to reflect mDNS requests out
the ge00 (WAN) port. This is the proper configuration when CeroWrt is
the primary router in a household. However, if you're using CeroWrt as a
secondary router, it is convenient to enable the mDNS reflector so you
can access resources on your "regular" network.

The configuration is saved in the `/etc/avahi/avahi-daemon.conf` file.
To allow the avahi-daemon to send queries into the ge00 network, ssh
into the router, open `/etc/avahi/avahi-daemon.conf` in an editor, then
find the `deny-interfaces=ge00` line and comment it out by placing a
"\#" at the front, like this:

`#deny-interfaces=ge00`

Then restart the avahi-daemon with this command:

`/etc/init.d/avahi-daemon restart`

mDNS resources on the ge00 port should now be visible and usable.

**NB:** These steps are included in the script at [Automated
Configuration of
CeroWrt](http://www.bufferbloat.net/projects/cerowrt/wiki/Automated_Configuration_of_CeroWrt)

Resources
---------

-   Avahi project website: http://avahi.org
-   Avahi on Wikipedia:
    http://en.wikipedia.org/wiki/Avahi\_%28software%29
-   Bonjour Browser: A Macintosh tool for browsing the Bonjour/mDNS
    services on the local network http://www.tildesoft.com/
-   Bonjour Print Services for Windows: A Windows program that makes it
    easy to find printers on the local network.
    http://support.apple.com/kb/DL999

