
---
title: Enable_ECN_on_multiple_operating_systems
date: 2011-06-21T08:15:20
lastmod: 2011-06-21T08:16:24
---
Enable ECN on multiple operating systems
========================================

Solaris
-------

OSX
---

Linux
-----

FreeBSD
-------

notes to sort out:

\[Tue Jun 21 2011\]\
<bmc> What was the name of the bufferbloat-related sysctl parameter on
Linux?\
ECN? I'm drawing a blank. \[07:43\]\
<dtaht> ?\
<dtaht> Got your plug?\
<bmc> <FONT>Up and running.</FONT>\
<dtaht> heh\
<bmc> <FONT>net.ipv4.tcp\_ecn</FONT> \[07:44\]\
<bmc> <FONT>That's it.</FONT>\
<dtaht>
http://www.bufferbloat.net/projects/bloat/wiki/Dogfood\_Principle\
<bmc> <FONT>I have it set to 2 which, as I recall, means "try ECN, but\
fallback if it's not there"</FONT>\
<dtaht> no, it's worse than that\
<dtaht> secondly this only applies to connections initiated from or to
the\
router \[07:45\]\
<dtaht> dsack, and sack are good too\
<bmc> <FONT>But it should help with NAT'ed connections, no?</FONT>\
<dtaht> I just got a guruplug version of openwrt built, but debian is
WAY\
easier to deal with.\
<dtaht> no\
<dtaht> proxied via something like polipo, yes \[07:46\]\
<bmc> <FONT>Hmm. But the original problem you had here was that my
crappy\
Linksys didn't grok ECN at all, and you had ECN = 1 on your Linux\
box. Right?</FONT>\
<dtaht> right \[07:47\]\
<dtaht> your router was not passing through the ECN bits - dying
terribly.\
<dtaht> Now you should be able to turn it on on the rest of your
internal gear\
<bmc> <FONT>So, if my plug router groks ECN, and I enable ECN on it, I
gain …\
what?</FONT>\
<bmc> <FONT>It's a flow-control thing, isn't it?</FONT>\
<dtaht> and have all the relative theoretical chocolaty goodness\
<dtaht> yes\
<dtaht> marking rather than dropping packets is a theoretical goodness
\[07:48\]\
<bmc> <FONT>Right. So, bottom line, I want to enable it on the plug,
and\
enable it (set to 2 or 1) on the various internal machines.</FONT>\
<dtaht> yes.\
<bmc> <FONT>Interesting. Out of the box, the plug's Debian has:</FONT>
\[07:49\]\
<bmc> <FONT>net.ipv4.tcp\_sack = 1<BR>net.ipv4.tcp\_ecn =\
2<BR>net.ipv4.tcp\_dsack = 1<BR></FONT>\
<dtaht> that are the best defaults for yesterday's internet. The new
hotness\
is ecn\
<dtaht> :)\
<bmc> <FONT>The internal Ubuntu servers are similarly
configured.</FONT>\
<dtaht> yep\
<dtaht> ECN breakage was a real problem\
<bmc> <FONT>Yes, but, IIRC, ecn=2 is essentially ecn=1, with a fallback
to\
oldness.</FONT> \[07:50\]\
<dtaht> in fact, we've fixed ECN, TOS, and Diffserv problems all over
the\
Linux stack in the last month.\
<dtaht> ummmm\
<bmc> <FONT>Or did I misunderstand your original explanation?</FONT>\
<dtaht> Or I was drunk...\
<dtaht> ecn = 0 entirely disabled\
<dtaht> ecn = 1 enabled\
<bmc> <FONT>Right. I got that.</FONT>\
<bmc> <FONT>What is ecn=2?</FONT>\
<dtaht> ecn = 2...\
<dtaht> I think means accept it if presented but don't initiate it...
Wait one\
\[07:51\]\
<dtaht> yea\
<bmc> <FONT>Ah. So, ecn=2 on the router is fine, but I want ecn=1 on
the\
internal client machines.</FONT>\
<dtaht> so ecn=1 is good, and a fallback, like ecn=3 - if it existed,
which\
would have the desired fallback behavior would be good \[07:52\]\
<dtaht> there's a patch for that coming, I think\
<bmc> <FONT>Sounds like I should leave the router at 2, in case there
are\
internal machines (e.g., windows breakage) that don't do ECN.</FONT>\
<dtaht> heh\
<dtaht> I'm not aware of ecn=1 breaking on ANYTHING except your old\
router. You were the first, the last, and the worst.\
<dtaht> but whatever\
<bmc> <FONT>I'm just trying to grok this stuff.</FONT> \[07:53\]\
<bmc> <FONT>I'll try 1 on the router, see what happens.</FONT>\
<dtaht> it helps to have qos on the router that applies it to streams
that are\
killing your life, rather than drops it... But that's not a huge issue\
for you as you have bandwidth to burn.\
<bmc> <FONT>Man, this dream plug is sweet. Tiny, small footprint
(physical and\
electrical), quiet as all fuck, and real \*nix, to boot.</FONT>\
<dtaht> thx for tryin it. How does the 'dreamplug' feel? Is it a better
piece\
of gear?\
<dtaht> hahha\
<dtaht> answered my question in advance \[07:54\]\
<bmc> <FONT>Way better. I resurrected the GuruPlug, via the JTAG. Trying
to\
decide whether I have a use for it.</FONT>\
<bmc> <FONT>Or whether I should give it to someone (e.g., Costine) and
spread\
the love.</FONT>\
<dtaht> yea, I loved the openrd, but the interviening releases of
sheevaplug\
and guruplug left me cold. I'm also not happy with the wireless chip,\
but that's relatively minor.\
<dtaht> spread the love, man....\
<bmc> <FONT>That's what I'm thinking. … Okay, time for a conf call. By
then,\
my kid should be awake and ready for waffles.</FONT> \[07:55\]\
<bmc> <FONT>BTW, the wireless is working just fine here.</FONT>\
<bmc> <FONT>I use rc.local to adjust the params via uapctl.</FONT>\
<dtaht> yea, well, start moving to the edge of the range and then watch
your\
ping times....\
<bmc> <FONT>Not an issue here.</FONT>

