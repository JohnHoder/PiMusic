import pafy
import io,sys,os
import subprocess
import urllib
import json as simplejson


FREQUENCY = "97.7"

search = sys.argv[1]
#search = 'gucci mane one hell of a life'

api = 'https://gdata.youtube.com/feeds/api/videos?q=%s&v=2&alt=json' % search


def downloadAndPlay():
	print urllib.urlopen(api)
	json = simplejson.load(urllib.urlopen(api))

	#title = json['entry']['title']['$t']
	#author = json['entry']['author'][0]['name']

	url = json['feed']['entry'][0]['content']['src']

	print "url:%s\n" % (url)

	############################################################

	#url = "https://www.youtube.com/watch?v=v73ECi8ou8g"
	video = pafy.new(url)

	#best = video.getbest(preftype="webm")

	#print best.url

	#audiostreams = video.audiostreams
	#audiostreams[1].download()

	#bestaudio = video.getbestaudio()
	#bestaudio.download()

	audiostreams = video.audiostreams
	
	print audiostreams

	i=0
	for a in audiostreams:
		i=i+1
		print(a.bitrate, a.extension, a.get_filesize())
		print "Extension: " + a.extension
		if(a.extension=="m4a"):
			break

	print audiostreams

	filename = audiostreams[i-1].download()
	print "Filename: " + filename

	#Local playing will break FM transmitter
	#player = subprocess.call(['cvlc',filename,'--play-and-exit'])
	#player = subprocess.call("omxplayer -o local \"" + filename + "\"", shell=True)

	#We Don't need converting it anymore, we use pipes directly
	#newfilenameraw = filename[:-4]
	#convert = subprocess.call("echo \"y\" | ffmpeg -i \"" + filename + "\" -f wav -acodec pcm_s16le -ar 22050 -ac 1 \"" + newfilenameraw + ".wav\"", shell=True)
	#broadcast = "sudo ./pifm \"" + newfilenameraw + ".wav" + "\" 97.7"

	broadcast = "sox \"" + filename + "\" -t mp3 - channels 1 | avconv -v fatal -i pipe:0 -ac 1 -ar 22050 -b 352k -f wav - | sudo ./pifm2 - " + FREQUENCY
	#print broadcast
	player = subprocess.call(broadcast, shell=True)


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
