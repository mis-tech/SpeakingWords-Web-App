import requests
import urllib.request as urllib2
from urllib.request import urlopen
from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect

# Create your views here.


def Search(request):
	videos = []
	msg=""
	def internet_on():
		try:
			urllib2.urlopen('http://216.58.192.142', timeout=1)
			return True
		except urllib2.URLError as err:
			msg="No internet connection"
			return False
	if internet_on():
		if request.method == 'POST':
			search_url = 'https://www.googleapis.com/youtube/v3/search'
			video_url = 'https://www.googleapis.com/youtube/v3/videos'

			search_params = {
				'part' : 'snippet',
				'q' : request.POST['search'],
				'key' : settings.YOUTUBE_DATA_API_KEY,
				'maxResults' : 9,
				'type' : 'video'
			}

			r = requests.get(search_url, params=search_params)

			results = r.json()['items']

			video_ids = []
			for result in results:
				video_ids.append(result['id']['videoId'])


			if request.POST['submit'] == 'lucky':
				n="embed/"
				return redirect(f'https://www.youtube.com/{n}{ video_ids[0] }')

			video_params = {
				'key' : settings.YOUTUBE_DATA_API_KEY,
				'part' : 'snippet,contentDetails',
				'id' : ','.join(video_ids),
				'maxResults' : 9
			}

			r = requests.get(video_url, params=video_params)

			results = r.json()['items']
			n="embed/"

			for result in results:
				video_data = {
					'title' : result['snippet']['title'],
					'id' : result['id'],
					'url' : f'https://www.youtube.com/{n}{ result["id"] }',
					'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds()//60),
					'thumbnail' : result['snippet']['thumbnails']['high']['url']
				}

				videos.append(video_data)

		
		context = {
			'videos' : videos
		}

		return render(request, 'search.html', context)

	else:
		return render(request, "error.html",{'msg':msg})
