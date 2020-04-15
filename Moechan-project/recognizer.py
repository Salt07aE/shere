import speech_recognition as sr

class Recognizer():
    def main():
        sr_r = sr.Recognizer()
        mic = sr.Microphone()
        print("\n聞き取り中・・・")
        with mic as source:
            sr_r.adjust_for_ambient_noise(source)
            audio = sr_r.listen(source)
            
        print ("解析中・・・")

        try:
            text = sr_r.recognize_google(audio, language='ja-JP' + "\n")

        except sr.UnknownValueError:
            print("音声を適切に解析できませんでした\n")
            text = "Error"
        except sr.RequestError as e:
            print("Google Speech Recognition service から結果をリクエストできませんでした; {0}\n".format(e))
            text = "Error"

        return text

if __name__ == "__main__":
    Recognizer.main()
