import speech_recognition as sr
import openai
import pyttsx3

def mainfunction(source):
	jarvis_voice("How may I help you?")
	audio = r.listen(source)
		
	try:
		print("Please wait, generating result")
		text = r.recognize_google(audio)
		openAiRecognize(text)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		#jarvis_voice("I am sorry, I don't think I understand you.")
	
	except sr.RequestError as e:
		print("Could not request results from Google ech Recognition service; {0}".format(e))
		#jarvis_voice("I am sorry, I don't think I understand you.")]
def openAiRecognize(user_query):
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_query,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6
    )
    print("You said: " + user_query)
    jarvis_voice("You asked me " + user_query)
    print("Answer: " + response.choices[0].text)
    jarvis_voice(response.choices[0].text)

def jarvis_voice(data):
    engine.setProperty('voice', 'com.apple.voice.compact.en-GB.Daniel')
    engine.setProperty('rate', 190)
    engine.say(data)
    engine.runAndWait()

if __name__ == "__main__":
	mic_name = "HDAUDIO\FUNC_01&VEN_111D&DEV_76D9&SUBSYS_103C183F"
	sample_rate = 48000
	chunk_size = 2048
	r = sr.Recognizer()
	mic_list = sr.Microphone.list_microphone_names()

	device_id = 1
	engine = pyttsx3.init()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		while 1:
		    mainfunction(source)