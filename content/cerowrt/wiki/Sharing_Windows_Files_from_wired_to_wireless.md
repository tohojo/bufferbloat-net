---
title: Sharing Windows Files from wired to wireless
date: 2011-11-30T23:36:17
lastmod: 2013-06-18T02:37:21
type: wiki
---
Sharing Windows Files from wired to wireless
============================================

By default Cerowrt routes between network interfaces rather than bridge
them. This improves performance markedly however it is an uncommon
concept, and introduces problems with protocols and applications that
expect everything to be on the same 'wire'.

Windows filesharing by default, expects everything to be on the same
wire. However, for larger deployments, it has always had the ability to
share files and printers across different wires, it has merely fallen
into disuse and is not enabled by default. Further, cerowrt doesn't
include windows support by default at this time, but it can be installed
via an optional package.

Instructions
------------

1\) On each PC, enable NetBIOS over TCP/IP. I found this disabled on both
Windows XP and Windows 7 machines. Go to the properties for your network
adapter, select Internet Protocol Version 4 then click on the Properties
button. When the Properties window comes up, click on the Advanced...
button in the lower-right hand corner. When the Advanced Settings window
comes up, make sure that "Enable NetBIOS over TCP/IP" is selected.
LMHOSTS lookup can be on or off.

2\) Install the samba36-server package on the router to enable WINS
support, via:

       opkg update
       opkg install luci-app-samba

       (or install via the web interface)

3\) By default, /etc/config/samba will look like:

       config samba
           option 'name'                   'openwrt'
           option 'workgroup'              'openwrt'
           option 'description'            'openwrt'
           option 'homes'                  '1'

       config sambashare
           option 'name'                   'tmp'
           option 'path'                   '/tmp'
           option 'read_only'              'no'
           option 'guest_ok'               'no'
           option 'create_mask'            '0700'
           option 'dir_mask'               '0700'
           #option 'users'                 'abc'

Change the 'workgroup' option above to match your Windows workgroup
name, or re-configure the workgroup of all the Windows\
computers to be OPENWRT (matches default 'workgroup' above)

You MAY need to supply more options, we're working on it.

5\) Modify "/etc/samba/smb.conf.template" and add this line to the\
\[global\] section:

       # Next line needed for Windows 7
       reset on zero vc = no

       wins support = yes

6\) Start samba via:

       /etc/init.d/samba start

And there may be more things required to make samba be correct.

7)

On Windows XP and later, the built-in firewall will filter incoming
NetBIOS over TCP traffic from remote subnets. This is only an issue on
machines that are actually sharing files.

\* On Windows XP, go to Control Panel, open Windows Firewall and switch
to the Exceptions tab. Select the "File and Printer Sharing" entry and
click "Edit Scope". You will need to enter a custom scope of
"172.30.42.0/24".

\* On Windows 7, running the following as Administrator should work:

    netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes remoteip=172.30.42.0/24

    rem Next lines are based on http://www.sevenforums.com/system-security/257798-windows-7-ipsec-vpn-client-firewall-configuration.html#post2136247
    netsh advfirewall firewall set rule name="File and Printer Sharing (NB-Session-In)" new remoteip=172.30.42.0/24,LocalSubnet
    netsh advfirewall firewall set rule name="File and Printer Sharing (NB-Name-In)" new remoteip=172.30.42.0/24,LocalSubnet
    netsh advfirewall firewall set rule name="File and Printer Sharing (NB-Datagram-In)" new remoteip=172.30.42.0/24,LocalSubnet
    netsh advfirewall firewall set rule name="File and Printer Sharing (Echo Request - ICMPv4-In)" new remoteip=172.30.42.0/24,LocalSubnet

Alternatively, go to Control Panel, then Firewall. Click on Advanced
Settings (in the left hand panel), then in the "Incoming Rules" folder,
open "File and Printer Sharing (SMB-in) (Private Profile)". In the Scope
tab, add the remote IP address "172.30.42.0/24".

8\) Open Windows Explorer, and make sure you can see the computers on the
wireless subnet from the computers on the wired subnet, and vice-versa
(this will be in the Network section in the lower-left hand corner). Try
to access the file share of a remote system using its Windows file path:

       \\WIRED (from a wireless computer)

9\) One it's all working, open the router GUI, click on the System tab in
the top row, then on the Startup tab in the second row. Make sure the
"samba" is Enabled. This is so Samba starts when the router is rebooted.