-   dtaht plans to get one of these puppies too, after bmc is happy for
    a few\
    weeks.\
    <bmc> <FONT>I have four WAPs in this interference-laden place.
    :-)</FONT>
-   dtaht is using diversity mesh routing now with babel \[07:56\]\
    <dtaht> babel + ahcpd is sweet\
    <dtaht> sit down, plug in the laptop\
    <dtaht> it figures out it's on wired\
    <bmc> <FONT>Something to look into, when I have time. If I ever have
    time\
    again.</FONT>\
    <dtaht> unplug, it figures out you are on wireless\
    <bmc> <FONT>Niiiice.</FONT>\
    <dtaht> streams, and connections, STAY UP\
    <bmc> <FONT>Very sweet.</FONT>\
    <bmc> <FONT>Okay, time to make that call. Later.</FONT>\
    <dtaht> yea, it's amazing how freeing it is to be able to plug in
    again.\
    <dtaht> later \[07:57\]\
    <dtaht> thx\
    <dtaht> also the mesh routing 'diversity' means that I have several
    nodes that\
    route over 5.x ghz and are aps over 2.4, and vice versa... Connect\
    your neighbors\
    <dtaht> whenever you get time I wanted to know how that meeting
    turned out.\
    \[07:58\]\
    <bmc> <FONT>What meeting?</FONT> \[08:00\]\
    <dtaht> some users group meeting of all the users groups \[08:07\]\
    <bmc> <FONT>Right. I went to a lot of meetings last week. :-) That
    went\
    well. We're moving forward, trying to get common venues, common\
    calendars, etc.</FONT> \[08:10\]\
    <bmc> <FONT>FYI, on Mac OS X:</FONT> \[08:12\]\
    <bmc> <FONT>\$ sysctl -a | egrep
    'ecn|sack'<BR>net.inet.tcp.ecn\_initiate\_out:\
    0<BR>net.inet.tcp.ecn\_negotiate\_in: 0<BR>net.inet.tcp.sack:\
    1<BR>net.inet.tcp.sack\_maxholes:\
    128<BR>net.inet.tcp.sack\_globalmaxholes:\
    65536<BR>net.inet.tcp.sack\_globalholes: 0<BR>net.inet.ipsec.ecn:\
    0<BR>net.inet6.ipsec6.ecn: 0<BR></FONT>\
    <dtaht> heh. THANK YOU \[08:22\]
-   dtaht wanted a mesh network in philly to implement.\
    <bmc> <FONT>Another data point: (dancer:bmc) \~ \$ uname -s -r
    <BR>FreeBSD\
    8.2-RELEASE<BR>(dancer:bmc) \~ \$ sysctl -a | egrep\
    'sack|ecn'<BR>vfs.bufreusecnt: 932<BR>net.inet.tcp.ecn.maxretries:\
    1<BR>net.inet.tcp.ecn.enable: 0<BR>net.inet.tcp.sack.globalholes:\
    0<BR>net.inet.tcp.sack.globalmaxholes:\
    65536<BR>net.inet.tcp.sack.maxholes:
    128<BR>net.inet.tcp.sack.enable:\
    1<BR>net.inet.sctp.enable\_sack\_immediately: \[08:48\]\
    <bmc> 0<BR>net.inet.sctp.nr\_sack\_on\_off:
    0<BR>net.inet.sctp.sack\_freq:\
    2<BR>net.inet.sctp.delayed\_sack\_time:
    200<BR>net.inet.sctp.strict\_sacks:\
    1<BR>net.inet.sctp.ecn\_nonce: 0<BR>net.inet.sctp.ecn\_enable:\
    1<BR></FONT>\
    <dtaht> sight \[08:50\]\
    <dtaht> sigh \[08:51\]\
    <bmc> <FONT>They're all different.</FONT>\
    <bmc> <FONT>I have OpenSolaris here, too. Want that data
    point?</FONT>\
    <dtaht> sure\
    <bmc> <FONT>Booting...</FONT>
