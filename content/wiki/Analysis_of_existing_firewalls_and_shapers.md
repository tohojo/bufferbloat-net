
---
title: Analysis of existing firewalls and shapers
date: 2011-06-20T05:28:52
lastmod: 2011-06-20T05:28:52
---
Analysis of existing firewall and shaper scripts
------------------------------------------------

TBD: I have examples of many of these types of shapers that I plan to go
into more detail with shortly.

### Openwrt firewall + QoS rules

Openwrt ties it's firewalling and QoS code closely together, using a
combination of 'qos-scripts' and firewall rules in a somewhat easy to
read format in /etc/config/qos and /etc/config/firewall, generating
complex rules as a result. It also defaults to TCP Westwood+ which has
interesting interactions with other TCP traffic when a proxy is used.

### Gargoyle

Gargoyle (A fork of openwrt)

### ufw

### Wondershaper

Wondershaper's big claim to fame was it's simplicity. It pioneered
[ACK prioritization]({{< relref "wiki/ACK_prioritization.md" >}}) for ssh traffic, and did its work in
only 4 TC rules.

### Nanog

### Airmax

Used by ubiquity in their line of high performance wireless routers,
this consists of a lot of very hard to parse tc rules that work magic
for fairness across a wireless network

### Adsl-Shaper

### Shorewall

### Linux voip server example

### Linux servers

### Linux desktops
