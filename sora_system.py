import requests
import codecs
import lxml.html
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# メールアドレスとパスワードの指定
USER = "T119076"
PASS = "Q*7e!yCY"

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "username":USER,
    "password":PASS,
    "logintoken":"saKR2z6p8dWXnZvzsBXQEM8gAa8j6WED",
}

# action
url_login = "https://sus.mrooms.net/login/index.php"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

soup = BeautifulSoup(res.text,"html.parser")
content = soup.find(class_="tree_item hasicon")
dashboard_url = content.a.get("href")

if dashboard_url is None:
    print("マイページが取得できませんでした")
    quit()
print("ダッシュボード=",dashboard_url)

dash = session.get(dashboard_url)
#soup = BeautifulSoup(dash.text,"html.parser")
#kadai = soup.find_all(class_="tab-content")[0]
#print(kadai)
html = lxml.html.fromstring(dash.text)

timeline = html.xpath("/html/body/div[4]/div[1]/div/div/aside/div[1]/div[2]/ul/li/ul/li[1]/p/a/span")
#tl = timeline.text()

print(timeline)
############################################################################################################




############################################################################################################



print(dash, file=codecs.open('sora-html.txt', 'w', 'utf-8'))
#print(today.text, file=codecs.open('sora-html.html', 'w', 'utf-8'))

#if links is None:
#        print("マイページが取得できませんでした")
#        quit()
