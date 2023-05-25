import requests
from bs4 import BeautifulSoup

URL = "https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20230101"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

musicList = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musicList:
    rank = music.select_one('.number').text[0:2].strip()
    title = music.select_one('.title.ellipsis').text.strip()
    artist = music.select_one('.artist').text
    print(rank + ' /', title + ' /', artist)
