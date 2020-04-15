import speech_recognition as sr
import requests
import trpg
from bs4 import BeautifulSoup


print("1")
url = 'https://tenki.jp/forecast/3/23/4820/20214/'
print("2")
r = requests.get(url)

sr_r = sr.Recognizer()
mic = sr.Microphone()
print("3")
bsObj = BeautifulSoup(r.content, "html.parser")
print("4")
today = bsObj.find(class_="today-weather")
tomorrow = bsObj.find(class_="tomorrow-weather")

while True:
    print("Say something ...")

    with mic as source:
        sr_r.adjust_for_ambient_noise(source) #雑音対策
        audio = sr_r.listen(source)

    print ("Now to recognize it...")

    try:
        print(sr_r.recognize_google(audio, language='ja-JP'))

        #"今日"の天気
        if sr_r.recognize_google(audio, language='ja-JP') == "今日の天気" :
            print("今日の天気を検索します")
            weather = today.p.string
            temp = today.div.find(class_="date-value-wrap").find_all("dd")
            
            temp_max = temp[0].span.string
            temp_min = temp[2].span.string

            print("天気:{}".format(weather))
            print("最高気温:{}".format(temp_max))
            print("最低気温:{}".format(temp_min))

            continue

        if sr_r.recognize_google(audio, language='ja-JP') == "TRPG" :
            trpg.main()
            continue

        # "ストップ" と言ったら音声認識を止める
        if sr_r.recognize_google(audio, language='ja-JP') == "ストップ" :
            print("ストップ")
            break

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))