
---
title: Monitoring CeroWrt
date: 2012-01-31T19:20:25
lastmod: 2013-03-16T11:25:07
---
Monitoring CeroWrt with SNMP and NetFlow
========================================

There are optional packages that allow you to install SNMP and NetFlow
agents on CeroWrt.

The <link>Automated Configuration of CeroWrt</link> page provides a
script that (optionally) performs both these actions as well as allowing
you to configure other aspects of your router in a single step. For
reference, the GUI process for enabling SNMP and NetFlow procedures are
documented here.

Installing and configuring SNMP on CeroWrt
------------------------------------------

The Simple Network Management Protocol (SNMP) is a protocol that allows
network management stations to retrieve operational statistics from
CeroWrt. The snmpd package implements MIB-II for traffic statistics and
system information; IF-MIB for detailed information about high-speed
interfaces; the UCD-SNMP and Host Resources MIBs for processor, disk,
and memory utilizations. To install and configure SNMP:

1.  Click the "S" tab on the *Available Packages* page. Find the
    "snmpd" entry.
2.  Click the **Install** link for the snmpd entry to install the
    SNMP daemon.
3.  Log in via ssh to complete these steps, or use the shell script
    below:
4.  To enable snmpd, type: `/etc/init.d/snmpd start`
5.  To force snmpd to start when the box reboots, type:
    `/etc/init.d/snmpd enable`
6.  This default install enables SNMPv1 and SNMPv2c with a default
    read-only community string of 'public'.
7.  The /etc/snmpd/snmpd.conf file can be configured to change these
    parameters according to directions elsewhere on the web.

NB: the snmp data apparently only gets updated every 15-30 seconds.
Consequently, it gives inaccurate results if it is probed more
frequently. (This is especially obvious if you look at traffic counters.
Two queries a few seconds apart retrieve the same value, thus the
computed data rate appears to be zero. This is a known flaw in the
OpenWrt package as well.)

Installing fprobe and configuring CeroWrt to be a NetFlow exporter
------------------------------------------------------------------

[NetFlow](http://www.cisco.com/en/US/prod/collateral/iosswrel/ps6537/ps6555/ps6601/prod_presentation0900aecd80311f57.pdf)
is a Cisco protocol that permits a router or switch to send (*export*) a
summary of recent traffic to a database (a *NetFlow collector*) for
analysis. The NetFlow data allows a network manager to see who's sending
or receiving traffic, what port(s) are being used, and make other
judgements about network traffic.

fprobe is a CeroWrt package that makes the router act as a NetFlow
exporter. To install and configure fprobe to send data to your
designated collector address on port 2055:

1.  Click the "F" tab on the *Available Packages* page. Find the
    "fprobe" entry.
2.  Click the **Install** link for the fprobe entry.
3.  To start fprobe at boot time, click the System tab, and the
    Startup sub-tab.
4.  Use the shell script below, or follow the rest of these steps:
5.  Scroll to the **Local Startup** at the bottom of the page and add
    the following above the "exit 0" line:\
    `fprobe -i ge00 -f ip -d 15 -e 60 localhost:2055`\
    This monitors traffic on interface ge00, filtering (reporting on)
    IP traffic. The inactive flow timeout is 15 seconds, the active flow
    timeout is 60 seconds, and flow records will be sent to *localhost*
    on port 2055. (You should change 'localhost' to the actual IP
    address of your collector.)
6.  (Optional) Log into the router via ssh, and enter the same command,
    restart the router to begin NetFlow Export, or use the shell script
    below

For more information, read the document:"fprobe man page"

A script for automating snmpd and fprobe configuration
------------------------------------------------------

The following shell script automates the installation and configuration
of snmpd and fprobe. The comments at the top show how to ssh into the
router, paste the script into a file in /tmp, then run that file. Note
that you should change *192.168.1.1* in **both** fprobe commands to the
address of your own NetFlow collector.

The script has been moved to the <link>Automated Configuration of
CeroWrt</link> page.
