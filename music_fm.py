import io,sys,os
import subprocess

FREQUENCY = "97.7"

search = sys.argv[1]

def downloadAndPlay():
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

	yolo = "youtube-dl \"ytsearch:" + search + "\" -f m4a --audio-format m4a -o - | sox -t m4a /dev/stdin -t mp3 /dev/stdout channels 1 | avconv -v fatal -i pipe:0 -ac 1 -ar 22050 -b 352k -f s16le - | sudo ./pifm/pifm - " + FREQUENCY + "22050"
	player = subprocess.call(yolo, shell=True)


if __name__ == '__main__':
	if "--stop" in sys.argv:
		player.stdin.write("q")
		raise SystemExit

	else:
		downloadAndPlay()
		raise SystemExit

	if "-h" in sys.argv:
		#helpscr()
		raise SystemExit
