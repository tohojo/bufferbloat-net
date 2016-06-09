
---
title: Wired oprofile with alignment trap
date: 2011-06-04T05:43:18
lastmod: 2011-06-04T05:43:18
---
Wired oprofile with alignment trap
==================================

In doing testing of the wired driver, we are seeing unaligned
instruction traps.\
Losing 20% of cpu to an unaligned instruction is bad.

Regrettably, you can't see where they are being caused via oprofile...

Counted INSTRUCTIONS events (Instructions completed) with a unit mask of
0x00 (No unit mask) count 100000\
samples cum. samples % cum. % app name symbol name\
-------------------------------------------------------------------------------\
2793 2793 15.9300 15.9300 vmlinux do\_ade\
2793 2793 100.000 100.000 vmlinux do\_ade \[self\]\
-------------------------------------------------------------------------------\
1750 4543 9.9812 25.9111 vmlinux csum\_partial\_copy\_nocheck\
1750 1750 100.000 100.000 vmlinux csum\_partial\_copy\_nocheck \[self\]\
-------------------------------------------------------------------------------\
1617 6160 9.2226 35.1337 ip\_tables /ip\_tables\
1617 1617 100.000 100.000 ip\_tables /ip\_tables \[self\]\
-------------------------------------------------------------------------------\
1594 7754 9.0914 44.2252 nf\_conntrack /nf\_conntrack\
1594 1594 100.000 100.000 nf\_conntrack /nf\_conntrack \[self\]\
-------------------------------------------------------------------------------\
606 8360 3.4563 47.6815 vmlinux tcp\_v4\_rcv\
606 606 100.000 100.000 vmlinux tcp\_v4\_rcv \[self\]\
-------------------------------------------------------------------------------\
565 8925 3.2225 50.9040 vmlinux csum\_partial\
565 565 100.000 100.000 vmlinux csum\_partial \[self\]\
-------------------------------------------------------------------------------\
544 9469 3.1027 54.0067 vmlinux handle\_adel\_int\
544 544 100.000 100.000 vmlinux handle\_adel\_int \[self\]\
-------------------------------------------------------------------------------\
435 9904 2.4810 56.4878 vmlinux ip\_rcv\
435 435 100.000 100.000 vmlinux ip\_rcv \[self\]\
-------------------------------------------------------------------------------\
433 10337 2.4696 58.9574 vmlinux \_\_copy\_user\
433 433 100.000 100.000 vmlinux \_\_copy\_user \[self\]\
-------------------------------------------------------------------------------
