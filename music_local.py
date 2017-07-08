import io,sys,os
import subprocess
from subprocess import call


search = sys.argv[1]
#search = 'gucci mane one hell of a life'

def downloadAndPlay():
	command = "youtube-dl \"ytsearch:" + search + "\" --extract-audio --audio-format mp3 --prefer-ffmpeg -o - | omxplayer -o local"
	player = subprocess.call(command, shell=True)

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
