
---
title: OCEAN CITY RELEASE REQUIREMENTS
date: 2011-05-28T07:10:41
lastmod: 2012-01-28T17:58:17
---
CEROWRT 'OCEAN CITY' RELEASE REQUIREMENTS
=========================================

THIS DOCUMENT IS OBSOLETE
-------------------------

See the <link>OCEAN CITY</link> page.

Objective: Provide a viable substrate for future releases of
<link>bismark:wiki|Bismark</link>, <link>iscwrt:wiki|ISCWRT</link>, and
<link>wisp6:Wiki|WISP6</link>.

Core Requirements
-----------------

Support more <link>targets</link>, notably those with 8MB of flash:
wndr3700v1, nanostation M5.

New features
------------

### Infrastructural pulls

1.  Merge up with openwrt head (now current)
2.  Working mesh support (as available)
3.  IPv6 as landing from wisp6 (as available)

### Bug fixes

1.  Fix for dhcp bug

### Additional Patches

1.  Netem, possibly with TCN http://tcn.hypert.net/ \#169 (delay and
    packet loss)
2.  Improvements to the switch (link detection, AQM, port mirroring)
3.  Additional packet schedulers
4.  Actual packet loss out of the wireless device

### Additional packages

1.  Incorporate ppoe support in the build DONE
2.  optional vpn support DONE Both openvpn and strongswan are available
3.  Bismark built and available optionally

Experimental features
---------------------

1.  KVM version could use 2.6.39 and/or debloat-testing
2.  Polipo enabled in DHCP
3.  Lighttpd used instead of uhttpd

Target release date
-------------------

TBD

Resources required
------------------

TBD
