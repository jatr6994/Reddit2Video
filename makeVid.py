import pyttsx3



def sentenceToAudio(sentence):  
	engine.say(sentence)
	engine.runAndWait()

	engine.setProperty('voice', voice.id)
	voices = engine.getProperty('voices')
	pyttsx3.init(driverName='sapi5') 



engine = pyttsx3.init()
sentenceToAudio('I love to test stuff')










# import pyttsx3
# from gtts import gTTS





# def sentenceToAudio(sentence):  
# 	tts = gTTS(text=sentence, lang='en')
# 	tts.save("saved_file.mp3")




# engine = pyttsx3.init(driverName='sapi5')
# sentenceToAudio('I love to test stuff')
