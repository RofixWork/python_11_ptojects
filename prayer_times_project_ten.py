from pystyle import *
import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import time
Write.Print("[+] this program for prayer times\n", Colors.red, 0.01)

Write.Print(Box.DoubleCube("Example 10"), Colors.white, 0.01)


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'
url = "https://timesprayer.com/prayer-times-cities-morocco.html"

fetch_website_content = requests.get(url, headers={
    'user-agent': user_agent
})
soup = bs(fetch_website_content.text, "html.parser").find(class_="todayprayer").find_all('li')
prayers = ('Alfajr', 'Chourouq', 'Dhuhr', 'Asr', 'Maghrib', 'Ishae')

with tqdm(total=100) as tq:
    for i in range(100):
        time.sleep(0.01)
        tq.update(1)


Write.Print(Box.SimpleCube("\n[+] Prayer Times:\n"), Colors.blue, 0.01)
for index, prayer in enumerate(soup) :
    time = prayer.find("time")
    Write.Print(f"{prayers[index]}: {time.text}\n", Colors.green, 0.01)
