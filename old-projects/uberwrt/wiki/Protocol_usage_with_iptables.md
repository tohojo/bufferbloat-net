
---
title: Protocol usage with iptables
date: 2011-05-28T08:21:02
lastmod: 2011-05-28T08:21:02
type: wiki
---
Protocol usage with iptables
============================

Idea stolen from:
https://forum.openwrt.org/viewtopic.php?pid=20345\#p20345

Regrettably this does not work well with the firewalling solution
already in place.

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto bittorrent -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto bittorrent -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto ftp -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto ftp -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto ssh -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto ssh -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto pop3 -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto pop3 -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto smtp -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto smtp -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto imap -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto imap -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto directconnect -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto directconnect -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto http -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto http -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto rdp -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto rdp -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto smb -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto smb -j MARK --set-mark 3

    iptables -t mangle -A POSTROUTING -o vlan1 -m layer7 --l7proto ventrilo -j MARK --set-mark 3
    iptables -t mangle -A PREROUTING -i vlan1 -m layer7 --l7proto ventrilo -j MARK --set-mark 3

    #All unmarked
    iptables -t mangle -A POSTROUTING -o $WAN -m mark --mark 0 -j MARK --set-mark 100
    iptables -t mangle -A PREROUTING -i $WAN -m mark --mark 0 -j MARK --set-mark 101

