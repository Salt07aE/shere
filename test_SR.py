import speech_recognition
r = speech_recognition.Recognizer()
with speech_recognition.AudioFile("oki.wav") as source:
    audio = r.record(source)
print(r.recognize_google(audio, language='ja-JP'))
