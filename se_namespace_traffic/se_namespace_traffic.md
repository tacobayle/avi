```
[admin:100-100-11-11]: > attach serviceengine AVICTRL_Avi-se-bsfdt
Warning: Permanently added '[127.1.0.5]:5097' (ECDSA) to the list of known hosts.

Avi Service Engine

Avi Networks software, Copyright (C) 2013-2017 by Avi Networks, Inc.
All rights reserved.

Management:   100.100.11.214/24              UP
Gateway:      100.100.11.1                   UP
Controller:   100.100.11.11                  UP





The copyrights to certain works contained in this software are
owned by other third parties and used and distributed under
license. Certain components of this software are licensed under



the GNU General Public License (GPL) version 2.0 or the GNU
Lesser General Public License (LGPL) Version 2.1. A copy of each
such license is available at
http://www.opensource.org/licenses/gpl-2.0.php and
http://www.opensource.org/licenses/lgpl-2.1.php
Last login: Tue Feb  7 12:09:45 2023 from ::1
admin@AVICTRL-Avi-se-bsfdt:~$
admin@AVICTRL-Avi-se-bsfdt:~$ ip netns
avi_ns3
avi_ns2
avi_poll_ns2
avi_poll_ns1
admin@AVICTRL-Avi-se-bsfdt:~$
admin@AVICTRL-Avi-se-bsfdt:~$ sudo ip netns exec avi_ns2 ip route
default via 100.100.31.1 dev avi_eth2 metric 30000
100.100.31.0/24 dev avi_eth2 proto kernel scope link src 100.100.31.211
admin@AVICTRL-Avi-se-bsfdt:~$
admin@AVICTRL-Avi-se-bsfdt:~$
admin@AVICTRL-Avi-se-bsfdt:~$ sudo ip netns exec avi_ns2 curl 100.100.21.11
Hello World - Cloud is NSX - IP is 100.100.21.11
admin@AVICTRL-Avi-se-bsfdt:~$
```