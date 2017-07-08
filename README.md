# PiMusic

Play songs from youtube and stream them directly to your FM receivers on specified frequency.

To stream online radio stream to pifm using a pipe, use something like this:
sox -t mp3 listen.pls -t wav -r 22050 -c 1 - | sudo ./pifm - 97.7

# Android client
There's also a simple Android application so that you can control the thing from your Android device too.
