
---
title: "Heartbleed and CeroWrt - upgrade please!"
date: 2014-04-16T11:05:11
type: news
author: Dave Täht
---
Heartbleed Update

In response to the heartbleed (CVE-2014-0160) vulnerability, on April\
9th 2014 we updated the under-development CeroWrt release to include\
the fixed version of openssl. The fix is in CeroWrt 3.10.36-3 and\
later.

We have no means of fixing the "stable" (3.7.5) release of CeroWrt,\
nor any of the innumerable development releases since then.

Please do a clean, fresh upgrade to CeroWrt 3.10.36-6 or later. \[1\]\
Images are available in:
http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/\
Reflashing instructions are here:

https://www.bufferbloat.net/projects/cerowrt/wiki/Cerowrt\_flashing\_instructions

In the base image, the administration gui of recent CeroWrt versions\
depended on openssl (however it is protected by firewall rules to only\
be accessible from within your own network), and several optional
packages\
did also - stunnel - used for "secure" tunneling, and openvpn in
particular.

To find out more about the bug go to http://heartbleed.com/ and/or\
see the relevant page on wikipedia:
http://en.wikipedia.org/wiki/Heartbleed

Heartbleed is one of the most serious bugs that has ever hit the\
internet, and in addition to web services, critical network daemons\
such as those that manage network printing, logging, monitoring, voip,\
chat, tunnels, vpns and email, all can potentially be exploited.

We strongly advise resyncing your source trees with us and distributing\
new firmware images containing the updated libraries. All\
network facing TLS-using daemons are potentially a risk, as are\
any TLS using services exposed behind the firewall.

Once your system is secured again, you should re-issue certs and
passwords,\
as per:
https://www.eff.org/deeplinks/2014/04/bleeding-hearts-club-heartbleed-recovery-system-administrators\
and check for unverified commits.

Packages maintained in the openwrt core repositories that can be\
affected when compiled for openssl\[2\] may include: libevent2,\
ustream-ssl, hostapd, openvpn, authsae, luci-ssl, and uhttpd.

Optional network daemons in other repositories such as radsecproxy,\
vsftpd, squid, mini\_httpd, pure-ftpd, cups, ndyndns, elinks,\
libtorrent, monit, nagios, syslog-ng3, boxbackup, rsyncrypto, curl,\
cyrus-sasl, openldap, icecast, fetchmail, dovecot, transmission,\
stunnel, httptunnel, apache, lighttpd, znc, net-snmp, bitlbee,\
asterisk, postfix and openvpn **all** use TLS level security, are\
often linked against openssl, and are thus potentially vulnerable.

Please see the relevant website for each of the products above\
for news on their vulnerabilities. Much of the furor over heartbleed\
has focused on websites, where notably smtp and imaps and im traffic\
has also been shown vulnerable.

https://zmap.io/heartbleed/

http://blog.freenode.net/2014/04/heartbleed/

Other infrastructure, router and CPE distributions are also affected.

Two examples among many:

http://www.theguardian.com/technology/2014/apr/16/bt-heartbleed-home-hubs

http://www.cnet.com/news/heartbleed-bug-also-affects-cisco-juniper-equipment/

Network facing Applications built on top of php4, php5, python, luasec,
erlang, ruby\
are also potentially affected.

Packages maintained in the ceropackages repository that were
potentially\
vulnerable are xorp, python-lafs, ccnx, and resiprocate.

Please take this seriously and check your firmware and your products
for\
usage of the vulnerable openssl versions.

We note also that multiple other serious vulnerabilities have been\
fixed in other CeroWrt and OpenWrt packages and in the Linux kernel
over\
the past years; you should consider fixing those vulnerabilities in\
your downstream products and routers while you are at it.

We have long been supportive of adding new features for openwrt to\
make it more easily updated in the field, the work could use more\
eyeballs and developers, and we need to find resources and funding for\
a code audit in the coming months.

Notes:

\[1\] Regrettably in the present development branch (3.10.36-4) we are\
trying to isolate a wifi bug that crops up after much traffic, we will\
announce a fix for that when it arrives. See Bug \#442 .

\[2\] The base as-provided-by OpenWrt base binary installations are not\
vulnerable to HeartBleed, as neither the builtin SSH server nor the\
optional LuCI SSL support rely on OpenSSL for cryptographic TLS\
support. Their Attitude Adjustment release used cyassl as a base,\
and the underway Barrier Breaker development series uses PolarSSL\
for as many packages as support exists and the GPLv2 license allows.

In other words the OpenSSL library is not installed within the stock\
base images available on their download servers, however they too\
contain many optional packages that do depend on openssl to function,\
and many downstream products may have chosen openssl over those\
products.

Check your trees! And if you are having a bad week, perhaps this\
will help: http://www.taht.net/\~mtaht/uncle\_bills\_helicopter.html

Stay calm and keep on patching!
