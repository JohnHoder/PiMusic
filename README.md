# PiMusic

This script will allow you to download songs from youtube and stream them with pifm to FM receivers on specified frequency.

This project is obsolete, it uses old Youtube API v2 which is not suppoted anymore.

I'm working on update to APIv3.

To stream online radio stream to pifm using a pipe, use something like this:
sox -t mp3 listen.pls -t wav -r 22050 -c 1 - | sudo ./pifm - 97.7

# Android
There's also an Android application present, a truly simple one.
It allows you to play songs from youtube to your FM receivers comfortably.
