import trpg
import speech_recognition as sr

class recognition():

    def main():
        sr_r = sr.Recognizer()
        mic = sr.Microphone()
        while True:
            print("\n聞き取り中・・・")
            with mic as source:
                sr_r.adjust_for_ambient_noise(source) #雑音対策
                audio = sr_r.listen(source)
            
            print ("解析中・・・")

            try:

                print("You said : " + sr_r.recognize_google(audio, language='ja-JP' + "\n"))

                if sr_r.recognize_google(audio, language='ja-JP') == "TRPG" :
                    print("\nTRPGプログラム実行\n")
                    trpg.TRPG.main()
                    continue

                elif sr_r.recognize_google(audio, language='ja-JP') == "プログラムを終了" : 
                    print("\nプログラムを終了します。\n")
                    break

            except sr.UnknownValueError:
                print("音声を適切に解析できませんでした\n")
            except sr.RequestError as e:
                print("Google Speech Recognition service から結果をリクエストできませんでした; {0}\n".format(e))

recognition.main()