import pafy
import io,sys,os
import subprocess
import urllib
import json as simplejson


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
		if(a.bitrate=="128k"):
			break

	print audiostreams

	filename = audiostreams[i].download()
	print filename
	#player = subprocess.call(['cvlc',filename,'--play-and-exit'])
	player = subprocess.call("omxplayer -o local \"" + filename + "\"", shell=True)



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
