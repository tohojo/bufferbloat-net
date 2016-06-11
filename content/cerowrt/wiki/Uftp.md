
---
title: Uftp
date: 2011-07-14T07:06:10
lastmod: 2011-08-01T11:57:23
type: wiki
---
Uftp
====

Description
-----------

"UFTP is an encrypted multicast file transfer program, designed to
securely, reliably, and efficiently transfer files to multiple receivers
simultaneously. This is useful for distributing large files to a large
number of receivers, and is especially useful for data distribution over
a satellite link (with two way communication), where the inherent delay
makes any TCP based communication highly inefficient. The multicast
encryption scheme is based on TLS with extensions to allow multiple
receivers to share a common key. UFTP also has the capability to
communicate over disjoint networks separated by one or more firewalls
(NAT traversal) and without full end-to-end multicast capability
(multicast tunneling) through the use of a UFTP proxy server. These
proxies also provide scalability by aggregating responses from a group
of receivers.

UFTP has been used in the production process of The Wall Street Journal
to send WSJ pages over satellite to their remote printing plants, and
other users have used it to send to over 1000 receivers.\
h3. Protocol Summary

A UFTP session consists of 3 main phases: The Announce/Register phase,
the File Transfer phase, and the Completion/Confirmation phase. The File
Transfer phase additionally consists of the File Info phase and the Data
Transfer phase for each file sent.

The Announce/Register phase sets up the multicast file transfer session
and negotiates all encryption parameters. The server sends out an
announcement over a public multicast address which the clients are
expected to be listening on. All subsequent messages from the server go
over a private multicast address specified in the announcement. Allowed
clients send a registration to respond to the announcement. The server
will then send either a confirmation message if encryption is disabled,
or the encryption key for the session if encryption is enabled. If the
client receives the encryption key, it sends an acknowledgment back to
the server.

The File Transfer phase starts with the File Info phase for the first
file to send. The server sends a message describing the file in
question. Besides the name and size of the file, this message describes
how the file will be broken down. A file is divided into a number of
blocks, and these blocks are grouped into sections. A block is a piece
of the file that is sent in a single packet. A section is a grouping of
blocks that can be sent together before the server needs to request
feedback from the clients. The total number of blocks and sections is
included in this message.

Continuing the File Transfer phase is the Data Transfer phase for the
first file. Data packets, each of which is a block, are sent by the
server at a rate specified by the user. Because UDP does not guarantee
that packets will arrive in order, each block is numbered so the client
can properly reassemble the file. When the server finishes a section, it
send a message to the clients requesting status. The clients then send
back a status message containing the list of NAKs (negative
acknowledgments) for the blocks in that section. Once all sections have
been sent, if the server has received a non zero number of NAKs from any
client, the server will begin a second pass of the data, this time only
sending the packets that were NAKed. The server will continue with
subsequent passes of the data until all clients have either received the
file or have timed out while the server was waited for a status message.
When a client has received the entire file, it sends a completion
message in response to the next status request.

The File Info phase and the Data Transfer phase are then repeated for
each file to be sent during the session

The Completion/Confirmation phase shuts down the session between the
server and clients. It starts with a message from the server indicating
the end of the session. The clients then respond with a completion
message, and the server responds to each completion with a confirmation
message."<link>http://www.tcnj.edu/\~bush/uftp.html</link>

How to test
-----------

Before running UFTP you have to make user that the routing table on your
machine has has a static multi-cast route enabled.\
On Linux: route add -net 224.0.0.0. netmask 240.0.0.0 dev *iface*

Run tests by exchanging files between a client (uftpd) and a server
(uftp).

UFTP Server command example:\
uftp -Y aes256 -h sha1 *FILE* = server sends *FILE* over tls encrypted
with aes256 and sha1

UFTP Client command example:\
uftpd -D *RECV-DIR* -T *TEMP-DIR* -L *LOG*= client daemon saves files
received *RECV-DIR* and temporary files (in case communication is
interrupted) to *TEMP-DIR* and logs to *LOG*

### Experiment design

Router &gt; Router: In this setting we have the uftp package installed
on two **adjacent** routers. One servers as a client, the other as the
server.... IT WORKS!

Host &gt; Router: The host is **directly connected** to the router

