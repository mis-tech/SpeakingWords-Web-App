from django.shortcuts import render
from django.http import HttpResponse



#For Translation
import goslate
from gtts import gTTS

#For Synonyms
import nltk 
from nltk.corpus import wordnet


#For internet connection checking
import urllib.request as urllib2

# Create your views here.


def Text_Processing(request):
	num=0
	if request.method == 'POST':
		text=""
		text=request.POST['Word']
		val=text
		msg=""
		message_class=''
		def internet_on():
			try:
				urllib2.urlopen('http://216.58.192.142', timeout=1)
				return True
			except urllib2.URLError as err:
				msg="No internet connection"
				return False

		if internet_on():
			tts = gTTS(text)
			tts.save('media/demoWord.mp3')
			if request.POST['submit'] == 'Synonym':
				val1=""
				val2=""
				val3=""
				val4=""
				synonyms = []
				antonyms = []
				for syn in wordnet.synsets(text): 
				    for l in syn.lemmas(): 
				        synonyms.append(l.name()) 
				        if l.antonyms(): 
				            antonyms.append(l.antonyms()[0].name())

				if len(synonyms) == 0:
					msg="No Results Please ReCheck Your Word's Spelling"
					message_class='is-danger'
					print(msg)
					print(msg)
					print(msg)
					return render(request, 'home.html',{'val':text, 'msg':msg, 'message_class':message_class})


				else:
					val1=synonyms[1]
					val2=synonyms[2]
					val3=synonyms[3]
					val4=synonyms[4]
					liss=[]
					liss=[val1,val2,val3,val4]

					return render(request, 'home.html', {'rzlt':liss, 'val':text, 'msg':msg, 'message_class':message_class})



			if request.POST['submit'] == 'Translation':
				gs = goslate.Goslate()
				translatedText = gs.translate(text,'ur')
				return render(request, 'home.html',{'rzlt':translatedText})

		else:
			return render(request, 'error.html',{'msg':msg})


			







				