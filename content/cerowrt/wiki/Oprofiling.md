
---
title: Oprofiling
date: 2012-04-06T21:58:13
lastmod: 2012-04-17T17:26:31
type: wiki
---
Oprofiling Cerowrt
==================

When digging into core OS problems, running oprofile can be revealing.

(for example see bugs \#195 \#216 and \#352 - 195 and 352 are/were
serious problems)

As you have limited amount of flash and ram, you can't run oprofile for
very long unless you have external disk, but it's\
generally ok to run it for brief periods out of ram. Here's how:

    # you only have to do this once to put the needed packages on flash.
    opkg update
    opkg install oprofile

    # you will need to do this on every boot/oprofile cycle
    cd /tmp
    mkdir session
    wget http://huchra.bufferbloat.net/~cero1/3.3/3.3.1-4/vmlinux

    # note that this last line just happens to be where this kernel is for this version.
    # you can find it in your_cerowrt_dir/build_dir/linux-ar71xx_generic/linux-the.kernel.version/vmlinux

    opcontrol --setup --vmlinux=/tmp/vmlinux --session-dir=/tmp/session

    # Then you can cycle here repeatedly until you run out of ram
    # setup a test (in my case I setup a netperf to run over wireless)
    opcontrol --start
    # run the test
    opcontrol --stop
    opcontrol --dump
    opreport -c --session-dir=/tmp/session | less

