---
title: Last day
date: 2011-07-15T08:35:47
lastmod: 2011-07-15T08:36:03
type: wiki
---
Last day
========

-   First step
    -   Test Woodrow build (email pointing to it) on the routers that
        failed to have a wireless radio on the last build
    -   Assuming that the build works (and the radios work) - log in to
        router, restart firewall and LOG errors in a bug report.
    -   Plug router in a real WAN port and see if it works

<!-- -->

-   Second step
    -   Test two wireless connections (2Ghz and 5Ghz)
    -   Enable both connections for crypto (WPA2)
    -   Laptop on 2Ghz can ping laptop on 5Ghz

<!-- -->

-   Third step
    -   Test DNS
    -   Make sure time is correct
    -   Does the webpage come up?

<!-- -->

-   Why did internal routing break?
    -   Burn 2 more routers and see if they break

<!-- -->

-   Resurrect LAB
    -   Burn 3 routers with the working code
    -   Scribble down the MAC addresses on the routers
    -   PDU - needs to have a map on the web-in:192.168.30.10
        login:admin pass:1234

