
---
title: Disaster planning
date: 2011-03-19T10:24:12
lastmod: 2011-03-19T10:27:06
type: wiki
---
Disaster planning
=================

Having all the core servers located in California is double-plus-ungood,
given the prospect of earthquakes.

This project is international in scope and should be international in
presence. We should be replicating essential services across
international boundaries.

While we've discussed hosting servers in Amsterdam with ISC and at MIT
and Georgia tech, we have not made commitments. There have also been
offers of virtual servers in the Central US, Canada, France, and
elsewhere.

Given the latency issues between Europe and the West coast, having
another data center located on the east coast, rather than the west
coast, would be ideal. However, thus far, only a few places on the East
coast have native IPv6 support and none have offered to donate bandwidth
or rackspace. (GA tech has come closest and has a good relationship with
ISC as well)

<link>Backups</link>
--------------------

Backups are currently limited to manual intervention, partially because
it's hard to get a consistent backup without lvm snapshot support of
database backends, and the original batch of servers were not configured
for it.

In case of server loss...
-------------------------

We need to move towards more virtualized servers in general. But having
spare hard disks and servers we can bring online in the event of
disaster would be good.

The problem with virtualization and things like EC2 is that in multiple
cases we do need to be running services that have access to the bare
hardware, and committing to a given virtualization service has a lot of
vendor lockin. At present we are evaluating kvm, which will drive the
choice of a virtualization service.

In case of earthquake
---------------------

We need to be able to re-host the services
