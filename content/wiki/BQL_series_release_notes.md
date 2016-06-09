
---
title: BQL series release notes
date: 2012-01-30T14:20:17
lastmod: 2012-03-01T18:19:59
---
BQL series release notes
========================

the 'BQL series' is a topic branch of cerowrt attempting to prove out
various\
new bufferbloat technologies, notably 'Byte Queue Limits' (BQL), and
SFQRED.

When this stabilizes we will move back into a real development cycle
again.

CeroWrt 3.3 Builds
------------------

Virtually all the work being done in the BQL series of builds has been
incorporated into the Linux 3.3 kernel. We have dropped further
development of the BQL series in favor of pushing on with development on
a more mainline core. For more information, see the

BQL smoketest-42 (No Longer Planned)
------------------------------------

-kernel 3.3-rc4\
-bind 9.9 final\
-decently working aqm with adsl support\
~~alternate tcp algorithm support~~

BQL smoketest-40 (14Feb2012)
----------------------------

http://huchra.bufferbloat.net/\~cero1/bql-smoketests/bql-40/

changes in this release:

kernel 3.3-rc3\
bind 9.9rc2\
ntpd + dnssec removed (too buggy)\
snmpd installed by default (for SNMP monitoring)\
fprobe installed by default (for NetFlow monitoring)\
avahi installed by default (for mdns/Bonjour device naming and discovery
across subnets)

sort of better working 'aqm' shaper installed

**** when configured uses hfsc + sfqred

**** still has trouble with ipv6, diffserv, and tcp elephants

**** no adsl overhead support

BQL smoketest-27 (30Jan2012)
----------------------------

http://huchra.bufferbloat.net/\~cero1/bql-smoketests/bql-27/

BQL-27 is the third public release of a BQL enabled kernel build for
cerowrt.

The primary purpose of the bql series is to evaluate and test the new
BQL, improved SFQ, RED, and SFQRED subsystems, while we grope towards a
final product definition.

It should be possible now to thoroughly debloat ethernet behavior, as
well as vastly improve to-upstream dsl/ethernet behavior.

Wireless-n remains a major problem, and is likely to remain one until a
thorough redesign takes place of the aggregation and AP\
layers in Linux. (in other words, we don't expect to make any real
progress on wireless until august at the earliest). That said, the new
algorithms do hold wireless latency 'tighter', under load.

A great deal of additional stuff is included by default, of varying
quality. Due to the size of this build, no jffs2 version will be
available, only the squashfs version works for wndr3700v2 and wndr3800.

I note that the wndr3700v3 has hit the stores and IS NOT compatible with
the v2. Get a 3800 if you want to be future proofed.

The standard [Installation Guide]({{< relref "wiki/Installation_Guide.md" >}}) otherwise applies.

### Features:

-   Kernel 3.2.2 + 3.3 backport of the new BQL and new AQM technologies
-   + Everything that's ever been in cerowrt before!
    (ipv6,mesh networking,bind9,etc)
-   +
-   BQL (Byte Queue Limits) - thx Tom Herbert
-   RED fixed, adaptive RED implemented, SFQ vastly expanded in
    capability, and SFQRED added (thx Eric Dumazet)
-   TX rings can be increased (thx to BQL) for faster networking
    performance
-   debloat script uses sfq instead of txqueuelen
-   Samba 3.6.1 \#314
-   Strongswan 4.5.3 See \#318
-   Working ahcp See \#252 \#322
-   Working isc-bind9 with dnssec See \#316
-   Working isc-ntp See \#316 \#280
-   iperf installed by default (because netperf is so new)
-   netperf upgraded to svn head\
    This breaks backward compatibility with older versions of netperf.
    To use netperf, you will have to install a new version from svn.\
    The principal reason for this upgrade was to gain remote
    TOS/diffserv setting, as well as alternate tcp algorithm support.
-   and much much more.

bql-27 meets the original base feature set intended for rc7.

Some core features may be added, others dropped, as being discussed on
the mailing list.

### Stability

Several hundred GB have been sent through the router with no crashes.
Performance is good. SFQ does wonders under load for things like voip,
short connections, and dns.

### Known Bugs

-   QFQ does not work (hangs under load)
-   The old openwrt AQM shaper is lame. See \#331
-   SFQ is underconfigured on all interfaces. See \#305 and \#332
-   Dibbler segvios and does not configure ipv6 interfaces. See \#274
-   PIM based multicast does not work (uftpd fails)
-   SFQ on an AP is not the best thing for packet aggregation
-   SFQ may now be 'over-optimized' for low latency. See \#332

You'll note that none of these issues are essential for normal
operation, and several have easy fixes already in the pipeline.\
Normal operation is pretty fine, actually.

### Dave's Goals

1\) After evaluating the performance of the current openwrt-based AQM
system, a\
substitute will be implemented. \#306 Regrettably the primary prototype
of that\
was QFQ based. \#312 The SFQRED implementation will be used instead,
which should\
work well, except with bittorrent. Unless I figure out how to do the
same\
thing with DRR, or get QFQ working.

2\) A gui for creating the AQMs and measuring bandwidth will be added\
\#306

3\) Hopefully the wins related bugs with XP vs Vista will be resolved\
by somebody. \#314 I still lack hardware to test that. I do not intend
to\
actually ship samba pre-installed at this point, but can be persuaded\
otherwise if something can be made to 'just work'.

4\) Working ds-lite support (dibbler? wide? what?) \#274

### Dave's wish list

Please give this one a shot. It's the first build to show significant
differences in performance since\
august. Actually, most bottlenecks have moved to my laptop(s) and
servers! I suggest running BQL enabled\
kernels on your desktops/laptops with the 'debloat' script in order to
see best results.

the debloat repository is being maintained separately from cerowrt:

https://github.com/dtaht/deBloat

see src/debloat.

A lot of glue is required as yet to make the various pieces function
smoothly,\
but I do hope you notice a difference in overall performance in normal
use. With a new external AQM we'll do\
better, but I'd like people to be exercising that code, suggesting
features, etc, before I commit\
to starting up a more formal release cycle, and product definition.

I am still toying with the idea of moving forward directly into Linux
3.3, rather than continuing\
to backport to 3.2.

That said, I won't be hurt if you delay until after I get the newest AQM
installed and working by default.

My hope would be mid-feburary for that.
