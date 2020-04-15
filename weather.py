import requests
from bs4 import BeautifulSoup

url = 'https://tenki.jp/forecast/3/23/4820/20214/'

r = requests.get(url)

bsObj = BeautifulSoup(r.content, "html.parser")

today = bsObj.find(class_="today-weather")
tomorrow = bsObj.find(class_="tomorrow-weather")
print("Pleas write 'today' or 'tomorrow'")
target_day = input()

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