(this is a healthy looking oprofile)

    CPU: MIPS 24K, speed 676 MHz (estimated)
    Counted INSTRUCTIONS events (1-0 Instructions completed) with a unit mask of 0x00 (No unit mask) count 100000
    samples  %        app name                 symbol name
    -------------------------------------------------------------------------------
    611       8.4451  mac80211                 /mac80211
      611      100.000  mac80211                 /mac80211 [self]
    -------------------------------------------------------------------------------
    453       6.2612  ath9k                    /ath9k
      453      100.000  ath9k                    /ath9k [self]
    -------------------------------------------------------------------------------
    408       5.6393  vmlinux                  csum_partial
      408      100.000  vmlinux                  csum_partial [self]
    -------------------------------------------------------------------------------
    396       5.4734  vmlinux                  __copy_user
      396      100.000  vmlinux                  __copy_user [self]
    -------------------------------------------------------------------------------
    352       4.8652  ip_tables                /ip_tables
      352      100.000  ip_tables                /ip_tables [self]
    -------------------------------------------------------------------------------
    320       4.4229  vmlinux                  lzma_main
      320      100.000  vmlinux                  lzma_main [self]
    -------------------------------------------------------------------------------
    257       3.5522  nf_conntrack             /nf_conntrack
      257      100.000  nf_conntrack             /nf_conntrack [self]
    -------------------------------------------------------------------------------
    253       3.4969  vmlinux                  __do_softirq
      253      100.000  vmlinux                  __do_softirq [self]
    -------------------------------------------------------------------------------
    237       3.2757  libuClibc-0.9.33.so      /lib/libuClibc-0.9.33.so
      237      100.000  libuClibc-0.9.33.so      /lib/libuClibc-0.9.33.so [self]
    -------------------------------------------------------------------------------
    141       1.9489  vmlinux                  __bzero
      141      100.000  vmlinux                  __bzero [self]
    -------------------------------------------------------------------------------
    125       1.7277  ath9k_hw                 /ath9k_hw
      125      100.000  ath9k_hw                 /ath9k_hw [self]
    -------------------------------------------------------------------------------
    109       1.5066  vmlinux                  finish_task_switch.constprop.62
      109      100.000  vmlinux                  finish_task_switch.constprop.62 [self]
    -------------------------------------------------------------------------------
    102       1.4098  cfg80211                 /cfg80211
      102      100.000  cfg80211                 /cfg80211 [self]
    -------------------------------------------------------------------------------
    89        1.2301  ld-uClibc-0.9.33.so      /lib/ld-uClibc-0.9.33.so
      89       100.000  ld-uClibc-0.9.33.so      /lib/ld-uClibc-0.9.33.so [self]
    -------------------------------------------------------------------------------
    89        1.2301  vmlinux                  __rmemcpy
      89       100.000  vmlinux                  __rmemcpy [self]
    -------------------------------------------------------------------------------
    89        1.2301  vmlinux                  nf_iterate
      89       100.000  vmlinux                  nf_iterate [self]
    -------------------------------------------------------------------------------
    76        1.0504  busybox                  /bin/busybox
      76       100.000  busybox                  /bin/busybox [self]
    -------------------------------------------------------------------------------
    74        1.0228  vmlinux                  tick_nohz_idle_exit
      74       100.000  vmlinux                  tick_nohz_idle_exit [self]
    -------------------------------------------------------------------------------
    72        0.9952  vmlinux                  local_bh_enable
      72       100.000  vmlinux                  local_bh_enable [self]
    -------------------------------------------------------------------------------
    67        0.9261  vmlinux                  tick_nohz_idle_enter
      67       100.000  vmlinux                  tick_nohz_idle_enter [self]
    -------------------------------------------------------------------------------
    66        0.9122  oprofiled                /usr/bin/oprofiled
      66       100.000  oprofiled                /usr/bin/oprofiled [self]
    -------------------------------------------------------------------------------
    62        0.8569  vmlinux                  __slab_alloc.isra.60.constprop.63
      62       100.000  vmlinux                  __slab_alloc.isra.60.constprop.63 [self]
    -------------------------------------------------------------------------------
    62        0.8569  vmlinux                  do_select
      62       100.000  vmlinux                  do_select [self]
    -------------------------------------------------------------------------------
    62        0.8569  vmlinux                  mix_pool_bytes_extract
      62       100.000  vmlinux                  mix_pool_bytes_extract [self]
    -------------------------------------------------------------------------------
    60        0.8293  iptable_nat              /iptable_nat
      60       100.000  iptable_nat              /iptable_nat [self]
    -------------------------------------------------------------------------------
    59        0.8155  vmlinux                  r4k_dma_cache_inv
      59       100.000  vmlinux                  r4k_dma_cache_inv [self]
    -------------------------------------------------------------------------------
    59        0.8155  wpad                     /usr/sbin/wpad
      59       100.000  wpad                     /usr/sbin/wpad [self]
    -------------------------------------------------------------------------------
    56        0.7740  nf_conntrack_ipv4        /nf_conntrack_ipv4
      56       100.000  nf_conntrack_ipv4        /nf_conntrack_ipv4 [self]
    -------------------------------------------------------------------------------
    53        0.7326  vmlinux                  __alloc_skb
      53       100.000  vmlinux                  __alloc_skb [self]
    -------------------------------------------------------------------------------
    53        0.7326  vmlinux                  lzma_len
      53       100.000  vmlinux                  lzma_len [self]
    -------------------------------------------------------------------------------
    46        0.6358  vmlinux                  fget_light
      46       100.000  vmlinux                  fget_light [self]
    -------------------------------------------------------------------------------
    45        0.6220  vmlinux                  tcp_v4_rcv
      45       100.000  vmlinux                  tcp_v4_rcv [self]
    -------------------------------------------------------------------------------
    44        0.6082  vmlinux                  __wake_up_sync_key
      44       100.000  vmlinux                  __wake_up_sync_key [self]
    -------------------------------------------------------------------------------
    42        0.5805  vmlinux                  r4k_wait
      42       100.000  vmlinux                  r4k_wait [self]
    -------------------------------------------------------------------------------
    40        0.5529  xt_conntrack             /xt_conntrack
      40       100.000  xt_conntrack             /xt_conntrack [self]
    -------------------------------------------------------------------------------
    39        0.5390  vmlinux                  datagram_poll
      39       100.000  vmlinux                  datagram_poll [self]
    -------------------------------------------------------------------------------
    38        0.5252  vmlinux                  getnstimeofday
      38       100.000  vmlinux                  getnstimeofday [self]
    -------------------------------------------------------------------------------
    38        0.5252  vmlinux                  rcu_sched_qs
      38       100.000  vmlinux                  rcu_sched_qs [self]
    -------------------------------------------------------------------------------
    38        0.5252  vmlinux                  tcp_rcv_established
      38       100.000  vmlinux                  tcp_rcv_established [self]
    -------------------------------------------------------------------------------
    36        0.4976  babeld                   /usr/sbin/babeld
      36       100.000  babeld                   /usr/sbin/babeld [self]
    -------------------------------------------------------------------------------
    36        0.4976  vmlinux                  __slab_free.isra.58
      36       100.000  vmlinux                  __slab_free.isra.58 [self]
    -------------------------------------------------------------------------------
    36        0.4976  vmlinux                  ring_buffer_consume
      36       100.000  vmlinux                  ring_buffer_consume [self]
    -------------------------------------------------------------------------------
    34        0.4699  vmlinux                  ip_rcv
      34       100.000  vmlinux                  ip_rcv [self]
    -------------------------------------------------------------------------------
    33        0.4561  iptable_mangle           /iptable_mangle
      33       100.000  iptable_mangle           /iptable_mangle [self]
    -------------------------------------------------------------------------------
    32        0.4423  vmlinux                  dict_repeat.part.4
      32       100.000  vmlinux                  dict_repeat.part.4 [self]
    -------------------------------------------------------------------------------
    32        0.4423  vmlinux                  nf_hook_slow
      32       100.000  vmlinux                  nf_hook_slow [self]
    -------------------------------------------------------------------------------
    31        0.4285  vmlinux                  kfree
      31       100.000  vmlinux                  kfree [self]
    -------------------------------------------------------------------------------
    31        0.4285  vmlinux                  kmem_cache_alloc
      31       100.000  vmlinux                  kmem_cache_alloc [self]
    -------------------------------------------------------------------------------
    30        0.4147  libnl-tiny.so            /usr/lib/libnl-tiny.so
      30       100.000  libnl-tiny.so            /usr/lib/libnl-tiny.so [self]
    -------------------------------------------------------------------------------
    29        0.4008  vmlinux                  tcp_transmit_skb
      29       100.000  vmlinux                  tcp_transmit_skb [self]
    -------------------------------------------------------------------------------
    28        0.3870  vmlinux                  kmem_cache_free
      28       100.000  vmlinux                  kmem_cache_free [self]
    -------------------------------------------------------------------------------
    27        0.3732  vmlinux                  __netif_receive_skb
      27       100.000  vmlinux                  __netif_receive_skb [self]
    -------------------------------------------------------------------------------
    26        0.3594  vmlinux                  __udelay
      26       100.000  vmlinux                  __udelay [self]
    -------------------------------------------------------------------------------
    25        0.3455  vmlinux                  ip_route_input_common
      25       100.000  vmlinux                  ip_route_input_common [self]
    -------------------------------------------------------------------------------
    25        0.3455  vmlinux                  tcp_event_data_recv
      25       100.000  vmlinux                  tcp_event_data_recv [self]
    -------------------------------------------------------------------------------
    24        0.3317  vmlinux                  sock_poll
      24       100.000  vmlinux                  sock_poll [self]
    -------------------------------------------------------------------------------
    22        0.3041  nf_nat                   /nf_nat
      22       100.000  nf_nat                   /nf_nat [self]
    -------------------------------------------------------------------------------
    22        0.3041  vmlinux                  put_cpu_partial
      22       100.000  vmlinux                  put_cpu_partial [self]
    -------------------------------------------------------------------------------
    22        0.3041  vmlinux                  skb_release_data
      22       100.000  vmlinux                  skb_release_data [self]
    -------------------------------------------------------------------------------
    21        0.2903  vmlinux                  fput
      21       100.000  vmlinux                  fput [self]
    -------------------------------------------------------------------------------
    21        0.2903  vmlinux                  link_path_walk
      21       100.000  vmlinux                  link_path_walk [self]
    -------------------------------------------------------------------------------
    20        0.2764  vmlinux                  __inet_lookup_established
      20       100.000  vmlinux                  __inet_lookup_established [self]
    -------------------------------------------------------------------------------
    20        0.2764  vmlinux                  ksize
      20       100.000  vmlinux                  ksize [self]
    -------------------------------------------------------------------------------
    20        0.2764  vmlinux                  skb_copy_datagram_iovec
      20       100.000  vmlinux                  skb_copy_datagram_iovec [self]
    -------------------------------------------------------------------------------
    20        0.2764  vmlinux                  skb_release_head_state
      20       100.000  vmlinux                  skb_release_head_state [self]
    -------------------------------------------------------------------------------
    19        0.2626  vmlinux                  __pollwait
      19       100.000  vmlinux                  __pollwait [self]
    -------------------------------------------------------------------------------
    19        0.2626  vmlinux                  netif_receive_skb
      19       100.000  vmlinux                  netif_receive_skb [self]
    -------------------------------------------------------------------------------
    19        0.2626  vmlinux                  skb_put
      19       100.000  vmlinux                  skb_put [self]
    -------------------------------------------------------------------------------
    19        0.2626  vmlinux                  tcp_recvmsg
      19       100.000  vmlinux                  tcp_recvmsg [self]
    -------------------------------------------------------------------------------
    18        0.2488  vmlinux                  __kmalloc_track_caller
      18       100.000  vmlinux                  __kmalloc_track_caller [self]
    -------------------------------------------------------------------------------
    18        0.2488  vmlinux                  crc32_le
      18       100.000  vmlinux                  crc32_le [self]
    -------------------------------------------------------------------------------
    18        0.2488  vmlinux                  ewma_add
      18       100.000  vmlinux                  ewma_add [self]
    -------------------------------------------------------------------------------
    17        0.2350  vmlinux                  skb_push
      17       100.000  vmlinux                  skb_push [self]
    -------------------------------------------------------------------------------
    16        0.2211  vmlinux                  __d_lookup_rcu
      16       100.000  vmlinux                  __d_lookup_rcu [self]
    -------------------------------------------------------------------------------
    16        0.2211  vmlinux                  core_sys_select
      16       100.000  vmlinux                  core_sys_select [self]
    -------------------------------------------------------------------------------
    16        0.2211  vmlinux                  tcp_send_ack
      16       100.000  vmlinux                  tcp_send_ack [self]
    -------------------------------------------------------------------------------
    14        0.1935  vmlinux                  __nla_reserve
      14       100.000  vmlinux                  __nla_reserve [self]
    -------------------------------------------------------------------------------
    14        0.1935  vmlinux                  dev_queue_xmit
      14       100.000  vmlinux                  dev_queue_xmit [self]
    -------------------------------------------------------------------------------
    14        0.1935  vmlinux                  skb_queue_tail
      14       100.000  vmlinux                  skb_queue_tail [self]
    -------------------------------------------------------------------------------
    13        0.1797  vmlinux                  add_wait_queue
      13       100.000  vmlinux                  add_wait_queue [self]
    -------------------------------------------------------------------------------
    13        0.1797  vmlinux                  dev_hard_start_xmit
      13       100.000  vmlinux                  dev_hard_start_xmit [self]
    -------------------------------------------------------------------------------
    13        0.1797  vmlinux                  local_bh_disable
      13       100.000  vmlinux                  local_bh_disable [self]
    -------------------------------------------------------------------------------
    13        0.1797  vmlinux                  mips_dma_map_page
      13       100.000  vmlinux                  mips_dma_map_page [self]
    -------------------------------------------------------------------------------
    12        0.1659  oprofile                 /oprofile
      12       100.000  oprofile                 /oprofile [self]
    -------------------------------------------------------------------------------
    12        0.1659  vmlinux                  __copy_skb_header
      12       100.000  vmlinux                  __copy_skb_header [self]
    -------------------------------------------------------------------------------
    12        0.1659  vmlinux                  __queue_work
      12       100.000  vmlinux                  __queue_work [self]
    -------------------------------------------------------------------------------
    12        0.1659  vmlinux                  ip_queue_xmit
      12       100.000  vmlinux                  ip_queue_xmit [self]
    -------------------------------------------------------------------------------
    12        0.1659  vmlinux                  remove_wait_queue
      12       100.000  vmlinux                  remove_wait_queue [self]
    -------------------------------------------------------------------------------
    11        0.1520  iptable_filter           /iptable_filter
      11       100.000  iptable_filter           /iptable_filter [self]
    -------------------------------------------------------------------------------
    11        0.1520  vmlinux                  __skb_checksum_complete_head
      11       100.000  vmlinux                  __skb_checksum_complete_head [self]
    -------------------------------------------------------------------------------
    11        0.1520  vmlinux                  ip_finish_output
      11       100.000  vmlinux                  ip_finish_output [self]
    -------------------------------------------------------------------------------
    11        0.1520  vmlinux                  ip_local_deliver
      11       100.000  vmlinux                  ip_local_deliver [self]
    -------------------------------------------------------------------------------
    11        0.1520  vmlinux                  skb_checksum
      11       100.000  vmlinux                  skb_checksum [self]
    -------------------------------------------------------------------------------
    10        0.1382  ipv6                     /ipv6
      10       100.000  ipv6                     /ipv6 [self]
    -------------------------------------------------------------------------------
    10        0.1382  libnetsnmp.so.15.1.2     /usr/lib/libnetsnmp.so.15.1.2
      10       100.000  libnetsnmp.so.15.1.2     /usr/lib/libnetsnmp.so.15.1.2 [self]
    -------------------------------------------------------------------------------
    10        0.1382  vmlinux                  __schedule
      10       100.000  vmlinux                  __schedule [self]
    -------------------------------------------------------------------------------
    10        0.1382  vmlinux                  fsnotify
      10       100.000  vmlinux                  fsnotify [self]
    -------------------------------------------------------------------------------
    10        0.1382  vmlinux                  handle_pte_fault
      10       100.000  vmlinux                  handle_pte_fault [self]
    -------------------------------------------------------------------------------
    10        0.1382  vmlinux                  ip_local_deliver_finish
      10       100.000  vmlinux                  ip_local_deliver_finish [self]
    -------------------------------------------------------------------------------
    10        0.1382  vmlinux                  ip_output
      10       100.000  vmlinux                  ip_output [self]
    -------------------------------------------------------------------------------
    10        0.1382  vmlinux                  ktime_get_ts
      10       100.000  vmlinux                  ktime_get_ts [self]
    -------------------------------------------------------------------------------
    9         0.1244  ath                      /ath
      9        100.000  ath                      /ath [self]
    -------------------------------------------------------------------------------
    9         0.1244  vmlinux                  __kfree_skb
      9        100.000  vmlinux                  __kfree_skb [self]
    -------------------------------------------------------------------------------
    9         0.1244  vmlinux                  __strncpy_from_user_nocheck_asm
      9        100.000  vmlinux                  __strncpy_from_user_nocheck_asm [self]
    -------------------------------------------------------------------------------
    9         0.1244  vmlinux                  mod_timer
      9        100.000  vmlinux                  mod_timer [self]
    -------------------------------------------------------------------------------
    9         0.1244  vmlinux                  netlink_recvmsg
      9        100.000  vmlinux                  netlink_recvmsg [self]
    -------------------------------------------------------------------------------
    9         0.1244  vmlinux                  tcp_rcv_rtt_update
      9        100.000  vmlinux                  tcp_rcv_rtt_update [self]
    -------------------------------------------------------------------------------
    9         0.1244  vmlinux                  unix_dgram_poll
      9        100.000  vmlinux                  unix_dgram_poll [self]
    -------------------------------------------------------------------------------
    8         0.1106  vmlinux                  blast_dcache32
      8        100.000  vmlinux                  blast_dcache32 [self]
    -------------------------------------------------------------------------------
    8         0.1106  vmlinux                  eth_type_trans
      8        100.000  vmlinux                  eth_type_trans [self]
    -------------------------------------------------------------------------------
    8         0.1106  vmlinux                  get_slab.isra.52
      8        100.000  vmlinux                  get_slab.isra.52 [self]
    -------------------------------------------------------------------------------
    8         0.1106  vmlinux                  led_trigger_event
      8        100.000  vmlinux                  led_trigger_event [self]
    -------------------------------------------------------------------------------
    8         0.1106  vmlinux                  poll_select_copy_remaining
      8        100.000  vmlinux                  poll_select_copy_remaining [self]
    -------------------------------------------------------------------------------
    8         0.1106  vmlinux                  process_one_work
      8        100.000  vmlinux                  process_one_work [self]
    -------------------------------------------------------------------------------
    8         0.1106  vmlinux                  r4k_dma_cache_wback_inv
      8        100.000  vmlinux                  r4k_dma_cache_wback_inv [self]
    -------------------------------------------------------------------------------
    8         0.1106  vmlinux                  sch_direct_xmit
      8        100.000  vmlinux                  sch_direct_xmit [self]
    -------------------------------------------------------------------------------
    7         0.0968  netserver                /usr/bin/netserver
      7        100.000  netserver                /usr/bin/netserver [self]
    -------------------------------------------------------------------------------
    7         0.0968  vmlinux                  __hrtimer_start_range_ns
      7        100.000  vmlinux                  __hrtimer_start_range_ns [self]
    -------------------------------------------------------------------------------
    7         0.0968  vmlinux                  do_last.isra.37
      7        100.000  vmlinux                  do_last.isra.37 [self]
    -------------------------------------------------------------------------------
    7         0.0968  vmlinux                  skb_pull
      7        100.000  vmlinux                  skb_pull [self]
    -------------------------------------------------------------------------------
    7         0.0968  vmlinux                  sock_rfree
      7        100.000  vmlinux                  sock_rfree [self]
    -------------------------------------------------------------------------------
    7         0.0968  vmlinux                  sys_select
      7        100.000  vmlinux                  sys_select [self]
    -------------------------------------------------------------------------------
    6         0.0829  nf_defrag_ipv4           /nf_defrag_ipv4
      6        100.000  nf_defrag_ipv4           /nf_defrag_ipv4 [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  __ip_local_out
      6        100.000  vmlinux                  __ip_local_out [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  __kmalloc
      6        100.000  vmlinux                  __kmalloc [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  __sys_recvmsg
      6        100.000  vmlinux                  __sys_recvmsg [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  __tcp_ack_snd_check
      6        100.000  vmlinux                  __tcp_ack_snd_check [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  __tcp_select_window
      6        100.000  vmlinux                  __tcp_select_window [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  __tcp_v4_send_check
      6        100.000  vmlinux                  __tcp_v4_send_check [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  dev_ioctl
      6        100.000  vmlinux                  dev_ioctl [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  do_lookup
      6        100.000  vmlinux                  do_lookup [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  handle_sys
      6        100.000  vmlinux                  handle_sys [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  hrtimer_try_to_cancel
      6        100.000  vmlinux                  hrtimer_try_to_cancel [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  ip_local_out
      6        100.000  vmlinux                  ip_local_out [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  path_openat
      6        100.000  vmlinux                  path_openat [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  skb_copy_bits
      6        100.000  vmlinux                  skb_copy_bits [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  tasklet_action
      6        100.000  vmlinux                  tasklet_action [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  tcp_options_write
      6        100.000  vmlinux                  tcp_options_write [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  unmap_vmas
      6        100.000  vmlinux                  unmap_vmas [self]
    -------------------------------------------------------------------------------
    6         0.0829  vmlinux                  worker_thread
      6        100.000  vmlinux                  worker_thread [self]
    -------------------------------------------------------------------------------
    5         0.0691  ath9k_common             /ath9k_common
      5        100.000  ath9k_common             /ath9k_common [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  __do_fault
      5        100.000  vmlinux                  __do_fault [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  __rtl8366_smi_write_reg
      5        100.000  vmlinux                  __rtl8366_smi_write_reg [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  ip_rcv_finish
      5        100.000  vmlinux                  ip_rcv_finish [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  ipv4_dst_check
      5        100.000  vmlinux                  ipv4_dst_check [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  ipv4_validate_peer
      5        100.000  vmlinux                  ipv4_validate_peer [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  nla_put
      5        100.000  vmlinux                  nla_put [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  rtnl_fill_ifinfo
      5        100.000  vmlinux                  rtnl_fill_ifinfo [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  schedule
      5        100.000  vmlinux                  schedule [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  select_estimate_accuracy
      5        100.000  vmlinux                  select_estimate_accuracy [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  snmp_fold_field64
      5        100.000  vmlinux                  snmp_fold_field64 [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  sock_def_readable
      5        100.000  vmlinux                  sock_def_readable [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  tcp_rcv_space_adjust
      5        100.000  vmlinux                  tcp_rcv_space_adjust [self]
    -------------------------------------------------------------------------------
    5         0.0691  vmlinux                  vm_normal_page
      5        100.000  vmlinux                  vm_normal_page [self]
    -------------------------------------------------------------------------------
    4         0.0553  dropbear                 /usr/sbin/dropbear
      4        100.000  dropbear                 /usr/sbin/dropbear [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  __dentry_open.isra.15
      4        100.000  vmlinux                  __dentry_open.isra.15 [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  filemap_fault
      4        100.000  vmlinux                  filemap_fault [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  filp_close
      4        100.000  vmlinux                  filp_close [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  find_vma
      4        100.000  vmlinux                  find_vma [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  ktime_get_real
      4        100.000  vmlinux                  ktime_get_real [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  memcmp
      4        100.000  vmlinux                  memcmp [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  memcpy_toiovec
      4        100.000  vmlinux                  memcpy_toiovec [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  memmove
      4        100.000  vmlinux                  memmove [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  memset
      4        100.000  vmlinux                  memset [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  netif_skb_features
      4        100.000  vmlinux                  netif_skb_features [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  netlink_unicast
      4        100.000  vmlinux                  netlink_unicast [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  ovl_permission
      4        100.000  vmlinux                  ovl_permission [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  packet_poll
      4        100.000  vmlinux                  packet_poll [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  poll_freewait
      4        100.000  vmlinux                  poll_freewait [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  put_page
      4        100.000  vmlinux                  put_page [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  raw_local_deliver
      4        100.000  vmlinux                  raw_local_deliver [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  ring_buffer_event_length
      4        100.000  vmlinux                  ring_buffer_event_length [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  schedule_hrtimeout_range_clock
      4        100.000  vmlinux                  schedule_hrtimeout_range_clock [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  sk_filter
      4        100.000  vmlinux                  sk_filter [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  skb_copy
      4        100.000  vmlinux                  skb_copy [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  sock_recvmsg
      4        100.000  vmlinux                  sock_recvmsg [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  tcp_cleanup_rbuf
      4        100.000  vmlinux                  tcp_cleanup_rbuf [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  timespec_add_safe
      4        100.000  vmlinux                  timespec_add_safe [self]
    -------------------------------------------------------------------------------
    4         0.0553  vmlinux                  vfs_write
      4        100.000  vmlinux                  vfs_write [self]
    -------------------------------------------------------------------------------
    3         0.0415  ip6_tables               /ip6_tables
      3        100.000  ip6_tables               /ip6_tables [self]
    -------------------------------------------------------------------------------
    3         0.0415  iptable_raw              /iptable_raw
      3        100.000  iptable_raw              /iptable_raw [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  __fsnotify_parent
      3        100.000  vmlinux                  __fsnotify_parent [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  __lshrdi3
      3        100.000  vmlinux                  __lshrdi3 [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  __nla_put
      3        100.000  vmlinux                  __nla_put [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  __rcu_process_callbacks
      3        100.000  vmlinux                  __rcu_process_callbacks [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  __wake_up
      3        100.000  vmlinux                  __wake_up [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  alloc_fd
      3        100.000  vmlinux                  alloc_fd [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  anon_vma_clone
      3        100.000  vmlinux                  anon_vma_clone [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  blast_icache32
      3        100.000  vmlinux                  blast_icache32 [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  copy_skb_header
      3        100.000  vmlinux                  copy_skb_header [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  do_filp_open
      3        100.000  vmlinux                  do_filp_open [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  do_gettimeofday
      3        100.000  vmlinux                  do_gettimeofday [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  do_page_fault
      3        100.000  vmlinux                  do_page_fault [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  dup_mm
      3        100.000  vmlinux                  dup_mm [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  generic_permission
      3        100.000  vmlinux                  generic_permission [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  get_empty_filp
      3        100.000  vmlinux                  get_empty_filp [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  harmonize_features.isra.41
      3        100.000  vmlinux                  harmonize_features.isra.41 [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  iowrite32
      3        100.000  vmlinux                  iowrite32 [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  mips_dma_mapping_error
      3        100.000  vmlinux                  mips_dma_mapping_error [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  move_addr_to_user
      3        100.000  vmlinux                  move_addr_to_user [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  mutex_lock
      3        100.000  vmlinux                  mutex_lock [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  page_waitqueue
      3        100.000  vmlinux                  page_waitqueue [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  path_init
      3        100.000  vmlinux                  path_init [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  path_put
      3        100.000  vmlinux                  path_put [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  prepare_to_wait
      3        100.000  vmlinux                  prepare_to_wait [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  radix_tree_lookup_element
      3        100.000  vmlinux                  radix_tree_lookup_element [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  release_sock
      3        100.000  vmlinux                  release_sock [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  rtl8366_smi_read_reg
      3        100.000  vmlinux                  rtl8366_smi_read_reg [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  rtnl_dump_ifinfo
      3        100.000  vmlinux                  rtnl_dump_ifinfo [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  set_normalized_timespec
      3        100.000  vmlinux                  set_normalized_timespec [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  sk_wait_data
      3        100.000  vmlinux                  sk_wait_data [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  sockfd_lookup_light
      3        100.000  vmlinux                  sockfd_lookup_light [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  stack_done
      3        100.000  vmlinux                  stack_done [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  strnlen
      3        100.000  vmlinux                  strnlen [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  tcp_send_delayed_ack
      3        100.000  vmlinux                  tcp_send_delayed_ack [self]
    -------------------------------------------------------------------------------
    3         0.0415  vmlinux                  unlink_anon_vmas
      3        100.000  vmlinux                  unlink_anon_vmas [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  __skb_recv_datagram
      2        100.000  vmlinux                  __skb_recv_datagram [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  __strnlen_user_nocheck_asm
      2        100.000  vmlinux                  __strnlen_user_nocheck_asm [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  __update_tlb
      2        100.000  vmlinux                  __update_tlb [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  __vm_enough_memory
      2        100.000  vmlinux                  __vm_enough_memory [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  _cond_resched
      2        100.000  vmlinux                  _cond_resched [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  bitbang_work
      2        100.000  vmlinux                  bitbang_work [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  c0_hpt_read
      2        100.000  vmlinux                  c0_hpt_read [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  complete_walk
      2        100.000  vmlinux                  complete_walk [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  copy_user_highpage
      2        100.000  vmlinux                  copy_user_highpage [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  cpu_idle
      2        100.000  vmlinux                  cpu_idle [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  csum_partial_copy_nocheck
      2        100.000  vmlinux                  csum_partial_copy_nocheck [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  do_ade
      2        100.000  vmlinux                  do_ade [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  do_mmap_pgoff
      2        100.000  vmlinux                  do_mmap_pgoff [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  do_sys_open
      2        100.000  vmlinux                  do_sys_open [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  expand_files
      2        100.000  vmlinux                  expand_files [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  file_free_rcu
      2        100.000  vmlinux                  file_free_rcu [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  find_vma_prepare
      2        100.000  vmlinux                  find_vma_prepare [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  get_page_from_freelist
      2        100.000  vmlinux                  get_page_from_freelist [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  getname_flags
      2        100.000  vmlinux                  getname_flags [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  handle_mm_fault
      2        100.000  vmlinux                  handle_mm_fault [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  inet_dump_ifaddr
      2        100.000  vmlinux                  inet_dump_ifaddr [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  inet_fill_link_af
      2        100.000  vmlinux                  inet_fill_link_af [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  inet_gifconf
      2        100.000  vmlinux                  inet_gifconf [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  mips_dma_unmap_page
      2        100.000  vmlinux                  mips_dma_unmap_page [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  mutex_unlock
      2        100.000  vmlinux                  mutex_unlock [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  number.isra.6
      2        100.000  vmlinux                  number.isra.6 [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  page_remove_rmap
      2        100.000  vmlinux                  page_remove_rmap [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  put_pid
      2        100.000  vmlinux                  put_pid [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  r4k_blast_dcache_page_dc32
      2        100.000  vmlinux                  r4k_blast_dcache_page_dc32 [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  rb_event_data_length
      2        100.000  vmlinux                  rb_event_data_length [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  rb_insert_color
      2        100.000  vmlinux                  rb_insert_color [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  rcu_bh_qs
      2        100.000  vmlinux                  rcu_bh_qs [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  rcu_idle_enter
      2        100.000  vmlinux                  rcu_idle_enter [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  run_ksoftirqd
      2        100.000  vmlinux                  run_ksoftirqd [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  run_timer_softirq
      2        100.000  vmlinux                  run_timer_softirq [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  skb_checksum_help
      2        100.000  vmlinux                  skb_checksum_help [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  skb_free_datagram
      2        100.000  vmlinux                  skb_free_datagram [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  strlen
      2        100.000  vmlinux                  strlen [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  sys_gettimeofday
      2        100.000  vmlinux                  sys_gettimeofday [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  sys_recvfrom
      2        100.000  vmlinux                  sys_recvfrom [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  sys_write
      2        100.000  vmlinux                  sys_write [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  tcp_established_options
      2        100.000  vmlinux                  tcp_established_options [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  tcp_v4_do_rcv
      2        100.000  vmlinux                  tcp_v4_do_rcv [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  unlock_page
      2        100.000  vmlinux                  unlock_page [self]
    -------------------------------------------------------------------------------
    2         0.0276  vmlinux                  write_pool
      2        100.000  vmlinux                  write_pool [self]
    -------------------------------------------------------------------------------
    1         0.0138  libdns.so.93.1.0         /usr/lib/libdns.so.93.1.0
      1        100.000  libdns.so.93.1.0         /usr/lib/libdns.so.93.1.0 [self]
    -------------------------------------------------------------------------------
    1         0.0138  libisc.so.90.1.0         /usr/lib/libisc.so.90.1.0
      1        100.000  libisc.so.90.1.0         /usr/lib/libisc.so.90.1.0 [self]
    -------------------------------------------------------------------------------
    1         0.0138  libnetsnmpagent.so.15.1.2 /usr/lib/libnetsnmpagent.so.15.1.2
      1        100.000  libnetsnmpagent.so.15.1.2 /usr/lib/libnetsnmpagent.so.15.1.2 [self]
    -------------------------------------------------------------------------------
    1         0.0138  libnetsnmphelpers.so.15.1.2 /usr/lib/libnetsnmphelpers.so.15.1.2
      1        100.000  libnetsnmphelpers.so.15.1.2 /usr/lib/libnetsnmphelpers.so.15.1.2 [self]
    -------------------------------------------------------------------------------
    1         0.0138  libpthread-0.9.33.so     /lib/libpthread-0.9.33.so
      1        100.000  libpthread-0.9.33.so     /lib/libpthread-0.9.33.so [self]
    -------------------------------------------------------------------------------
    1         0.0138  samba_multicall          /usr/sbin/samba_multicall
      1        100.000  samba_multicall          /usr/sbin/samba_multicall [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __alloc_pages_nodemask
      1        100.000  vmlinux                  __alloc_pages_nodemask [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __d_alloc
      1        100.000  vmlinux                  __d_alloc [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __d_lookup
      1        100.000  vmlinux                  __d_lookup [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __down_read
      1        100.000  vmlinux                  __down_read [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __down_write_nested
      1        100.000  vmlinux                  __down_write_nested [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __flush_dcache_page
      1        100.000  vmlinux                  __flush_dcache_page [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __get_free_pages
      1        100.000  vmlinux                  __get_free_pages [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __lru_cache_add
      1        100.000  vmlinux                  __lru_cache_add [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __ndelay
      1        100.000  vmlinux                  __ndelay [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __page_cache_release.part.11
      1        100.000  vmlinux                  __page_cache_release.part.11 [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __pte_alloc
      1        100.000  vmlinux                  __pte_alloc [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __put_anon_vma
      1        100.000  vmlinux                  __put_anon_vma [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __sk_dst_check
      1        100.000  vmlinux                  __sk_dst_check [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __split_vma
      1        100.000  vmlinux                  __split_vma [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __srcu_read_lock
      1        100.000  vmlinux                  __srcu_read_lock [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __strncpy_from_user_asm
      1        100.000  vmlinux                  __strncpy_from_user_asm [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  __update_cache
      1        100.000  vmlinux                  __update_cache [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  add_to_page_cache_locked
      1        100.000  vmlinux                  add_to_page_cache_locked [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  ag71xx_poll
      1        100.000  vmlinux                  ag71xx_poll [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  anon_vma_prepare
      1        100.000  vmlinux                  anon_vma_prepare [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  arch_get_unmapped_area_common
      1        100.000  vmlinux                  arch_get_unmapped_area_common [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  blast_icache32_page
      1        100.000  vmlinux                  blast_icache32_page [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  cap_file_mmap
      1        100.000  vmlinux                  cap_file_mmap [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  cdev_get
      1        100.000  vmlinux                  cdev_get [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  cdev_put
      1        100.000  vmlinux                  cdev_put [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  chrdev_open
      1        100.000  vmlinux                  chrdev_open [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  consume_skb
      1        100.000  vmlinux                  consume_skb [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  copy_pte_range
      1        100.000  vmlinux                  copy_pte_range [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  d_lookup
      1        100.000  vmlinux                  d_lookup [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  dev_get_stats
      1        100.000  vmlinux                  dev_get_stats [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  do_exit
      1        100.000  vmlinux                  do_exit [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  do_munmap
      1        100.000  vmlinux                  do_munmap [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  do_vfs_ioctl
      1        100.000  vmlinux                  do_vfs_ioctl [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  do_wp_page.isra.77
      1        100.000  vmlinux                  do_wp_page.isra.77 [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  dput
      1        100.000  vmlinux                  dput [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  drop_file_write_access
      1        100.000  vmlinux                  drop_file_write_access [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  extract_buf
      1        100.000  vmlinux                  extract_buf [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  fd_install
      1        100.000  vmlinux                  fd_install [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  find_get_page
      1        100.000  vmlinux                  find_get_page [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  find_next_zero_bit
      1        100.000  vmlinux                  find_next_zero_bit [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  format_decode
      1        100.000  vmlinux                  format_decode [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  free_pgtables
      1        100.000  vmlinux                  free_pgtables [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  generic_make_request_checks
      1        100.000  vmlinux                  generic_make_request_checks [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  get_pageblock_flags_group
      1        100.000  vmlinux                  get_pageblock_flags_group [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  get_work_gcwq
      1        100.000  vmlinux                  get_work_gcwq [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  hrtimer_init
      1        100.000  vmlinux                  hrtimer_init [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  inet_create
      1        100.000  vmlinux                  inet_create [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  inet_recvmsg
      1        100.000  vmlinux                  inet_recvmsg [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  inode_permission
      1        100.000  vmlinux                  inode_permission [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  install_special_mapping
      1        100.000  vmlinux                  install_special_mapping [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  ioread32
      1        100.000  vmlinux                  ioread32 [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  kfree_skb
      1        100.000  vmlinux                  kfree_skb [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  ktime_add_ns
      1        100.000  vmlinux                  ktime_add_ns [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  ktime_add_safe
      1        100.000  vmlinux                  ktime_add_safe [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  load_elf_binary
      1        100.000  vmlinux                  load_elf_binary [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  lock_sock_nested
      1        100.000  vmlinux                  lock_sock_nested [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  locks_remove_flock
      1        100.000  vmlinux                  locks_remove_flock [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  locks_remove_posix
      1        100.000  vmlinux                  locks_remove_posix [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  md5_transform
      1        100.000  vmlinux                  md5_transform [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  memcpy
      1        100.000  vmlinux                  memcpy [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  mmap_region
      1        100.000  vmlinux                  mmap_region [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  mntget
      1        100.000  vmlinux                  mntget [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  mntput_no_expire
      1        100.000  vmlinux                  mntput_no_expire [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  module_put
      1        100.000  vmlinux                  module_put [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  netdev_run_todo
      1        100.000  vmlinux                  netdev_run_todo [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  netlink_lookup.isra.16
      1        100.000  vmlinux                  netlink_lookup.isra.16 [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  netlink_table_ungrab
      1        100.000  vmlinux                  netlink_table_ungrab [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  netlink_trim
      1        100.000  vmlinux                  netlink_trim [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  nla_reserve
      1        100.000  vmlinux                  nla_reserve [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  ovl_entry_real
      1        100.000  vmlinux                  ovl_entry_real [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  pagevec_lru_move_fn
      1        100.000  vmlinux                  pagevec_lru_move_fn [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  path_get
      1        100.000  vmlinux                  path_get [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  pgd_init
      1        100.000  vmlinux                  pgd_init [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  poll_schedule_timeout
      1        100.000  vmlinux                  poll_schedule_timeout [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  poll_select_set_timeout
      1        100.000  vmlinux                  poll_select_set_timeout [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  prio_tree_insert
      1        100.000  vmlinux                  prio_tree_insert [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  queue_delayed_work_on
      1        100.000  vmlinux                  queue_delayed_work_on [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  r4k_flush_cache_page
      1        100.000  vmlinux                  r4k_flush_cache_page [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  rcu_idle_exit
      1        100.000  vmlinux                  rcu_idle_exit [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  release_pages
      1        100.000  vmlinux                  release_pages [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  release_task
      1        100.000  vmlinux                  release_task [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  remove_vma
      1        100.000  vmlinux                  remove_vma [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  ret_from_exception
      1        100.000  vmlinux                  ret_from_exception [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  round_jiffies_common
      1        100.000  vmlinux                  round_jiffies_common [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  rtnl_dump_all
      1        100.000  vmlinux                  rtnl_dump_all [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  rw_verify_area
      1        100.000  vmlinux                  rw_verify_area [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  schedule_timeout
      1        100.000  vmlinux                  schedule_timeout [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  sha_transform
      1        100.000  vmlinux                  sha_transform [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  shmem_getpage_gfp
      1        100.000  vmlinux                  shmem_getpage_gfp [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  sk_free
      1        100.000  vmlinux                  sk_free [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  skb_dequeue
      1        100.000  vmlinux                  skb_dequeue [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  skip_atoi
      1        100.000  vmlinux                  skip_atoi [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  sock_close
      1        100.000  vmlinux                  sock_close [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  sock_wfree
      1        100.000  vmlinux                  sock_wfree [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  spi_async_locked
      1        100.000  vmlinux                  spi_async_locked [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  squashfs_read_metadata
      1        100.000  vmlinux                  squashfs_read_metadata [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  strchr
      1        100.000  vmlinux                  strchr [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  sys_close
      1        100.000  vmlinux                  sys_close [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  sys_open
      1        100.000  vmlinux                  sys_open [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  sys_read
      1        100.000  vmlinux                  sys_read [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  sys_recv
      1        100.000  vmlinux                  sys_recv [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  sys_sendto
      1        100.000  vmlinux                  sys_sendto [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  tcp_collapse
      1        100.000  vmlinux                  tcp_collapse [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  tcp_v4_send_check
      1        100.000  vmlinux                  tcp_v4_send_check [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  unix_peer_get
      1        100.000  vmlinux                  unix_peer_get [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  user_path_at_empty
      1        100.000  vmlinux                  user_path_at_empty [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  vfs_fstatat
      1        100.000  vmlinux                  vfs_fstatat [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  vfs_read
      1        100.000  vmlinux                  vfs_read [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  vm_get_page_prot
      1        100.000  vmlinux                  vm_get_page_prot [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  vma_merge
      1        100.000  vmlinux                  vma_merge [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  vsnprintf
      1        100.000  vmlinux                  vsnprintf [self]
    -------------------------------------------------------------------------------
    1         0.0138  vmlinux                  xz_dec_lzma2_run
      1        100.000  vmlinux                  xz_dec_lzma2_run [self]
    -------------------------------------------------------------------------------
