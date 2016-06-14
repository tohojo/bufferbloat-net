
---
title: Release Strategy
date: 2012-02-13T14:40:14
lastmod: 2012-02-13T17:34:02
type: wiki
---
Release Strategy
================

Cerowrt has followed multiple release strategies and naming schemes
since its inception, and even the primary author finds it all rather
confusing. This page is about the current release strategy. As for how
to access older builds, please see the <link>Pre-3.3 Releases</link>
page.

Goals going forward for the source trees and binaries:

-   Have a clear development/release split
-   Be easily build-able by those with little or no openwrt experience
-   Produce reproducible results
-   Make possible other architecture support
-   Make possible to do at least some (particularly security) in-field
    updates
-   Make more possible to feed changes upstream
-   Make doing R&D faster and more productive

Naming scheme (binaries)
------------------------

Future releases will be named after the kernel they are based on. Using
'codenames' like [OCEAN CITY](OCEAN_CITY.md) or <link>Paris</link> will be
dropped.

One of the core goals of cerowrt is to track the main kernel trees as
closely as possible. This simplifies maintenance and essential R&D by
making it easy to develop code on mainstream architectures
(x86,x86\_64)\
and bring the patches 'right' over to embedded - and vice versa. It also
makes reproducing and fixing bugs much simpler. The kernel is on roughly
a 3 month development cycle.

So what we will see are versions that look like

cerowrt-3.3-rc3-X - where 'X' is the build number, and is otherwise
meaningless. The 3.3-rc3 part mirrors the existing kernel naming scheme,
and thus a 'final' cerowrt release will probably look like:

cerowrt-3.3.1-X. We will not track the 'stable' releases of the kernel
too closely unless there is stuff that is explicitly broken that needs
to be fixed.

There will be 'topic' branches, much like the existing 'bql' branch,
where some particular problem is being fixed or explored. Rather than
confuse people, 'topic' branches will go under some other subdirectory.

The biggest problem this scheme induces is that it is in conflict with
openwrt's release schedule.

Field updates
-------------

There's no real plan to do field updates aside from migrating towards
something that might work, more often,\
at this time.

Naming scheme (repositories)
----------------------------

Because integrating with upstream openwrt has been problematic,
requiring frequent rebasing, a given series (3.3 in this example) will
end up in its own repositories when its development cycle formally
starts. No rebasing will be performed during the formal development
cycle. Conflicting commits will be reverted, or merged, instead.
(maybe). Commits will be exclusively pulled from the existing git
mirrors such as nbd's, pushed into the current development tree, and
patches made available after testing on both the mailing list and in a
'topic' branch that people can pull from.

This is modeled on the present-day kernel development process where the
middle-tier maintainer asks\
the primary maintainer to just pull from a topic branch. It would be my
preference from a patch mangling\
standpoint for 'pulls' from a topic branch rather than commits from the
mailing list happen, but we'll see.

The git repos will try to enforce openwrt's commit policies as well. (I
don't know what they are and need to find out)

At the start of a new development cycle, cerowrt will be rebased on
openwrt head, the patch sets that didn't make it upstream will be folded
in, with the merges and conflicting commits stripped out, and we'll
start again.

We will do continuous integration over that cycle up until something
major changes (like a toolchain change),\
then freeze, continuing continuous integration in a topic branch until
or if it proves out.

I would prefer to keep stuff in git branches rather than explicitly
named repos (cerowrt-3.3, ceropackages-3.2), etc, if it weren't for the
rebasing problem and inexperienced git users.

At the moment I plan on explicitly named repos.

Upstream work
-------------

The fastest and best way to get patches into openwrt has been to work
upstream beyond it.

So periodically core utilities or applications that need an update or
surgery will be forked off into the ceropackages repo, worked on,
tested, and patches submitted upstream to the application developer. The
out of tree package will be maintained out of tree until the new version
makes it back to openwrt.

It has generally been too painful to bother submitting updates to core
utilities to openwrt's own upstream,\
except for trivial stuff, but we should at least, try harder. A good way
to approach this may be to have\
explicit 'patch review' days on the openwrt patchwork tree. (and to make
sure our tested patches are upstream\
at that point). It would be a goodness to get more stuff in general out
of patchwork and into openwrt that isn't 'ours' as a way of contributing
back to the community.

However several core utilities (iproute2, iptables) are very kernel
dependent and need to fork off in order\
to more closely track their 'head' versions. Perhaps a separate
'openwrt-next' tree, similar to the 'net-next'\
tree could serve as a staging area for those and for patchwork.

The existing ceropackages 'application-latest' convention will be
dropped, and the openwrt feeds 'preference' option adopted, instead.
This minimizes the delta between the next generation of the package and
the old package.

Web site
--------

A virtual host will be established somewhere to shorten the urls.

Roadmaps
--------

The existing roadmap and bug lists consist of many man-years worth of
work, which is unfunded and un-resourced. Much of that work continues to
happen organically, and having the bug lists so public helps to focus
our huge herd of cats. Coming up with a better way to track the openwrt
buglist would be useful too.

And: coming up with a way to get the herd of cats funded and fed on a
regular basis would best.

The existing roadmaps will be cut down to goals that are achievable on a
3 month cycle on the resources we have, so we can at least give people
(especially ourselves!) a clue as to what we plan to do.

We will take advantage of opportunities that come up, of course.

In terms of picking a release date, somewhere around the projected
arrival of a linux-X.Y.1 seems best.

In terms of picking a 'start of new development date', sometime after
patches arrive for a new kernel that prove out (in a topic branch), is
the trigger point.

Finding a way to reduce the delta between openwrt's kernel patch set and
the device's specific patch set\
should become a higher priority than it has been, in order to further
speed up the cycle.

Core feature set
----------------

When development came to a standstill back in November, our core feature
set was the most advanced set of ideas in the industry, in building a
ipv6 capable box that actually worked the way a geek would want things
to work.

While that entire feature set now 'works' it's still a little 'too
geeky', and we have some new requirements in the coming year.

-   Tons of Gui work
-   IPv6 support
-   DHCP-PD support

The core feature set is sufficiently different from openwrt as to cause
problems with integration,guis, etc, etc.

Also it would be good to be testing more openwrt-like configurations in
the general case.

The core feature set needs to be nailed down for each release and stay
nailed down.

Long term support
-----------------

There still is no plan for long term support! The goal is to do R&D and
get new stuff working and pushed upstream!
