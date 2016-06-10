
---
title: Debugging CeroWrt
date: 2014-05-29T13:49:51
lastmod: 2014-05-29T13:49:51
---
Debugging CeroWrt
=================

If you wish to help us debug CeroWrt, we recommend that you use the
*cerostats.sh* script to collect configuration and diagnostic
information from the router. This script is part of the
[CeroWrtScripts bundle.]({{< relref "wiki/CeroWrtScripts.md" >}})

The easiest way to use the script is to clone the
[bundle]({{< relref "wiki/CeroWrtScripts.md" >}}) onto the router ahead of time, so you
can run the script when trouble arises.
The [CeroWrtScripts page]({{< relref "wiki/CeroWrtScripts.md" >}}) describes how to
clone those files into your router. When it's there, you can enter these
commands:

    $ ssh root@gw.home.lan        # or whatever you need to do to ssh to CeroWrt
    # cd /usr/lib/CeroWrtScripts  # this is the recommended directory for the scripts
    # sh cerostats.sh
    Done... Stats written to /tmp/cerostats_output.txt (cerostats.sh)
    #

The *cerostats.sh* script writes its output to
`/tmp/cerostats_output.txt` which you can copy/paste into your trouble
report.
