#!/bin/sh
  now=$(date +%d%m%Y-%H%M%S).h264
  raspivid -o /mnt/video/$now -t 890000 -w 800 -h 600 -fps 15
