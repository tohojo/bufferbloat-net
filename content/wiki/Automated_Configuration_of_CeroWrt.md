
---
title: Automated Configuration of CeroWrt
date: 2013-03-16T11:08:06
lastmod: 2014-05-29T13:06:27
---
Automated Configuration of CeroWrt
==================================

CeroWrt uses the LuCi GUI (from OpenWrt) to make it easy to tweak most
every part of the CeroWrt configuration.

However, when testing the software, it's convenient to have a script
that will issue the same set of configuration commands so that a fresh
firmware installation can be brought to a consistent state in a single
step. The following script will configure a number of interesting
aspects of CeroWrt, including:

-   Set up the ge00/WAN interface to connect to your provider
-   Update the software packages
-   Update the root password
-   Set the time zone
-   Enable SNMP for traffic monitoring and measurements
-   Enable NetFlow export for traffic analysis
-   Enable mDNS/ZeroConf on the ge00 (WAN) interface
-   Change default IP addresses and subnets for interfaces
-   Change default DNS names
-   Set the SQM (Smart Queue Management) parameters
-   Set the radio channels
-   Set wireless SSID names
-   Set the wireless security credentials

The script has a set of lines for each task. They're all optional,
because they're all commented out. If you wish to perform one of these,
fill in any of the values, then uncomment the affected lines.

How can I get this script?
--------------------------

The *config-cerowrt.sh* script is now part of the
[CeroWrtScripts]({{< relref "wiki/CeroWrtScripts.md" >}}) A direct link to the
script is:
https://github.com/richb-hanover/CeroWrtScripts/blob/master/config-cerowrt.sh
But it's easier to use the script if you `git clone` it to your router
as described on the [CeroWrtScripts]({{< relref "wiki/CeroWrtScripts.md" >}})
