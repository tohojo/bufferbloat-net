
---
title: Minstrel_Wireless_Rate_Selection
date: 2012-07-08T12:42:28
lastmod: 2012-07-08T12:42:28
---
Minstrel Wireless Rate Selection
================================

    root@davesroof:/sys/kernel/debug/ieee80211/phy0/netdev:wlan0/stations/00:27:22:a8:a3:1a# cat rc_stats
        type      rate     throughput  ewma prob   this prob  this succ/attempt   success    attempts
        HT20/LGI    MCS0        3.6       58.0      100.0          0(  0)        306         384
        HT20/LGI    MCS1        8.8       75.4       19.9          0(  0)        731        1185
        HT20/LGI    MCS2        5.1       31.0        0.0          0(  0)       1578        2538
        HT20/LGI  t MCS3       14.4       69.2      100.0          0(  0)      21405       26086
        HT20/LGI T PMCS4       27.4       97.6      100.0          0(  0)     153050      185927
        HT20/LGI    MCS5       14.0       41.4        0.0          0(  0)       1827        4486
        HT20/LGI    MCS6        0.0        0.0        0.0          0(  0)         10        1426
        HT20/LGI    MCS7        0.0        0.0        0.0          0(  0)          0        1428
        HT20/LGI    MCS8        8.4       71.5      100.0          0(  0)        528         784
        HT20/LGI    MCS9        5.3       25.7        0.0          0(  0)       9196       12302
        HT20/LGI    MCS10      10.4       37.1        0.0          0(  0)      18929       28297
        HT20/LGI    MCS11      14.1       41.7      100.0          0(  0)      23875       35908
        HT20/LGI    MCS12       0.0        0.0        0.0          0(  0)        591        2410
        HT20/LGI    MCS13       0.0        0.0        0.0          0(  0)          0        1428
        HT20/LGI    MCS14       0.0        0.0        0.0          0(  0)          0        1433
        HT20/LGI    MCS15       0.0        0.0        0.0          0(  0)          0        1431

        Total packet count::    ideal 217212      lookaround 14954
        Average A-MPDU length: 1.0


    root@davesroof:/sys/kernel/debug/ieee80211# cd phy0/
        root@davesroof:/sys/kernel/debug/ieee80211/phy0# ls
        ath9k                    ht40allow_map            netdev:wlan0             reset                    total_ps_buffered
        channel_type             hwflags                  power                    rts_threshold            user_power
        fragmentation_threshold  keys                     queues                   short_retry_limit        wep_iv
        frequency                long_retry_limit         rc                       statistics
        root@davesroof:/sys/kernel/debug/ieee80211/phy0# cd ath9k/
        root@davesroof:/sys/kernel/debug/ieee80211/phy0/ath9k# ls
        base_eeprom    dma            gpio_led       ignore_extcca  modal_eeprom   qlen_vi        regdump        reset          tx_chainmask
        chanbw         dump_nfcal     gpio_mask      interrupt      qlen_be        qlen_vo        regidx         rx_chainmask   xmit
        disable_ani    eeprom         gpio_val       misc           qlen_bk        recv           regval         stations
        root@davesroof:/sys/kernel/debug/ieee80211/phy0/ath9k# cat xmit
        Num-Tx-Queues: 10  tx-queues-setup: 0x10f poll-work-seen: 36206
                                    BE         BK        VI        VO

        MPDUs Queued:            27436        174     15066     12730
        MPDUs Completed:         27322        174     15062     12708
        MPDUs XRetried:            114          0         4        22
        Aggregates:              94194          5         0         0
        AMPDUs Queued HW:       620975         49     21536         0
        AMPDUs Queued SW:       438841          7         0         0
        AMPDUs Completed:      1045702         34      6476         0
        AMPDUs Retried:         438217        728    413300         0
        AMPDUs XRetried:         14114         22     15059         0
        FIFO Underrun:               0          0         0         0
        TXOP Exceeded:               0          0         0         0
        TXTIMER Expiry:              0          0         0         0
        DESC CFG Error:              0          0         0         0
        DATA Underrun:               0          0         0         0
        DELIM Underrun:              0          0         0         0
        TX-Pkts-All:           1087252        230     36601     12730
        TX-Bytes-All:        712792668      12570   3244394   1330716
        hw-put-tx-buf:               1          1         1         1
        hw-tx-start:           1430422        953    449902     12730
        hw-tx-proc-desc:       1430422        953    449901     12730
        TX-Failed:                   0          0         0         0
        txq-memory-address:   81f1a174   81f1a1f0  81f1a0f8  81f1a07c
        axq-qnum:                    2          3         1         0
        axq-depth:                   0          0         1         0
        axq-ampdu_depth:             0          0         1         0
        axq-stopped                  0          0         0         0
        tx-in-progress               0          0         0         0
        pending-frames               0          0         1         0
        txq_headidx:                 0          0         0         0
        txq_tailidx:                 0          0         0         0
        axq_q empty:                   0          0         0         0
        axq_acq empty:                 1          1         1         1
        txq_fifo[0] empty:             1          1         1         1
        txq_fifo[1] empty:             1          1         1         1
        txq_fifo[2] empty:             1          1         1         1
        txq_fifo[3] empty:             1          1         1         1
        txq_fifo[4] empty:             1          1         1         1
        txq_fifo[5] empty:             1          1         1         1
        txq_fifo[6] empty:             1          1         1         1
        txq_fifo[7] empty:             1          1         1         1

