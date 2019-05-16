---
title: Windows Tips
date: 2011-02-02T11:14:57
lastmod: 2014-05-05T12:35:15
type: wiki
---
Windows Tips
============

Enable Compound TCP
-------------------

Compound TCP is a Hybrid TCP Congestion Control approach. You can also
enable ECN (lossless congestion control feedback):

If enough end users enable ECN, core providers may be inclined to deploy
<link>AQM with Packet Marking</link> too... And as <link>Home
Gateways</link> are those which are prone to ECN implementation bugs, a
full disconnect from the internet (rather than certain sites not
reachable) is quite easy to quickly diagnose.

Also, enabling ECN gives you more retries with the SYN (3x ECN+SYN, 3x
normal SYN), so in a heavy congested / bufferbloated environment, your
small flows might get through eventually, with higher probability.

### Windows Vista / Windows 7 users can enable "Compound TCP",

```
netsh int tcp set global congestionprovider=ctcp
netsh int tcp set global ecncapability=enabled
```

### Windows 8

The use of `netsh int tcp set global congestionprovider=ctcp` has been
depreciated. In order to set or change the congestionprovider the
following command must be used:

```
set-nettcpsetting -CongestionProvider CTCP
```

However, CTCP is the default on windows 8 and later. Changing the setting does
not seem to work on Windows 10.

Type `get-nettcpsetting` to view other settings that used to be part of
netsh tcp global.

ECN is a global setting and is still configurable, even on clients,
through netsh by running:

```
netsh int tcp set global ecn=enable
```

On Windows Server 2012, you can change this setting through the custom
template or netsh.