-   dtaht just had 3 new olpcs arrive and is mildly distracted\
    <bmc> <FONT>Nice.</FONT> \[08:52\]\
    <bmc> <FONT>They make good nightlights, I'm told.</FONT>\
    <dtaht> the 1.5s are better nightlights\
    <dtaht> the 1.75s (I'm on the list) are cool\
    <dtaht> I'm trying to convince them to add 5.x ghz support\
    <bmc> <FONT>Every child should have that.</FONT>\
    <dtaht> hahahaha\
    <bmc> <FONT>Hmm… SunOS 5.11. sysctl not found...</FONT> \[08:53\]\
    <bmc> <FONT>\$ ndd /dev/tcp \\?|egrep -i
    'ecn|sack'<BR>tcp\_sack\_permitted\
    (read and write)<BR>tcp\_ecn\_permitted (read and\
    write)<BR></FONT> \[08:58\]\
    <bmc> <FONT>(sunball:bmc) /etc \$ ndd -get /dev/tcp\
    tcp\_sack\_permitted<BR>2<BR>(sunball:bmc) /etc \$ ndd -get
    /dev/tcp\
    tcp\_ecn\_permitted<BR>1<BR></FONT> \[08:59\]\
    <bmc>\
    <FONT>http://download.oracle.com/docs/cd/E19963-01/html/821-1450/chapter4-31.html</FONT>\
    <bmc> <FONT>(Oracle Solaris Tunable Parameters Reference
    Manual)</FONT>\
    <bmc> <FONT>ecn: 0 (disabled), 1 (passive enabled), or 2 (active
    enabled)\
    </FONT> \[09:00\]\
    <bmc> <FONT>Same values for SACK</FONT>\
    <bmc> <FONT>Defaults are as shown above.</FONT> \[09:01\]\
    <dtaht> excellent. \[09:09\]\
    <bmc> <FONT>I just tweeted this: When you've spent the last decade
    mostly\
    using Linux and BSD, the infrequent foray into Solaris feels like
    going\
    to Mars. \#unix</FONT>\
    <dtaht> So if I get you to turn it on, that will only leave about 2
    billion\
    computers left to fix and 10s of thousands or routers left to junk\
    \[09:10\]\
    <dtaht> heheheh\
    <dtaht> solaris is like 1998\
    <bmc> <FONT>I don't even want to think about how one accomplishes
    this in\
    HP/UX.</FONT>\
    <bmc> <FONT>Assuming it's even possible.</FONT>\
    <dtaht> thx for the data I'm going to update the wiki in a bit\
    <bmc> <FONT>Or, for that matter, AIX, which makes Mars seem
    familiar.</FONT>\
    <dtaht> hahahah\
    <dtaht> do these things have sysctl.conf?\
    <bmc> <FONT>I didn't see a reference to an ndd.conf</FONT>
    \[09:11\]\
    <bmc> <FONT>http://www.sean.de/Solaris/soltune.html\#ndd</FONT>\
    <bmc> <FONT>Worth skimming.</FONT> \[09:12\]\
    <bmc> <FONT>Of course, Solaris no longer has an /etc/rc.local,
    either.</FONT>\
    <bmc> <FONT>Instead, you're supposed to create something in
    /etc/init.d\
    (rc.local is fine), then symlink it to an "S" file in the
    appropriate\
    runlevel directory (e.g., rc3.d).</FONT>\
    <bmc> <FONT>**sigh**</FONT>\
    <bmc> <FONT>Wait...</FONT> \[09:13\]\
    <bmc> <FONT>I just ran across this:</FONT>\
    <bmc> <FONT>To set parameters so they remain in effect after you
    reboot the\
    system, add the parameter values to /etc/system when you want to\
    configure parameters for all devices in the system.</FONT>\
    <bmc> <FONT>A startup script can also be used to set a ndd
    parameters across\
    system reboots. Include the appropriate ndd command in a system
    startup\
    script, such as the /etc/init.d/inetinit file or a customized script
    in\
    /etc/rc2.d or /etc/rc3.d. Be sure to make a copy of any files
    before\
    adding the ndd commands.</FONT> \[09:14\]\
    ERC&gt;

http://www.vistax64.com/vista-general/53861-how-do-you-enable-ecn-explicit-congestion-notification.html</FONT>\
\[09:15\]\
<bmc> <FONT>Gotta run. Back later.</FONT>\
ERC&gt;
