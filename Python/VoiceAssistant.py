#simple voice assistant module
import pyttsx3
text_speech = pyttsx3.init()
voice = text_speech.getProperty('voices')
text_speech.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

def textToSpeech():
    currentVoice = text_speech.getProperty('voice')
    text_speech.say("hi, i am you voice assistant")
    text_speech.runAndWait()
    answer=input("what is your name: ")
    text_speech.say("good evening" + answer)
    text_speech.runAndWait()
    question = input("> ")
    if question == "what is your name":
        text_speech.say("my name is " + currentVoice.split(".")[-1])
        text_speech.runAndWait()
    elif question == "what are you doing":
        text_speech.say("i am helping people making calls, this mom person is very famous.")
        text_speech.runAndWait()
