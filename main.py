from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import random
import os

#change to your own
url = ""
video_selector = ".tiktok-yz6ijl-DivWrapper a"

def scroll_to_bottom(driver):
  scroll_pause_time = 1
  screen_height = driver.execute_script("return window.screen.height")
  i = 1

  while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i})".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break

def download_video(link):
    #change to your own
    cookies = {
        '_gid': 'GA1.2.454926346.1684539618',
        '__gads': 'ID=4561e7905edd8159-22bbabea56df0038:T=1684539618:RT=1684539618:S=ALNI_Ma5V0zO5SVL3vMVU-h7R8nu75Xyeg',
        '__gpi': 'UID=0000098dac1ca7e2:T=1684539618:RT=1684539618:S=ALNI_MbPm6VEuurO_L38BC4cOqPJEwCTYA',
        '__cflb': '02DiuEcwseaiqqyPC5qqJA27ysjsZzMZ78usYJKLbPy4f',
        '_gat_UA-3524196-6': '1',
        '_ga': 'GA1.2.1228860227.1684539618',
        '_ga_ZSF3D6YSLC': 'GS1.1.1684539618.1.1.1684540133.0.0.0',
    }

    #change to your own
    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://ssstik.io/en#google_vignette',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    
    #change to your own
    params = {
        'url': 'dl',
    }

    #change to your own
    data = {
        'id': link,
        'locale': 'en',
        'tt': 'aWJmNTlm',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    return response.text

def save_to_file(raw_html, id):
  download_directory = 'videos'
  soup = BeautifulSoup(raw_html, "html.parser")

  

  link = soup.a["href"]
  title = soup.p.getText().strip()

  if not os.path.exists(download_directory):
     os.makedirs(download_directory)
  
  mp4File = urlopen(link)
  with open(f"{download_directory}/{id}-{title}.mp4", "wb") as output:
      while True:
          data = mp4File.read(4096)
          if data:
              output.write(data)
          else:
              break

def process():
  driver = webdriver.Chrome()
  driver.get(url)
  time.sleep(10)

  scroll_to_bottom(driver)

  soup = BeautifulSoup(driver.page_source, 'html.parser')
  video_links = soup.select(video_selector)
  print(f"Number of links: {len(video_links)}")

  for i, link in enumerate(video_links):
    print(f"Downloading video number: {i}, link: {link['href']}")
    response_html = download_video(link['href'])
    time.sleep(random.randint(3, 5))
    save_to_file(response_html, i)
    time.sleep(10)
    
process()
