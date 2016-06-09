
---
title: Device naming scheme
date: 2011-07-09T11:10:04
lastmod: 2013-03-16T11:19:18
---
Device and Interface Naming Scheme
==================================

Instead of the conventional 'ethX' and 'wlanX' device naming scheme,
devices are named after their security model and type.

This was not done to make it easier for humans, but for more efficient
firewall rules, as we noted during testing that various firewall rules
and classifiers using the default naming scheme cut performance by as
much as 75%, and by default, about 11%. This naming scheme allows for
pattern matching ('+' syntax) on the devices, and also clearly
identifies when different radios are in use.

By breaking up the interface names into different classes, based on
function and type, we gain (theoretically, this work isn't completed)
efficiency in classification and firewalling not possible otherwise.

Also, as 2.4ghz radios, 5.x ghz radios and GigE ethernet have very
different characteristics, this system lets each be played with
individually.

Lastly, the 'guest' concept lets encrypted, unencrypted, and mesh
networks be tested individually. Etc. See also: [default network numbering]({{< relref "wiki/Default_network_numbering.md" >}}).

The device naming pattern is

{g|s|d|}{e|w}{radio}{device number}

g = guest or gateway\
s = secure\
d = dmz

e = ethernet\
w = wireless

The device and firewall mapping for the unfamiliar is:

  ---------- ---------- -------------- ---------- ------------------ -------------------------------------------
  old name   new name   old zone       new zone   IP range           Why
  eth1       ge00       wan            wan        DHCP               Default gateway
  eth0       se00       lan            lan        172.30.42.0/27     First lan interface
  wlan0      sw00       N/A(bridged)   lan        172.30.42.64/27    First 2.4 ghz wireless interface
  wlan3      sw10       N/A(bridged)   lan        172.30.42.96/27    First 5.x ghz wireless interface
  wlan1      gw00       N/A            guest      172.30.42.128/27   Second (guest) 2.4 ghz wireless interface
  wlan4      gw10       N/A            guest      172.30.42.160/27   Second (guest) 5.x ghz wireless interface
  wlan5      gw11       N/A            guest      172.30.42.192/27   Third (mesh) 5.x ghz wireless interface
  wlan2      gw01       N/A            guest      172.30.42.192/27   Third (mesh) 2.4 ghz wireless interface
  ---------- ---------- -------------- ---------- ------------------ -------------------------------------------

Vlans, although they work, are not currently mapped into this naming
scheme.

### See also:

[Default network numbering]({{< relref "wiki/Default_network_numbering.md" >}})\
[Changing your cerowrt ip addresses]({{< relref "wiki/Changing_your_cerowrt_ip_addresses.md" >}})\
[Automated Configuration of CeroWrt]({{< relref "wiki/Automated_Configuration_of_CeroWrt.md" >}})
