import io,sys,os
import subprocess
import re

FREQUENCY = "103.3"

def findAndPlay(search):
	#Local playing will break FM transmitter
	#player = subprocess.call(['cvlc',filename,'--play-and-exit'])
	#player = subprocess.call("omxplayer -o local \"" + filename + "\"", shell=True)

	#We Don't need converting it anymore, we use pipes directly
	#newfilenameraw = filename[:-4]
	#convert = subprocess.call("echo \"y\" | ffmpeg -i \"" + filename + "\" -f wav -acodec pcm_s16le -ar 22050 -ac 1 \"" + newfilenameraw + ".wav\"", shell=True)
	#broadcast = "sudo ./pifm \"" + newfilenameraw + ".wav" + "\" 97.7"

	#filename = "sound.m4a"
	#commandDownload = "youtube-dl \"ytsearch:" + search + "\" -f m4a --audio-format m4a -o \"./sounds/" + filename + "\""
	#down = subprocess.call(commandDownload, shell=True)
	#broadcast = "sox \"" + filename + "\" -t mp3 - channels 1 | avconv -v fatal -i pipe:0 -ac 1 -ar 22050 -b 352k -f wav - | sudo ./pifm - " + FREQUENCY
	#player = subprocess.call(broadcast, shell=True)

<<<<<<< HEAD
	yolo = "youtube-dl --verbose --socket-timeout 1000 \"ytsearch:" + search + "\" -f m4a --audio-format m4a -o - | sox -t m4a /dev/stdin -t mp3 /dev/stdout channels 1 | buffer -s 512k -t -m 32M | ffmpeg -v fatal -i pipe:0 -ac 1 -ar 22050 -b 352k -f s16le - | sudo ./pifm/pifm - " + FREQUENCY + "22050"
=======
	yolo = "youtube-dl \"ytsearch:" + search + "\" -f m4a --audio-format m4a -o - | sox -t m4a /dev/stdin -t mp3 /dev/stdout channels 1 | buffer -s 512k -t -m 16M | avconv -v fatal -i pipe:0 -ac 1 -ar 22050 -b 352k -f s16le - | sudo ./pifm/pifm - " + FREQUENCY + "22050"
>>>>>>> 9a4b1dd61640c7c4059bfa29f624cd91b9bff07a
	player = subprocess.call(yolo, shell=True)

def urlAndPlay(url):
	yolo = "youtube-dl \"" + url + "\" -f m4a --audio-format m4a -o - | sox -t m4a /dev/stdin -t mp3 /dev/stdout channels 1 | buffer -s 512k -t -m 16M | avconv -v fatal -i pipe:0 -ac 1 -ar 22050 -b 352k -f s16le - | sudo ./pifm/pifm - " + FREQUENCY + "22050"
	player = subprocess.call(yolo, shell=True)

if __name__ == '__main__':
	if "--stop" in sys.argv:
		player.stdin.write("q")
		raise SystemExit
	elif "--url" in sys.argv:
		url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', sys.argv[2])[0]
		print url
		urlAndPlay(url)
		raise SystemExit
	else:
		findAndPlay(sys.argv[1])
		raise SystemExit

	if "-h" in sys.argv:
		#helpscr()
		raise SystemExit
