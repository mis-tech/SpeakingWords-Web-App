from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from django.http import JsonResponse
import simplejson as json
import json
import jsonpickle

import os 




def Gallery(request):
	path="C:\\Program Files\\Sublime Text 3\\NewWorkingFYP\\SpeakingWords\\SpeakingWords\\media\\audio"
	aud_list = os.listdir(path)
	lenth=len(aud_list)
	#audio_list = jsonpickle.encode(aud_list)
	aud_list.reverse()
	return render(request, 'gallery.html',{'AudioFiles': aud_list})






