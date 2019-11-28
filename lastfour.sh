#!/bin/sh

sudo find /mnt/video/*.h264 -mmin -59 -exec cp {} /home/pi/sync/ \;
