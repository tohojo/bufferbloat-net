
---
title: Wisp6
date: 2011-03-20T09:32:42
lastmod: 2011-03-20T13:39:35
---
Wisp6
=====

This was [Dave Täht's](http://www.taht.net) project for the last 4
years, 12, if you count the original [Linux based wireless
router](http://the-edge.blogspot.com/2010/10/who-invented-embedded-linux-based.html)
(astounding success), the
[thirdbreak.org](http://replay.waybackmachine.org/20030218111947/http://www.thirdbreak.org/)
effort (failure), [wiline.com](http://www.wiline.com) (qualified
success),
[pocobelle](http://the-edge.blogspot.com/search/label/pocobelle)
(partial success), OLPC and [mesh
potato](http://www.villagetelco.org/about/mesh-potato/mesh-potato-faq/)
(partial success) projects. 17 years, if you count a [hybrid
wireless/modem
design](http://waybackmachine.org/19990215000000*/http://directnet1.net/index.html)
, and [mosquitonet.](http://www.qsl.net/n9zia/metricom/rico.html)

There is a boatload of documentation on wisp6 that exists only in
org-mode in emacs that I've been meaning to put up somewhere.

I have issues in that there are two possible patents involved (defensive
only, and assigned to a worthy organization, maybe OIN, or the IETF),
and a boatload of software IP, and \$XXXk of my own cash expended and
living dirt cheap in the third world, all sunk into the effort, that are
hard to just write off and not entirely up to me. There were many
problems in the project, but [bufferbloat was one of the
biggest](http://the-edge.blogspot.com/2011/03/beating-my-bloat.html)
certainly.

That said, I will document some of the differences here. After
witnessing the collapse of OLPC, I'd given the Wisp6 project no
publicity. After all the effort sunk into trying to make a <link>perfect
wireless router</link> I kept my goals high and expectations low, while
throwing out a lot of conventions that have become bad "standards", for
example, the lack of an integral proxy component and continued wide-band
2.4 ghz usage.

If I succeeded I'd have done something good. If I failed, I'd just go
[surfing.](http://www.nicaraguasurfreport.com/reportlist.php?id_secc=25)

WISP6 Core differences from a conventional wireless router design
-----------------------------------------------------------------

-   Directional 5.X ghz radios (Nanostation M5) in a multi-channel mesh
    configuration

<!-- -->

-   Dual band CPE (dreamplug), also mesh capable, with bind9, proxy, and
    bittorrent support

<!-- -->

-   Greenfield 5.x Ghz 802.11n (for aggregation & higher speed
    multicast support)

<!-- -->

-   IPv6 based multicast routing protocol (babel, babelz)

<!-- -->

-   NTP secured by autokey, with accurate time supplied via GPS

<!-- -->

-   NO BRIDGING, purely routing

<!-- -->

-   Core (backbone) routers had no ipv4 support at all

<!-- -->

-   IPsec used to secure traffic

<!-- -->

-   4in6 encapsulation to the end nodes

<!-- -->

-   Increased MTU from 1500 to handle the changes in encapsulation

<!-- -->

-   bind9 support

<!-- -->

-   json based autoconfiguration

<!-- -->

-   Lifeline wireless support (get online at limited bandwidth with just
    a pre-configured radio, no monthly cost)

<!-- -->

-   VOIP support

<!-- -->

-   Proxy support

Prototype deployment network map
--------------------------------

I climbed a LOT of mountains to determine beam paths. See google earth
map [here](http://www.teklibre.com/~d/b4barrios10.kml) and zoom in below
San Juan Del Sur, Nicaragua. At one point I had a contract to spread
wireless internet across the entire Rivas department.

This partially deployed network was taken down in May, 2010, due to the
arrival of the Survivor TV show.
