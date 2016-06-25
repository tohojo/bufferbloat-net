---
title: Wlan script
date: 2011-04-20T15:53:17
lastmod: 2011-04-20T15:53:17
type: wiki
---
Wlan script for Debian style /etc/network/if-up.d directory
===========================================================

    #!/bin/sh

    IFTOOL=/sbin/ifconfig
    TXQUEUELEN=32

    test -x $IFTOOL || exit 0

    # Don't bother to reload when lo is configured.
    if [ "$IFACE" != "wlan0" ]; then
        exit 0
    fi

    # Only run from ifup.
    if [ "$MODE" != start ]; then
        exit 0
    fi

    SETTINGS="txqueuelen $TXQUEUELEN"

    [ -z "$SETTINGS" ] || $IFTOOL "$IFACE" $SETTINGS

    exit 0
