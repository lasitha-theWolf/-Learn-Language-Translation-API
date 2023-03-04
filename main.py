import googletrans
import speech_recognition as sr
import gtts
import playsound2

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'en'
out_lang = 'hi'
try:
    with sr.Microphone() as source:
        print('Speak now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass
translated = translator.translate(text, dest=out_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=out_lang)
converted_audio.save('romantic.mp3')
playsound2.playsound('romantic.mp3')

print(googletrans.LANGUAGES)

