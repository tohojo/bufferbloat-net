
---
title: Pure_IPv6_based_networking
date: 2012-03-07T12:12:43
lastmod: 2012-03-08T09:24:04
---
Pure IPv6 based networking
==========================

This is as yet, a draft.

IPv6 has been 'the future' for over a decade now. Making it work right,
in time for the 'World IPv6 launch', June 6, 2012, is one of the many
goals of cerowrt.

This is how to setup a pure ipv6 based network behind the router itself.
While useful as an academic exercise, it is also useful in exposing
what, exactly, needs to be done in order to have a working ipv6 based
network.

Get IPv6 working
----------------

There are multiple ways to get ipv6 working. The best, of course, is
native ipv6, which is coming available from multiple providers, notably
comcast. You can also tunnel (6in4), or use 6to4. As cerowrt has 6
default interfaces it is best to get at least a /60, preferably a /56 or
better, ipv6 network to play with.

Present versions of cerowrt try really hard to come up automatically in
6to4 mode. This functionality will be disabled by default\
in the near future.

For purposes of this discussion I'm merely going to document how
<link>bloatlab 1</link> is configured. The bloatlab has a /60 ipv6
delegation from isc.org, thus leading to the possibility of 16 distinct
ipv6 networks. There is also a 'main' network on which an array of
routers and test equipment are configured.

The internal address range we're using is: 2001:4f8:3:aa00::/60. Any
time you see addresses in this range in this document, please substitute
your own.

Configure cerowrt on the right ipv6 addresses
---------------------------------------------

This is in the case of a native ipv6 enabled network. For 6to4 or 6in4
instructions, there will be some more notes soon.

    config interface 'ge00'
            option ifname 'ge00'
            option proto 'dhcp'
            option accept_ra '1'
            option send_rs '1'

    config interface 'se00'
            option ifname 'se00'
            option proto 'static'
            option ipaddr '172.29.6.1'
            option netmask '255.255.255.224'
            option ip6addr '2001:4f8:3:aa0c::1/64'

The first stanza for 'ge00' accepts whatever ipv6 address is assigned by
the 'RA' protocol and may not be what you need - dhcp-pd is being worked
on at present. I note that your should be setting 'ipaddr' to whatever
you want to have for your network, not the above.

Add the ip6addr option to each additional interface, incrementing the
4th field appropriately. Note that the /64 is not actually required...
In the case of the two meshed interfaces (gw01, gw11), the correct
approach is to use the same, single /128 for both (e.g.
2001:4f8:3:aa0e::1/128).

It's simplest just to reboot at this point. Radvd will automatically
pick up the ipv6 addresses, and hopefully the default gw will be
supplied by the upstream ipv6 router....

### Check to see if you have ipv6 addresses on clients after the reboot

And, do you have a default gw?

If so, awesome. Things like ping6 huchra.bufferbloat.net should 'just
work'. If they don't, a horde of other problems could be happening and
are currently beyond the scope of this document.

Cope with security issues
-------------------------

### Get DNS to work right

The integral bind9 server in cerowrt is fully capable of doing DNS over
ipv6. However it makes a difference between 'internal' and 'external'
views of its database that need to be managed via access control lists
(acl)s. Edit /etc/chroot/named/etc/bind/conf/acls.local.conf to have a
line in it that matches the address ranges you are using

acl mylan {\
192.168/16;\
172.16/12;\
2001:4f8:3:aa00::/60;\
// 2002:XXXX:YYYY::/48; if you are using a 6to4 address\
};

IF you have a local forwarder that is ipv6 and dnssec enabled, you can
edit the forwarders.conf file in this directory to suit, and uncomment
the forwarder line in named.conf.

then restart bind

    killall bind; 
    nslookup ::1
    nslookup ipv6.google.com

You can go much further with this than this, notably doing reverse dns,
etc, but not today. It is certainly my hope to get to where ipv6 is as
transparent to use as ipv4 at some point. I note that most of google's
services when bind9 is operating over ipv6, automatically come up on
ipv6, so there is generally no need to use 'ipv6.google.com' when things
are working properly.

### Enable the polipo web proxy

Web proxies have been a standard component of the http protocol since
the early days, and despite falling into disuse of late, are the
simplest way to retain universal to-the-web access, by using the proxy
to translate between ipv6 internally to ipv4 or ipv6 based websites
externally. However polipo needs to be reconfigured slightly to accept
connections within your network over ipv6. Add the following two lines
(Again, substituting your own ipv6 address range) to /etc/config/polipo

            option 'dnsNameServer' '::1'
            list 'allowedClients' '2001:4f8:3:aa00::/60'

It is also useful to use polipo as a caching web proxy, by putting a
flash drive into the cerowrt box and enabling the cache option, but for
now

    /etc/init.d/polipo restart

### Enable the web proxy on the clients

there are a few ways to do this, the most straightforward is merely to
put the ipv6 address of the polipo proxy in your 'network
connections-&gt;proxies' entry for your web browser. A more 'right' way
might be to use the 'wpad' auto proxy configuration facility,\
which would be able to supply the right configuration information
automatically...

At this point you should be able to surf the web with only minor
breakage. In my own tests the only thing that broke was the macromedia
protocol used in some TED talks. That is not to say this is perfect....

### Enable ipv6 nameservice lookup on clients

Easiest way is to just stick the appropriate

nameserver 2001:4f8:3:aa0c::1

in /etc/resolv.conf. In an ideal world, a service such as rdnssd or
dibbler-client, will do this bit of grunt work for you.

### I use git and have to proxy it through polipo

While a few git services already have ipv6 support, github (my main one)
does not, so I do this:

https://gist.github.com/49288\#file\_gitproxy\_socat

### Samba

Samba 'just works' on ipv6. However there are some firewall rules that
will affect getting from the 'guest' networks to the 'secure' networks
contained in /etc/firewall.user that should probably be examined.

### Try to use ipv6 enabled services.

For example, ipv6.google.com, and irc chat services such as freenode,
are already on ipv6. My primary email servers are also on ipv6, as well
as my jabber server. Admittedly, that's me. It is not terribly hard to
get this stuff running on various servers, but I'll leave that for
another document.

Turn off ipv4 entirely
----------------------

So you have all the above working and want to go beyond the bleeding
edge?

Turn off ipv4 entirely on a client and see what happens. On Linux, it's
straightforward:

    ip -4 addr show dev whatever
    # take that address
    ip -4 addr del dev whatever that_address

And at least until your dhcp refreshes, you will be purely ipv6 and can
experience all the pleasures (if any exist) and pain (plenty) that ipv6
can bring to your network.

Known Problems
--------------

### DNSSL

Having a dns search list was a late addition to the RA protocol and is
still not widely adopted. This (as one example), makes implementing wpad
support difficult. A test patch is in progress on the router itself, but
as for clients...

### Security with polipo

The polipo web proxy is a single tier proxy, in that it has no means of
discriminating between 'allowed' and 'restricted' networks. By making it
available across the entire allocated ipv6 range as done above, the
concept of local secure internal and guest networks has been bypassed,
anyone that can connect to the proxy can access various web-like
services on both 'guest and secure'. This is probably not what you want,
but at least the above restriction keeps people from outside your lans,
out. Without finer grained access controls in polipo such as what squid
has, I don't know how to fix this....

### Security with ip6tables

The ip6tables rules have not been fully evaluated as to their
effectiveness and thoroughness.