\* Wired:\
Host:

     
    matt@wontseeme:~/src/bismark_week/uftp-3.5.1$ ./uftp -D -R 500 /home/matt/Dropbox/ebooks/R/02_corpus_frequency_data.slides.pdf
    UFTP version 3.5.1  Copyright (C) 2001-2011  Dennis A. Bush
    Starting at Thu Jul 14 12:37:08 2011
    Transfer rate: 1000 Kbps (125 KB/s)
    Wait between packets: 11718 us
    Using private multicast address 230.5.5.220  Group ID: 549A4C1C
    Initializing group
    Sending ANNOUNCE 1
    Sending ANNOUNCE 2
    Received REGISTER from client gw.jc.lab.projectbismark.net
    Sending REG_CONF 3.1
    Sending ANNOUNCE 3
    Received REGISTER from client gw.jc.lab.projectbismark.net
    Sending REG_CONF 4.1
    Sending ANNOUNCE 4
    ----- 500 -----
    Error getting file status for 500: No such file or directory
    ----- 02_corpus_frequency_data.slides.pdf -----
    File ID: 0001  Name: 02_corpus_frequency_data.slides.pdf
      sending as R/02_corpus_frequency_data.slides.pdf
    Bytes: 6071756  Blocks: 4205  Sections: 1
    Sending FILEINFO 1.1
    Received INFO_ACK from client gw.jc.lab.projectbismark.net
    Sending FILEINFO 2.1
    Received INFO_ACK+ from client gw.jc.lab.projectbismark.net
    Sending FILEINFO 3.1
    Received INFO_ACK+ from client gw.jc.lab.projectbismark.net
    Sending FILEINFO 4.1
    Received INFO_ACK+ from client gw.jc.lab.projectbismark.net
    Couldn't get INFO_ACK from gw.jc.lab.projectbismark.net
    Maximum file transfer time: 142 seconds
    Sending file...pass 1
    Sending DONE 1.1
    Got 20 NAKs for pass 1 section 1 from client gw.jc.lab.projectbismark.net
    Average wait time = 11718.04 us
    Received 20 distinct NAKs for pass 1
    Sending file...pass 2
    Sending DONE 1.1
    Got COMPLETE from client gw.jc.lab.projectbismark.net
    Average wait time = 11727.70 us
    Received 0 distinct NAKs for pass 2
    Transfer status:
    Host: gw.jc.lab.projectbismark.net  Status: Completed   time:  52.364 seconds    NAKs: 20
    Host: gw.jc.lab.projectbismark.net  Status: Lost connection
    Total elapsed time: 52.364 seconds
    Overall throughput: 113.24 KB/s
    -----------------------------
    Finishing group
    Sending DONE 1.1
    Got COMPLETE from client gw.jc.lab.projectbismark.net
    Late completions:
    Sending DONE_CONF 2.1
    Group complete
    uftp: Finishing at Thu Jul 14 12:38:28 2011

Router:

    uftpd -D /tmp/recv_dir

-   Wireless:

Host &gt; Host

Router &gt; Multiple Hosts: DOES NOT WORK!

Host:\
/uftpd -D /home/matt/src/bismark\_week/ -L works ; tail -f works

2011/07/14 11:30:28.195551: UFTP version 3.5.1 Copyright © 2001-2011
Dennis A. Bush\
2011/07/14 11:30:28.196667: Loaded key with fingerprint
12:7F:6E:58:60:85:63:E4:64:71:25:FA:80:FC:53:F6:46:87:2E:B9

Router:\
root@gw:\~\# uftp -D -L /tmp/1stlog /tmp/file.test\
Killed\
root@gw:\~\# du /tmp/file.test\
12268 /tmp/file.test

Note: the 1stlog file is never created.

### Experiment environment

Routers: Netgear WNDR3700V2 Running CeroWRT smoketest

Host A: Thinkpad X61s\
Linux wontseeme 2.6.38-7.dmz.1-liquorix-amd64 \#1 ZEN SMP PREEMPT Sun
May 22 23:53:16 CDT 2011 x86\_64 x86\_64 x86\_64 GNU/Linux

Host B: Virtualized instance of Ubuntu 10.10 on Macbook Pro\
Macbook: Processor 2 Ghz Intel Core 2 Duo, Memory 2 GB 1067 MHz DDR3
running Mac OS X version 10.6.8\
VM: Linux jupiter 2.6.35-30-generic \#54-Ubuntu SMP Tue Jun 7 18:40:23
UTC 2011 i686 GNU/Linux

### Preliminary Results
