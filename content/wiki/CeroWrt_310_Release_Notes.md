
---
title: CeroWrt 310 Release Notes
date: 2013-11-06T07:36:56
lastmod: 2014-07-29T15:28:07
---
CeroWrt 3.10 Release Notes
==========================

{{&gt;toc}}

**CeroWrt 3.10 Beta Test Release Notes**

Current version is **3.10.50-1**, built on 28 July 2014. The current
build can be downloaded from:
http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr See the
**Status** section (below) for more information.

**About CeroWrt**

CeroWrt is a wireless router OS built on the [OpenWrt
firmware](http://openwrt.org) . It is a research project intended to
resolve the bufferbloat epidemic in home networking today, and to push
forward the state of the art of edge networks and routers. Sub-projects
include proper IPv6 support, tighter integration with DNSSEC, and most
importantly, reducing bufferbloat in both the wired and wireless
components of the stack.

**Features**

-   High performance routing in a relatively inexpensive “home” router -
    the Netgear WNDR3800.
-   A major improvement to the problem of bufferbloat. VoIP, Skype,
    gaming, and other latency-sensitive applications continue to work
    well even during heavy up/download.
-   IPv6 support. Another major goal of CeroWrt is to make IPv6
    networking in the home as simple as IPv4. IPv6 subnet assignment and
    other features are enabled, and have been extensively tested on
    comcast's deployment.
-   Linux 3.10.x kernel. Many of the fixes for bufferbloat have been
    implemented in mainline Linux. This means that bufferbloat is
    improving for the rest of the world. http://kernel.org
-   CeroWrt defaults to the fq\_codel queueing discipline that
    implements the
    [Codel](http://www.bufferbloat.net/projects/codel/wiki) algorithm
    from Kathie Nichols and Van Jacobson along with Eric Dumazet's
    adaptation of Fair Queueing (fq\_codel) on top. 
-   CeroWrt also includes these queueing disciplines for
    experimentation: fq\_codel, efq\_codel, nfq\_codel, sfq, codel,
    ns2\_codel, RED, ARED, SFQRED, QFQ and Cisco's PIE.
-   Babel routing protocol with source specific routing
    support (babels). [Source Sensitive
    Routing](http://hal-univ-diderot.archives-ouvertes.fr/docs/00/94/72/34/PDF/source-sensitive-routing.pdf)
    allows for multiple exit nodes on IPv6 and IPv4 among other things.
-   Improved DNS handling by incorporating dnsmasq for both DNS and
    DHCP support. CeroWrt 3.10 enables DNSSEC by default, but see note
    in the Status section.
-   Incorporates <link>CeroWrt\_and\_BCP38|Best Common Practices
    38</link> (BCP38) to defeat Denial of Service attacks which employ
    IP Source Address Spoofing.
-   Adequate entropy for the random number generators, for better
    encryption (WPA, SSL), ethernet drivers, etc.
-   All the features expected from a modern small office/home (SOHO)
    router:\
    - Dynamic DNS to establish a static DNS name even if the IP address
    from your IPS changes\
    - UPnP (Universal Plug and Play) and SSDP proxy that allows DLNA
    discovery across CeroWRT's routed (not bridged) interfaces\
    - mDNS (multicast DNS) that both allow other computers on the local
    network to find each other \
    - Polipo caching web proxy\
    - All the features of the OpenWrt distribution, including the
    attractive LuCI web GUI for configuration. We track the OpenWrt
    development code base (“Barrier Breaker”) and incorporate the
    capabilities of that distribution. http://openwrt.org and
    http://wiki.openwrt.org/doc/howto/luci.essentials
-   CeroWrt has a broad set of useful packages built-in or
    optionally loaded. See the list of Major Packages below.

CeroWrt remains a vehicle for research around many aspects of
networking, both in SOHO and high-performance settings. CeroWrt is only
built for the WNDR3800 router (or the similar WNDR3700v2 model) so we
can spend our time on these new features without worrying about hardware
compatibility. We actively push our developments back into the mainline
kernel and OpenWrt's Barrier Breaker sources so these features will
become available in other equipment.

**Status**

The current CeroWrt release is code-named “Toronto", and has proven to
be highly stable, both from an ordinary operational standpoint as well
as being able to survive heavy load testing. Many people are using this
beta release of CeroWrt as their primary router, and we encourage you to
do so as well.

-   Download the current build from:
    http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr
-   Use the [installation and configuration
    instructions](http://www.bufferbloat.net/projects/cerowrt/wiki/Installation_Guide)
    to get up and running.
-   See also the <link>Debugging CeroWrt</link> page for information to
    collect when submitting trouble reports.

**Open Issues**

-   We are hopeful that this version fixes a nasty wifi ( \#442 ) bug,
    but we are still testing.
-   DNSSEC is enabled by default, but we are still seeking a robust
    method for getting an accurate time on boot before we can release a
    version we can call stable. (There's a chicken and egg problem...
    DNSSEC requires an accurate time stamp; To look up the current time,
    CeroWrt needs to talk to an NTP server; to find an NTP server,
    CeroWrt needs to do a DNS lookup. There are a few solutions: we need
    to choose one that's robust.)
-   \[Fixed\] Releases 3.10.36-4 (9 Apr 2014) and later also include the
    fix for the major OpenSSL bug, "heartbleed", see:
    http://heartbleed.com/ )

**What has Changed since CeroWrt 3.7.5-2:**

-   Linux 3.10 kernel which has incorporated many fixes to bufferbloat,
    as well as finding many long-standing errors in the TCP/IP stack.
-   A GUI for setting Smart Queue Management (SQM) parameters for
    slower links. See <link>Setting\_up\_SQM\_for\_CeroWrt\_310|Setting
    up SQM for CeroWrt 3.10</link>.
-   CeroWrt defaults to fq\_codel on the ge00 (wide area) interface,
    using the simple.qos queue setup script
    (see /usr/lib/sqm/simplest.qos)
-   Updated packages for:\
    - DNS and DNSSEC using dnsmasq
    (http://www.thekelleys.org.uk/dnsmasq/doc.html);\
    - Native IPv6 as well as 6in4, 6to4, IPv6 NAT, etc.;\
    - Babel Routing protocol
    (http://www.pps.univ-paris-diderot.fr/\~jch/software/babel/);
    (quagga and olsr and BATMAN are available as options)\
    - mDNS (http://avahi.org/);

<!-- -->

-   Much work to support the current dnsmasq for both DNS naming as well
    as IPv4/IPv6 address assignment
-   <link>CeroWrt\_and\_BCP38|Best Common Practices 38</link> (BCP38) is
    on by defaut to defeat Denial of Service attacks which employ IP
    Source Address Spoofing.
-   Deep scrutiny of the entire Linux networking stack has identified a
    number of errors which are fixed in CeroWrt and also pushed back
    into the Linux kernel, including TSO handling; improvements of RTT
    computations; fixed many unaligned access traps in the IPv6 code.
-   Incorporates work to improve the entropy for /dev/random
    and get\_cycles()
-   Firewall improvements; block external access to SNMP (port 161) by
    default; uses pattern matching syntax to simply/decrease number of
    filter rules.
-   Includes recent Cisco PIE queue discipline for comparison with
    fq\_codel
-   Web interface on port 81 is now using HTTPS by default with perfect
    forward secrecy

**Major Packages distributed with CeroWrt:**

*<span
class="release. full a make we when updated be will They beta. current the in versions the reflect not may numbers package these Note:"></span>*

-   **DNS Packages:**\
    - dnsmasq-dhcp6 2.71\
    - avahi-daemon 0.6.31-5 - reflector for zeroconf/mDNS-SD/Bonjour
    names

<!-- -->

-   **IPv6 Packages:**\
    - 6to4 version 12-1 - IPv6 tunnel through IPv4 (not turned on by
    default)\
    - 6in4 version 15-1 - IPv6 tunneling (not turned on by default)\
    - 6rd version 5-1\
    - iptables & ip6tables version 1.4.21-1 - iptable firewall for v4
    and v6\
    - kmod-ipt-nat6 version 3.10.32-1 - IPv6 NAT

<!-- -->

-   **Routing:**\
    - babels version 20131225-git-3-1 - Routing code

<!-- -->

-   **Diagnostic/measurement tools:**\
    - snmpd version 5.4.2.1-5 - for monitoring network traffic\
    - netperf-latest version - 2.6.0r658-4

<!-- -->

-   **Other tools/package:**\
    - Linux 3.10.32 kernel\
    - mosh server version 1.2.4-1 - an SSH alternative (optional)\
    - All the tools installed by default on an OpenWrt router\
    - Polipo version 1.0.5-3

Progress Notes - Earlier Releases
=================================

The following items are the rough notes that accompanied each of the
updates from 3.7.5-2 to the current build.

CeroWrt 3.7.5-2 - 3 Feb 2013
----------------------------

Previous stable "Modena" release

3.8.6-2 - 7 Apr 2013
--------------------

Up to Openwrt head

**** DONE update to dnsmasq 2.66rc4

**** DONE update iptables\
 But is there npt66 support?

**** DONE fix igmp patch

**** DONE update quagga, netperf,

**** TODO babel refresh

**** DONE Change name to berlin

**** DONE Fix kernel config for additional TCPs

3.8.6-3 - 10 Apr 2013
---------------------

This has a merge from openwrt from over the weekend (fixes to
qos-scripts, some ipv6 gui support, I forget what else)

also the requested mtr package is built and available via opkg.\
the openvpn gui didn't build.

3.8.8-4 - 24 Apr 2013
---------------------

+ Refresh to openwrt barrier breaker head

 this now contains nearly all the patches formerly separately in
cerowrt!

 ++ fq\_codel is on by default on ALL interfaces with default quantum of
300\
      (yes, openwrt has obsoleted pfifo\_fast!)\
 ++ unaligned access patches, etc, etc\
 + dhcp-pd SERVER support\
the usual multitude of other openwrt fixes... all tested extensively\
at the battlemesh conference.

+ Update to dnsmasq 2.67test2

Toke got really busy in building his own version of cero and adding

+ AQM scripts and gui\
+ tahoe-lafs added (untested)\
+ uftp4 updated

- no upnp/ssdp fix because I'm clueless

3.8.13-3 - 18 May 2013
----------------------

Very much a development release - I want to clearly note that I can
crash the router over wifi using the rrul test easily. I can
(furthermore) crash the x86 linux-3.9.2 iwl driver on my laptop even
more easier than I can crash the router. The combination of the two
problems are making debugging impossible.

So... pretty please... with sugar on top... don't install this on your
default gw?

If on the other hand, you have a jtag debugger handy, and don't have a
iwl card on your laptop, and can look into the wifi issues, please do
so... (all you have to do is bump up /etc/xinetd.d/netserver to 16 and
run the netperf-wrapper against it for a few minutes)

There are otherwise a huge number of interesting things that have
accumulated for this release cycle.

I was very happy that most of what was in Modena has landed in openwrt
and the mainline linux kernels last month. Relieved, actually. I felt
that I could take a break... even thought I could quit... spent a few
days on a beach in Morocco and got bored to death... so....

The BIG new thing in this release is a version CISCO's PIE AQM
algorithm, which after nearly a year of development and analysis was
released as open source last week. The version of pie I just put in cero
has not been fully verified to be correct, but has the additional
features of ECN and TSQ support over the original. I hope to bake this a
lot more over the coming week. (the wifi issue is annoying but secondary
at the moment to finally! finally! fiddling with PIE)

There was the usual huge resync with openwrt. dslite landed recently in
particular, but there have just been a huge number of updates across
the board that I've lost track of. FW3 for example, is a fast, in-c
replacement for the old firewall scripts, and openwrt is now using
multi-table support in preparation for handling src/dst routing better.

Toke contributed tahoe-lafs and suggested trying out the tinc vpn
system, so those are available as an optional package. tinc is kind of
neat. a meshy vpn system. Never heard of it before now.

Toke also has been a great help elsewhere, notably in getting a gui and
scripts going for the backend AQM system, working on a new build
script to make it easier for others to build cero, and lots, lots more.\
Rich Brown & Toke updated the onboard documentation significantly\
Electra convinced me to make batman-adv available (but not enabled) by
default\
Babeld 1.4 has a new convergence smoothing algorithm (but quagga-babeld
is still the default)\
OpenWrt's QOS web page and backend scripts have been replaced by the new
AQM page\
The AQM scripts are now correct for EF and ECN.\
fq\_codel is now the default on everything with a quantum of 300

3.8.13-7 - 12 June 2013
-----------------------

I've had it up and running a few days on a couple routers,

and yes, I'm still trying to take some time off but:

+ can't crash it over wifi anymore\
+ AQM + gui is coming along, am looking at gargoyle's methods a bit
now...

- Known bug: 6in4 does not work via the gui or openwrt config file -
this bug has existed for about a month now\
and I haven't looked into it. I did look into fixing fq\_codel
performance under 6in4, and that patch is in here,\
so after a bit more testing I'll try to get that upstream...

- the results I get from 802.11e are even more dismal than usual when
the VI and VO queues are in full use.\
+ For purely best effort wifi traffic, things look pretty good.

I am seriously considering disabling 802.11e negotiation in the next
release.

I did prove 6in4 is working with the std-from-hurricane-electric script,
so it's a bug in netifd, cero's config, or elsewhere at the openwrt
level...

modprobe ipv6\
ip tunnel add he-ipv6 mode sit remote \$the\_he\_tunnel  local
\$my\_local\_ip ttl 255 tos inherit

1.  Note that I don't know if openwrt turns on tos inherit or not, btw,
    need to look into it. It's potentially useful

ip link set he-ipv6 up\
ip addr add \$mylink/64 dev he-ipv6\
ip route add ::/0 dev he-ipv6\
ip -f inet6 addr

??? - Mid June 2013
-------------------

- Work on htb queuing (Only affected ATM?) - lots of problems, helped
straighten out in CeroWrt and also other distros/kernel?

- Tweak for Windows file sharing (see Robert Bradley, 21 Jun 2013)

- Toke's note re: CeroWrt build script - 30 Jun 2013

3.10.10-1 - 9 Sep 2013
----------------------

+ readlink fix (hopefully fixes sysupgrade)\
+ usual merge with openwrt head (tons of ath9k changes)\
+ dnsmasq 2.67test10\
+ ipv6subtrees back in\
+ the final htb atm patches\
+ eliminated maxpacket check in codel

- did not fold in edumazet's new fq code\
- 100% totally untested. May a braver soul than I give it a shot. I
won't be near a cero box til thursday, otherwise.

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.10-1/

-I'm not sure if I got the "last" of the aqm gui patches in there or
not...

...

Anyway... I had hopes to get a stable release out in august. I AM very
happy about the major stuff that got fixed, instead... but...

Since we didn't... I now have a ton of other matters piled up. Not least
of which is a pending trip to england and the eu.

So for the next month I don't see how I'm going to be able to put more
than a day a week into cerowrt. Tops. So I have tagged up this
"release" and pushed all the baked portions of the sources to github.
I'm still a little dubious of the ipv6 subtrees bit....

3.10.13-2 - 1 Oct 2013
----------------------

+ Proved it is possible to build an OS release on a "Narrowboat"\
-  but not test one without hacking at the 12v power supply off the
solar panel\
+ merge with openwrt head\
+ dnsmasq 2.67test17\
+ ipv6subtrees now part of 3.10.12\
+ htb adsl fixes also\
+ Simon kelly is starting to finalize dnsmasq 2.67 now that summer is
over

- still no fix for the sysupgrade bug\
- Most of the get\_cycles() and /dev/random keruffle has settled down\
but I did not fold the latest patchset for that into this. The\
discussion on PRNGs was very illuminating and worth reading.There were\
multiple threads on this topic on lkml, this is one:

https://lkml.org/lkml/2013/9/10/188

- I'd meant to push out some fixes to codel to the kernel mainline,
didn't.\
- PIE was submitted to the kernel mainline a few days ago but was\
kicked back, also that version as submitted is pretty different from\
what is in cero\
- Been trying to find a sane answer for dns-sd support and haven't found
one.

I will be returning to the US a bit early (tomorrow) and hope to gain\
a week to solidify cero some more towards getting towards an honest\
beta. But: If you are happy with previous dev builds I don't think\
there is reason to use this one.

3.10.15-5 - 14Oct2013
---------------------

totally untested. I will be back in front of a router in the yurtlab\
monday morning  PDT.

+ resync with openwrt\
- revert back to dnsmasq 2.66 (openwrt head)

Judging from the conversation it sounds like the dnsmasq bug may well\
not be the latest dnsmasq at all! but a modern openwrt not interacting\
with the multiple devices correctly. So I've reverted dnsmasq to\
openwrt head to test that assumption...

... in the morning. Unless someone beats me to it.

3.10.17-1 - 20 Oct 2013
-----------------------

+ sync with openwrt\
+ dnsmasq 2.67rc4\
+ get\_cycles() and /dev/random fixes\
+ mild firewall changes\
+ actually sort of tested\
-  sysupgrade still busted\
- didn't package the jitter rng

The simple expedient of putting a script in /etc/rc.local to restart\
pimd, minissdpd, and dnsmasq 60 seconds after boot appears to get us a\
working dhcp/dns on the wifi interfaces once again.

dnsmasq wasn't busted, it was how it interfaces to netifd. the march\
down to something deployable resumes with rc4.

This is the first test that I know of, of some of the RNG fixes\
upstream, notably the mips code does the right thing with a highly\
optimized "get\_cycles()".

There are two changes to the firewall code

1\) There has been a long-standing error in not blocking port 161\
(snmp) from the outside world. It is now blocked by default.

Although I am not aware of any exploits of this (besides the\
information leakage) I would recommend blocking this port by default\
on your existing builds, also, or disabling the snmp daemon entirely\
if you do not use it.

2\) Usage of the "pattern matching syntax" on various firewall rules.

Instead of 3 rules for se00,sw00,sw10, and 4 for gw00,gw10,gw01,gw11\
there are now 1 rule for s+ and one rule for gw+

This does not show up in the web interface correctly. I'd also like to\
get to a more efficient rule set for the blocked ports, perhaps with\
ipset...

...

It's sort of my hope that with these fixes that the march towards a\
stable release can resume, and we get some fresh shiny new bugs out of\
this.

Upcoming next are a revised version of pie, more random number fixes,\
and I forget what else.

3.10.17-2 - 20 Oct 2013
-----------------------

- lighttpd didn't work

3.10.17-3 - 21 Oct 2013
-----------------------

+ this fixes the lighttppd bug noted in -2.\
+ has support for signed packages\
+ better random support\
+ tested long enough to check for the -2 regression\
+ Added (slow implementation of) port-mirroring
http://code.google.com/p/port-mirroring/

- doesn't do https yet\
- still abuses rc.local for starting up late daemons

Also - git 378abc says “Added support for port-mirroring via iptables”

3.10.17-5 - 30 Oct 2013
-----------------------

3.10.17-5 has the "final" version of cisco's pie, the "final" version\
of dnsmasq 2.67, and imho was finally feature complete.

regrettably it still has the sysupgrade bug and a bug was found in\
dnsmasq that has not been fully addressed yet, and I haven't had the\
chance to evaluate the differences between this version of pie and the\
last.

It seems wise to stick with 3.10.17-3 for now unless you specifically\
want to play with pie.

3.10.17-6/ 01-Nov-2013 18:44  -   
----------------------------------

+ resync with openwrt\
+ dnsmasq 2.68test1\
+ pie v3 (as submitted to the netdev list)\
- no sysupgrade fix\
- dnsmasq still restarted via /etc/rc.local

3.10.18-1/ 10-Nov-2013 14:47 
-----------------------------

Not sure what the changes were, but it seemed to work better

3.10.21-1/ 01-Dec-2013 17:05  -   
----------------------------------

This is nothing more than a resync with openwrt and a bugfix for\
dnsmasq. It is completely untested.

+ fresh merge with openwrt\
** bunch of ath9k fixes\
+ update to dnsmasq 2.68rc4 (fixes cname and a few other bugs)

- haven't found time to address http://www.bufferbloat.net/issues/436\
   plan to update the machine involved to this version.\
   hope to get more reports from the field. ? Would like to find
someone\
   with comcast ipv6 to try this on....

- the /sbin/mount bug explanation sounded plausible but haven't tried
it\
   will do so shortly

- have several reports of a successful "fragmentation?" crash attack\
  in openwrt in general, but no details.

3.10.21-2/ 14-Dec-2013 11:23  - 
--------------------------------

? 

3.10.23-1/ 11-Dec-2013 10:31  -   
----------------------------------

The upcoming 3.10.23-1 development release has a refresh of mac80211,\
and a bug fix related to multicast, so I have some hope for it.

It has also the latest dnsmasq 2.68 (which fixes a bug in cname\
handling in particular), and also pie v3 but I am (as usual) not in a\
position to test it right now.

It is my hope that now that the bug happens a lot we can track it\
down. Or, that it's fixed. :)

I just put that release up at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.23-1/

It does not have the updated aqm-scripts code and gui (sorry\
sebastian), nor the pie v4 drop that just got rejected for kernel\
mainline. I'll try to do a respin this weekend with those, and poke\
harder at the dma tx issue after I get back in the lab. Thoughts\
towards being able to isolate the cause and minimize the effect are\
welcomed - it's one of the biggest barriers to declaring a stable\
release at this point!

3.10.24-1/ 13-Dec-2013 12:45 
-----------------------------

Build city is now London (not sure where transition happened)

I have applied the patch to the next build of cerowrt-3.10.24-1 \
(see
https://lists.bufferbloat.net/pipermail/cerowrt-devel/2013-December/001734.html
) for\
the wndr3700v2 and 3800 which will be here when the build completes:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.24-1

I have folded this \[patch\] into cerowrt-3.10.24-1. Note that in
addition to\
this problem the last couple builds have been testing dnsmasq 2.68\
which may have also broke at the same time, and I am far from the\
yurtlab right now so I am unable to test before sunday. (use fixed ip\
addrs if it's still busted)

New settings in AQM tab for:\
- Advanced configuration (allows you to choose queueing discipline and
associated setup script)\
- Linklayer Adaption mechanism (allows you to choose between none,
htb-private, and tc-stab, and then set associated parameters)

3.10.24-5/ 16-Dec-2013 12:45 
-----------------------------

+ hopefully nasty interface initialization bug fixed\
http://www.bufferbloat.net/issues/437\
+ dnsmasq 2.68\
+ pie v4\
+ latest AQM & AQM GUI code\
+ TSQ fix (part of 3.10.24)\
+ package signing enabled by default

- I can get a DMA tx error out of it\
- untested as a final set of commits because I've been at it all day\
and I turn into a pumpkin at midnight\
- I still haven't looked at the mount-utils bug (does it mount ext4?\
btrfs? do fsck without that package?)

3.10.24-7/ 22-Dec-2013
----------------------

+ latest "AQM" code (thx Sebastian!)\
+ fix for the major kernel trap (thx Robert!)\
+ babels src routing support by default (thx Matthieu & babel team!)\
+ dnsmasq reload fixes (thx jow!)\
+ resync with openwrt (thx \#openwrt)\
+ Fix for WMM mode in wifi (old patch accidentally dropped)\
+ quagga still available as a separate package

- untested as a whole (only in pieces)\
- There may be more kernel traps lurking\
- babels doesn't redistribute /27s for some reason (and there is no src\
specific routing support in the scripts as yet, either)\
- I chickened out and didn't remove the dnsmasq restart from rc.local\
- Still working on ipv6  stuff (I did test a HE tunnel, which, after\
 disabling 6relayd and uncommenting everything in /etc/dnsmasq.conf\
 "just worked")

Get it at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.24-7/

But I expect I'll get another one out before the new year.

I'd like to settle on some name to replace "AQM" over the holiday.

*NB:* This build didn't work well, and was moved to a "bad" directory on
the download page

3.10.24-8/ 24-Dec-2013
----------------------

+ committed, tagged and pushed\
+ AQM renamed to "SQM"\
+ fixed boo tup problems in ~~7~~ busybox config had changed in openwrt
(thx toke!)\
+ latest "SQM" code (thx Sebastian & Toke!).\
+ ICMP is now deprioritized (helps vs ping floods and sweeps.
hopefully)\
+ fix for the major kernel trap (thx Robert!)\
+ babels src routing support (thx Matthieu & babel team!)\
+ babels distributes all routes (ipv6 and ipv4) on all interfaces its
enabled on\
+ dnsmasq reload fixes (thx jow!)\
+ resync with openwrt (thx \#openwrt)\
+ Fix for WMM mode in wifi (old patch accidentally dropped). VO queue is
effectively disabled now.\
+ quagga still available as a separate package\
+ DMA tx error hopefully gone\
+ Packages signed by default\
+ Portions tested by all you wonderful users

- untested as a whole (only in pieces)\
- There may be more kernel traps lurking - there are several thousand on
boot, but I was unable to trigger any\
- I chickened out and didn't remove the dnsmasq restart from rc.local\
- Still working on ipv6  stuff (I did test a HE tunnel, which,
after disabling 6relayd and uncommenting everything in
/etc/dnsmasq.conf "just worked")\
- STILL haven't got around to fixing the mount utils error in
sysupgrade\
- SQM doesn't start on boot right

Get it at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.24-8/

IMPORTANT NOTES 1: If you have an aqm setting you've backed up - the
filename has changed so you will need to copy it sqm and change your
file to refer to package sqm. Better to recreate from scratch...

2\) and there is some sort of race on first boot that stops the sqm
script from running. (probably module insertion) you will need to toss a
/etc/init.d/sqm restart into /etc/fixdaemons to fix that. Something more
robust is needed. It IS restartable from the gui, but...

I expect I'll get another cero out before the new year. The biggest
problem I see is that I can't get ipv6 from comcast to work. As to that
being cero (6relayd?) or this crappy cable modem, don't know. Need to
setup a dhcpv6 server to test it. I'd also really like to get mosh to
work (I have an ipv6 enabled version in my github), to poke into the
upnp issues with apple boxes, and add https support to the gui (now that
all the random number fixes have stablized)

In looking at traffic the majority incoming from comcast appears to have
diffserv stomped on, so I think an option for squashing inbound diffserv
would be good. (or there is some other problem that has simple.qos
mostly using the background htb bucket)

Also high on my list is figuring out how to use babels to let me setup
ipv6 native, ipv6 tunneled and 6to4 all at the same time, and have it
get routed properly.

the bad 6relayd interaction with dnsmasq has to be resolved somehow. I'm
not sure to what extent the features of dnsmasq and 6relayd intersect. I
keep just disabling it and enabling /etc/dnsmasq.conf. I'd like to get
6relayd to work to see what it does...

Any other outstanding issues that are major? One thing that has really
become apparent has been the need for a comprehensive test suite...

I would still be hesitant to inflict this on spouses and family on
christmas morning, but a Merry Christmas to all, and to all a good Net!

3.10.26-7/ 21-Jan-2014
----------------------

This is a special release intended only for comcast users with ipv6\
capable modems and CMTSes.

NOTE: If you are running any form of tunneling for ipv6 (e.g.
hurricane)\
do NOT try this release, as it breaks badly.

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/comcast/3.10.26-7/

I strongly recommend all cerowrt users on comcast, upgrade.\[1\]

If you are on comcast and dare not upgrade to this, comment out these\
lines in /etc/config/network

\#config interface ge01 \# wan6 on some release.

1.  option ifname @ge00
2.  option proto dhcpv6
3.  option 'broadcast' '1'
4.  option 'metric' '2048'
5.  option 'reqprefix' '60'

and reboot to disable dhcpv6 on the external interface entirely.

I have been having flashbacks to the IPX/SPX transition... but it\
really did bring a tear to my eye to finally have ipv6 connectivity\
for the first time, native. And to see no real difference in RTT\
between ipv4 and v6.

http://snapon.lab.bufferbloat.net/\~d/bev/comcast\_native\_ipv6/

Oh brave new world that may have new protocols in it.

A bunch of other stuff landed in cero, and if you are not tunneling,\
and your spouse and family are willing, you can try:

+ openwrt sync from head\
+ RA spamming filter stopping mega firewall reloads on comcast ipv6 -\
thx steven barth!\
+ switch from dnsmasq to using odhcpd for ipv6 RAs (thx \#openwrt![]()
+ Comcast ipv6 actually tested by me
+ GUI is now https - thx sebastian) (we still have some work left here)\
For snowden points, it also does perfect forward secrecy.\
+ GUI has selectable skins (pick one, any one)\
+ SQM starts correctly on boot and other restarts\
+ SQM now scales better to higher rates\
+ updated on-board documentation ( example:\
http://cero2.bufferbloat.net/cerowrt/index.html )\
+ updated uftp, ccnx, new libnettle package (for dnsmasq 2.69) - thx\
stephen walker\
+ sysupgrade fixed

on the minus side

- We still have some timing problems in picking up the RAs,\
particularly from wifi.\
If you don't get ipv6 addresses on your wifi client after a fresh\
boot of cero,\
reconnect the wifi client. After cero is fully booted. and has\
dhcpv6-pd'd addresses, you'll get them. Usually.

- bcp38: didn't get 'round2it src/dst routing solves half of it\
- updated shaperprobe, ditg, same\
- HT40+ DOES appear to be NOT working. (this has been the case for a
while)\
- Hurricane electric ipv6 tunnels are **badly broken** as in \*will\
disable your router\* with a zillion extra processes.

a huge change in openwrt made saturday was a switch to source specific
routing,

e.g, if you have two ipv6 providers, (or a vpn, and so on)\
stuff from source A will go out the right destination for destination
A,\
and stuff from source B will go out the right destination for\
destination B. At least in theory.

so you will see "from" routes.

root at cerowrt:\~\# ip -6 route\
default from :: via fe80::201:5cff:de41:b841 dev ge00 proto static
metric 1024\
default from 2001:E:L:I:D:E:D:Z via fe80::201:5ccf:fe41:b841 dev ge00\
proto static metric 1024\
default from 2601:X:Y::0::/60 via fe80::201:5ccf:fe41:b841 dev ge00\
proto static metric 1024\
2601:X:Y:0::/64 dev gw00 proto kernel metric 256 expires 345262sec\
2601:X:Y:1::/64 dev gw10 proto kernel metric 256 expires 345262sec\
2601:X:Y:2::/64 dev se00 proto kernel metric 256 expires 345262sec\
2601:X:Y:3::/64 dev sw00 proto kernel metric 256 expires 345262sec\
2601:X:Y:4::/64 dev sw10 proto kernel metric 256 expires 345262sec\
unreachable 2601:X:X:0::/60 dev lo proto static metric 2147483647 error
-128

I figure there is much work to be done to get things like ipsec and
openvpn\
and bird/quagga/babeld to work well again, but source/dest routing was\
desparately needed, so...

\[1\] All my testing was done on an ARRIS TM822G cablemodem. (I have a
profoundly\
low opinion of several other cablemodems, notably the technicolor...)\
There are a few other testers on other cablemodems, please report\
in...

I return now to my regularly scheduled workweek from last wednesday.\
Share and enjoy.

3.10.28-14/19-Feb-2014
----------------------

Get it at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.28-14/

+ all known instruction traps killed\
+ build almost entirely replicatable now\
+ package set almost equivalent to pre 3.10.28 releases\
+ squid added as an optional package\
+ dnssec support for dnsmasq enabled by default\
+ ohybridproxy, mdnsresponder, mdnsd packages optional, not very usable\
frankly, sorting this out is going to take a meeting at ietf homenet\
+ ipv6 tunneling at the same time as native fixed\
+ multiple routing bugs squashed\
(but not clear if default routes are right)\
+ pie v4 and ns2/Xfq\_codel re-incorporated\
+ some sctp support added\
+ pimd apparently fixed (tested with uftp, pimd -r)\
+ fixdaemons script obsoleted\
+ upnpd and natpmp hopefully mostly fixed\
+ usb filesystems tested\
+ gpsd 3.10 (pushed to openwrt also)\
+ sysupgrade was fixed a few releases back\
(please use sysupgrade -n on this release and get a fresh config)\
+ jffs2 version produced (untested)

A huge thanks for the timely intervention by multiple googlers in\
donating some badly needed compute resources. A thanks also to\
Sebastian for some new SQM work, Gabor Juhos for finding the last\
instruction traps (and blogic/cyrus for fixing it), Simon Kelly for\
continuing to make dnsmasq great(er), Toke for beating up dnssec,\
\#openwrt, \#bufferbloat...

... and all you lovely, patient, users.

The negatives are few, minor, but pesky.

- package signing still broken\
- could use an update to shaperprobe for mlab support\
- No nsec3 support in dnssec\
- probable issues with ntp time fetching verses dnssec\
- no procd support for babeld\
- no bcp38\
- concerned about missing usb and 3g device functionality\
anybody got a HUWEI device?\
- if you have dns issues please share them here.\
dnssec can be disabled via commenting out two lines\
we also still have issues in using dns with multiple\
upstreams. Fixes in pipeline.\
- concerned about other source specific routing issues\
particularly interop with tinc, openvpn and strongswan,\
and what happens when interface ipv6 addrs change\
- need to benchmark and improve wifi some more\
- should probably switch to pre-compiling luci web interface\
- haven't looked into ht40+ issues (HT20 is pretty good)\
- needs to stay UP for a while before I'm willing to freeze

Not a lot of this really matters...

I'm hoping this is the best release we've had since\
the comcast disasters. Go forth and test.

I HAVE NOT tested it as a home gateway. I will try to do so before\
saturday. Feel free to beat me to it.

I will try to get out **one** more release before I leave for Britain\
next week.

3.10.28-16/22-Feb-2014
----------------------

Minor release:

latest sqm, some nice fixes for https://dev.openwrt.org/ticket/14092 a\
couple fixes for odchpd, etc....

homestretch.

3.10.32-1/23-Feb-2014
---------------------

THIS BUILD IS NOT STABLE!

DON'T get it at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/bad/3.10.32-1

However, it does contain the following changes:

Tested for all of an hour (as an interior gateway, not external).

Summary: We still have issues with the 5.x ghz channels

On the plus side, a device (Android nexus 7 2.4ghz) works now when\
before it didn't. On the minus side another device (nexus 4 5ghz)\
doesn't. No RX is ever seen\
on that channel...

To keep my facts straight...

+ sync with openwrt head (with all changes pushed to date)\
+ diff added back into system\
+ radsecproxy added as an optional package (allows for enterprise wifi\
logins securely)\
+ updated kernel to current stable\
+ SQM does more of the right thing with "target" at low bandwidths, has\
a few other tweaks, IMHO is nearly ready to go upstream to openwrt\
+ ton of ath9k related fixes

- HT20 is still the default for wireless 5ghz.\
+/- package signing is being reworked\
+/- source specific dns stuff in there but not integrated with netifd\
- no bcp38 still (help?)

I'm hoping we'll soon be able to call the kernel bits of this thing\
"stable". I was hoping we've nailed the last of the major kernel bugs\
at this point.\
the wifi fixes looked good in theory...

https://dev.openwrt.org/changeset/39688\
https://dev.openwrt.org/ticket/14092

NOTE: I'm out of time to work on this for the week, probably.

I will be doing some benchmarking of 3.10.28-16 but have to get on a\
plane for england tuesday, have a lecture at Queen Mary college in\
London thursday, and ietf\
the week following (and another lecture at Cambridge the week after),\
still have to pack, write a bunch of things, etc. I hope we get the\
mdns hybrid proxy and hnetd issues sorted at ietf.

I'd also like to be able to test things like huawei 3g devices\
(commonly available in the EU, but not the US), am not sure all the
required\
modules are built.

3.10.32-9/14-Mar-2014
---------------------

Get it at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.32-9/

I've been running this a few days now with no problems.

+ resync with openwrt head\
+ upnp (when enabled) works with a yamaha receiver, torrent, and a few\
other things\
+ with no ipv6, 0 unaligned instruction traps\
+ Latest SQM code\
+ Latest dnsmasq with dnssec enabled\
+ everything rolled up from the comcast releases

- untested with ipv6 as yet\
- haven't tried blue-ray\
- My nexus-4 still fails to get an address at 5ghz (but felix's\
succeeds) so I'm going to assume\
there's something wrong with my nexus-4. A newer nexus-7 works\
correctly. There were a ton\
of noise rejection patches from openwrt head that made it into this
release...

It looks like you can increase the dnsmasq cache to 9999 and improve\
the hit rate\
on the namebench test without impacting memory much. Not that\
namebench is representative.\
And various test sites for dnssec return green.

In other plus's: a whole bunch of vm boxes were donated by google and\
after a bit of fiddling by travis yesterday the build cluster is in\
the best shape I've ever seen it.

http://buildbot.openwrt.org:8010/buildslaves

It's my hope that by speeding up build cycle time this will make\
openwrt head much more stable,\
and thus cerowrt more stable, and speed up the pending barrier breaker\
release of openwrt by a lot.

I have kind of taken 2 weeks off from cero and have to look at my\
notes for what else is\
a barrier to a stable release. As best I recall my last two wishlist\
items were procd support\
for babeld, and bcp38 support. We have issues still with upnp. hnetd,\
and ohybridproxy are entirely untested, and I am fiddling with the\
auto target/interval calculation with various methods.

3.10.32-12/21-Mar-2014
----------------------

Get it at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.32-12/

-  currently untested (but a really small delta from -10 and -11)\
+ Resync with openwrt head\
+ dnsmasq 2.69rc1 (close approximation thereof)\
+ This is the first release with toke's bcp38 code installed (and\
enabled by default). I am hoping people simply don't even notice it's\
there... (it's off the firewall web page)

Dave Täht writes:

The only problems I foresee happening are:

1\) some devices are dependent on double-nat to be configurable -\
notably most cable modems depend on 192.168.100.1 to get configured\
the first time. I thought about adding that in as a default exception,\
and still may.

2\) People using this on an interior gateway on a complex network will\
need to either disable bcp38 or (preferably) add their rfc1918\
network(s) to the exception list on the interior gateway (not on the\
external gateway). For example, the yurtlab lives on subnets\
172.21.0.0/20.

3\) I am not prescient, however, and the only way to find out what\
problems will be created is to inflict it on\^H\^H\^H\^H\^H\^H\^H kindly
ask\
the cerowrt userbase to try it.

- Jim Gettys tells me that after a day or so of heavy use of\
3.10.32-9, the 2.4ghz radio gets thoroughly wedged after a succession\
of DMA tx errors and only a reboot can clear it.

I am in the process of rebuilding the yurtlab and can get back into\
heavy wifi testing over the next week or so. In the interim,\
please beat up wifi any way you can...

I would really like to get to a stable beta release by the end of the
month.

3.10.34-4/2-Apr-2014
--------------------

+ resync with openwrt\
they seem to be settling down...\
+ Toke's ntp + dnssec stuff\
+ Yet Another Patch to try and isolate the wireless hang problem\
that happens to jg every day or so and nearly no-one else.\
+ Fix to babel's meshing interfaces\
+ dnsmasq updated to head (seems to be stabilizing)\
+ Tested for a couple hours

- I am under the impression we haven't enabled "auto" for\
target and interval yet in SQM.

-There is some stuff in here I don't grok yet like this

Author: cyrus <cyrus at 3c298f89-4303-0410-b956-a3cf2f4a3e73>\
Date: Tue Apr 1 18:52:09 2014 +0000

odhcpd: add preliminary support for managed DHCPv6-PD and CER-ID

3.10.36-3/7-Apr-2014
--------------------

+ Resync with openwrt

  This includes a new hostapd and a new version of wireless-testing

+ update to openssl 1.01g - closes CVE-2014-0160

- totally untested as yet (I am away from my routers and have other\
fish to fry right now)

3.10.36-4/9-Apr-2014
--------------------

as usual, it can be found at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.36-4/

+ dnsmasq 2.69 with dnssec enabled by default\
+ possible workaround for wifi bug \#442 in increased qlen\_\*\
+ fix for ipv6 access to https://gw.home.lan:81\
+ fresh merge with opewrt\
+ update to 2048 bit cert generation\
+ fix for openssl heartbleed (fix also in -3) bug\
+ tested for an hour\
+ change to sqm to basically always use "simplest.qos" on inbound

- I'm very, very, very, very, very, very, very, very, very tired.

I really hope this results in a stable cerowrt. Please beat the hell out
of it.

I'm already planning a vacation.

3.10.36-6/19-Apr-2014
---------------------

as usual, it can be found at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.36-6/

+ felix's wifi patch for bug \#442 added\
  please break wifi.

+ debloat qlens reduced again to 12 for be and bk wifi queues\
+ heartbleed fix from -3 forward

I note that nearly every "secured"-by-openssl network facing daemon has
been\
shown vulnerable to heartbleed. The hole in openvpn bit **me**, in\
particular. I've updated, rekeyed and re-certified the vpns I have in\
place, and you should too for any openvpn servers and clients you have\
too.

It was a real PITA for me, and I only had a few boxes on it.

For more details, see:
http://community.openvpn.net/openvpn/wiki/heartbleed

For more details on the daemons potentially affected by heartbleed in\
cerowrt, openwrt, and others, see the advisory at:

http://www.bufferbloat.net/news/50

+ resync with openwrt\
  notably there were updates to netifd, and a fix for a strongswan CVE

+ dnscrypt added as an optional package (thx stephen walker and
"mailjoe")\
+ snort added as an optional package

+/- full dnssec\
- upgrade to httping 2.x broke\
- no sqm autotuning yet\
- neither snort nor dnscrypt tested

If you are not experiencing problems with wifi or with heartbleed\
there are few reasons to update to this release.

If you use sysupgrade without a clean reflash, note that the\
/etc/opkg.conf file is not re-written in this case, and still points\
to the old repository. If you wish to install additional packages\
after an inplace upgrade, you will also have to update /etc/opkg.conf
to\
point to the right directory (with the proper version number).

3.10.40-5/18-May-2014
---------------------

*No published change notes*

3.10.40-6/27-May-2014
---------------------

As jg was able to get the darn wifi to hang daily still, and I have
several\
private reports of wifi issues as well - I spent the last weeks
building\
up the yurtlab and software to take an indepth look at thrashing\
the problem harder and harder. (and then took the holiday off)

Get it at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.40-6/

+ refresh to openwrt-head and wireless-testing head\
+ ton of fixes in wireless - including a memory leak fix in mac80211,\
and a fix on the ath9k rx path. (thx felix)\
+ procd leak fixes\
+ dnsmasq 2.71

- untested as yet\
- put 802.11e back in (at least for now)

There's also an archer c7v2 build that I think has a working switch now,
but\
I can crash that ath10k with a sharp look.

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/archer/3.10.40-5/

I will be flashing this stuff much later this afternoon. Feel free to
stay clear\
til I do...

3.10.44-3/17-Jun-2014
---------------------

3.10.44-2 was something of a disaster, so I recut it, and\
have been using 3.10.44-3 as my main gw for an hour or so...

Get it at:
http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/archer/3.10.44-3/

+ all homewrt stuff ripped out\
+ huge resync with openwrt head\
  among many other things this includes a lot of rework of the wifi
drivers\
  which may have some influence on bug 442\
  update to iproute2\
  many updates all across the board\
+ sqm fixed to work with modern luci (thx Magnus Olsson!)\
+ Rich Brown's cerowrt-scripts installed for the first time by default
-\
  bug: they need to have -4 or -6 specified for certain targets, and\
two of the targets in circulation\
  are not responding to netperf (try netperf-west.bufferbloat.net)

  It could use a gui for running the test and displaying the results...

- tested for about an hour...\
- it is possible to switch dns servers from odhcp to dnsmasq and vice\
versa via changing maindhcp in /etc/config/dhcp (not tested)\
+ conflict between avahi-daemon and mdns. mdns is now optional.

- the hnetd, mdns, and mdnsproxy work is still in progress, and these\
daemons are built but not installed by default. And installing them\
leads to major system instability, so don't do that unless you are\
prepared to debug over a serial port and factory reflash.

I would generally discourage everyone from installing this as your\
main router, but I know how effective that is. Certainly if you are\
experiencing wifi hangs this is worth trying.

3.10.44-5/24-Jun-2014
---------------------

\[ Get 3.10.44-6, listed below \]

+ resync with openwrt head\
updates to iw, mac80211\
various routing table fixes in netifd

+ dnsmasq 2.71 with mini-gmp and libnettle mainlined\
also moved into procd for better automagic restart\
(this leaves babel as the only major daemon not managed by procd. sigh)

- totally untested (I tested 3.10.44-4 pretty thoroughly though)\
I won't have time for this personally 'til later this week.\
- still no answer for bug 442 - I do get bad things to happen on a\
ubnt device now\
- left off on the homewrt integration for now

I need to get around to submitting sqm upstream again, but am busy on\
other tasks.\
IETF is coming up, also.

3.10.44-6/24-Jun-2014
---------------------

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.44-6/

+ tested for all of 20 minutes - I intend to start a major test series
overnight\
and beat the c\*\*p out of it and the other devices I'm working on.
feel\
free to wait to install.

+ fixed the basic problems with the -5 build\
+ same update from openwrt head as in -5.

+ mdnsd nuked again (ultimately we're going to switch to it but not now)

I had to completely strip mdnsd out of the build to make it go away\
(./scripts/feeds uninstall mdnsd)

+ natpmp was conflicting with the same (new unified) functionality in\
miniupnpd, si I nuked natpmp.\
not clear if better firewall rules are needed yet, the ipv6\
functionality scares me.

- see some errors like:

Wed Jun 25 03:29:13 2014 daemon.warn miniupnpd\[4119\]: SSDP packet\
sender 172.21.2.5:34062 not from a LAN, ignoring

+ netserver started again from xinetd

- it looks like the ntp monitoring thing toke did is not working\
and/or we're running the wrong ntp now\
but dnsmasq does not run with timechecks enabled by default, so we do\
dnssec correctly with invalid time until something sends a sighup

...

I'm really looking forward to the barrier breaker freeze.

I am doing no more builds until I replicate bug 442.

3.10.48-2/18-Jul-2014
---------------------

Get it at:
http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.48-2/

+ resync with openwrt head\
(it's not clear how to deal with the barrier breaker freeze yet)\
+ hopefully a fix for bug \#442\
- but only extensive testing will tell\
- we have some rumored negative data so don't get your hopes up\
+ sqm improvements\
inbound diffserv squashing works now as does not squashing - you can
actually\
see inbound shaping working semi-properly now if you choose to trust\
your inbound connection's classification.\
gui support for above\
+ babel improvements\
latest source specific code from the main openwrt-routing repo\
simplification of the default route export mechanism\
diversity routing enabled by default\
link detection enabled by default\
(if you aren't using babel, just disable it)

- wire-incompatible change to babels\
if you are using babels on another router you don't want to upgrade,\
you will need to uninstall the babeld package and install the current\
babels package from this release. Carefully, as you need to copy over\
the new config files (/etc/firewall.user /etc/babeld.conf\
/etc/config/babeld) from this release also.

- I am focused on getting ready for ietf, and thus unable to give ipv6\
a shakeout without risking my vpn failing while I'm away. I was hoping\
to get some time tomorrow to deploy on ipv6. It's looking less likely\
by the minute, I'd rather have an extensive test up and running\
continuously before I leave of what I got.

- I won't have time for another release for 2 weeks. If it breaks in\
some new, crazy way, please revert to a prior version.

3.10.50-1/28-Jul-2014
---------------------

+ resync with openwrt head\
In particular felix nailed another wifi bug. I do hope bug 442 is\
thoroughly stomped now.\
+ bcp38 is now openwrt mainlined (yea toke!)\
+ some fixes to the sqm system by sebastian (thx!)

- untested (not in a position to test today, might be tomorrow)\
- not against barrier breaker branch (yet)

I have some hope that this is getting close to being a release
candidate...

Get it at:

http://snapon.lab.bufferbloat.net/\~cero2/cerowrt/wndr/3.10.50-1/

NB: This version was re-built on 28Jul2014 to fix lighttpd config
problem. Kept same version number.
