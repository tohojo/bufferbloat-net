
---
title: Setting up a Measurement Server
date: 2011-04-19T11:16:14
lastmod: 2011-04-28T09:08:39
---
Setting up a Measurement Server
===============================

**M-Lab nodes**

\* Just after logging in, run the following commands:

    sudo yum -y install subversion
    svn co --username bismark --password broadbandInternet https://svn.comics.unina.it/bismark/trunk/mserver .
    ./scripts/setup-mlab

The measurement server is then operative.\
If needed you can change default options by modifying the
\~/etc/mserver.conf file.\
After modifying the configuration file you have to launch the
./scripts/reload script.

**NOTE** The management server needs to be configured accordingly

**Platform independent**

\* The server needs the following packages installed

    socat
    subversion

-   The user designated to run measurements needs sudo permissions
    (without password) to run **socat**
-   checkout https://svn.comics.unina.it/bismark/trunk/mserver to the
    user home directory
-   setup user's crontab with the provided crontab file

