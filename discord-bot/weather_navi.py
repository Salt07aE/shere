import requests
from bs4 import BeautifulSoup

class Weather_navi():
    def __init__(self):
        self.url = 'https://tenki.jp/forecast/'
        self.r = requests.get(url)
        self.bsObj = BeautifulSoup(r.content, "html.parser")
        self.today = bsObj.find(class_="today-weather")
        self.tomorrow = bsObj.find(class_="tomorrow-weather")

    def weather():
        
        if target_day == "today":
            weather = today.p.string
            temp = today.div.find(class_="date-value-wrap").find_all("dd")
            print("今日の茅野市の天気をお知らせします。")

        elif target_day == "tomorrow":
            weather = tomorrow.p.string
            temp = tomorrow.div.find(class_="date-value-wrap").find_all("dd")
            print("明日の茅野市の天気お知らせします。")

else:
    print("error")

temp_max = temp[0].span.string
temp_min = temp[2].span.string

print("天気:{}".format(weather))
print("最高気温:{}".format(temp_max))
print("最低気温:{}".format(temp_min))

#print(temp)