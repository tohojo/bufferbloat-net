---
title: Basic Diffserv Improvements to Linux
date: 2011-06-19T15:03:15
lastmod: 2011-06-30T12:10:17
type: wiki
---
Basic Diffserv Improvements to Linux
------------------------------------

    [!] -m dscp --dscp-classes DSCPSET -j 
    [!] -m dscp --clamp-to BE,DSCPSET -j a_trust_but_verify

Where DSCPSET is of the form AF,EF,0x4,2,CS1,etc and becomes a 64 bit
bitfield for matching purposes. Also the userspace distinction between

    --dscp-class
    --dscp

could be removed, as the codes are distinct from numeric values
regardless, and several important existing classes of traffic are
undefined by both the current implementation and RFC)

    -j CLASSIFY --set-priority-by-dscp offset
    -j MARK --set-mark-by-dscp offset

This extends the existing FWMARK and classifier targets to be more
orthogonal.

### Protocols Match

It would be nice to also perform this kind of matching against a
protocol set. The world is bigger than just udp and tcp, and with all
the interesting protocols in the Linux kernel it would be good to easily
be allow a few more of them out and in. As protocol is a 8 bit field,
this leads to a 256 bitfield, which would be matched against in the 64
bit CPU case, probably close to 99.999999% of the time, at present.

### PROBLEMS

#### IPtables vs IPset

in both of these cases, these problems and solutions fall between the
flexibility of iptables (one protocol/dscp value or not one
protocol/dscp value), and ipset, which can scale to 64k entries of
various sorts. The first leads to very long chains for extensive
protocol/dscp matching, the other is not part of ipset at present, and
overkill.

Matching against sets in the range of 64 - 256 bits is best handled via
brute force.

#### Usage of filter vs mangle tables

Logically, you want to clamp incoming DSCP bits to just those your site
recognizes as soon as possible, e.g. on the INPUT chain, or in TC,
before it hits the mangle table.

I am under the impression that mangling exists due to the effect on
checksumming that playing with packets can induce, however, the DSCP/ECN
fields are not included in checksums...

That said, being orthogonal between tc and iptables for classification
of these sorts would be useful and would perhaps be able to share code.

#### Modifying packets in match rule

See above. The usefulness here is in --clamp-to you can jump to a target
based on the fact you clamped something, to further reclassify it.

#### Possible 64 bit enhancements

Doing matches of this 64 bit match value can be made more efficient on
64 bit arches by simply using an existing (void \*) in the skb as data.

The degree to which you cringe is dependent on how much you like
kallocating and de-kallocating a 64 bit value and then dereferencing the
resulting pointer in a high performance chain.

I don't see a clean solution at present for 32 bit arches besides
allocating the value and treating it as a pointer, and for that matter
may be misunderstanding something regarding the usage of this void
value.
