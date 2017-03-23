# ircddbmhd3
ircDDB mheard daemon for the G3 add-on

This repository contains the files for a Centos 7 RPM package.


This program listens on an ethernet interface for ip packets
originating from an RP2C DSTAR Repeater Controller.
It reports its findings via UDP to this software:

https://github.com/dl1bff/ircDDB-DV/blob/master/net/ircDDB/dv/RptrUDPReceiver.java


The code uses a modified version of this file for calculation 
of the Golay (23,12,7) error correction code:

http://www.eccpage.com/golay23.c

*** Because of its copyrights,
*** ALL OF ircDDB-mheard CAN ONLY BE USED IN NON-COMMERCIAL APPLICATIONS!


