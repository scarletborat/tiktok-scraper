from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import urllib
import random
import os
from video_converters import ssstik_converter, snaptik_converter

class Scraper():
    def __init__(
            self,
            source_url,
            root_element_selector = '.tiktok-x6y88p-DivItemContainerV2',
            source_video_url_selector = '.tiktok-yz6ijl-DivWrapper a',
            source_video_title_selector = '.tiktok-j2a19r-SpanText',
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
            download_directory = 'videos',
            scroll_pause_time=3
        ):
        self.source_url = source_url
        self.source_video_url_selector = source_video_url_selector
        self.source_video_title_selector = source_video_title_selector
        self.root_element_selector = root_element_selector
        self.scroll_pause_time = scroll_pause_time
        self.download_directory = download_directory
        self.driver = None
        self.user_agent = user_agent
        self.create_directory()

    def create_directory(self):
        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

    def scroll_to_bottom(self, driver):
        screen_height = driver.execute_script("return window.screen.height")
        i = 1

        while True:
            driver.execute_script("window.scrollTo(0, {screen_height}*{i})".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(self.scroll_pause_time)
            scroll_height = driver.execute_script("return document.body.scrollHeight;")  
            if (screen_height) * i > scroll_height:
                break
    
    def convert_video(self, video_url):
        return snaptik_converter(video_url, self.driver)
    
    def download_video(self, url, id, title = 'title'):
        headers = { 'User-Agent': self.user_agent }
        req = urllib.request.Request(url, headers=headers)
        mp4File = urllib.request.urlopen(req)
        
        with open(f"{self.download_directory}/{id}-{title}.mp4", "wb") as output:
            while True:
                data = mp4File.read(4096)
                if data:
                    output.write(data)
                else:
                    break
    
    def process(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.source_url)

        # self.scroll_to_bottom(self.driver)
        
        root_elements = self.driver.find_elements(By.CSS_SELECTOR, self.root_element_selector)
        video_links = [{
            'url': root_element.find_element(By.CSS_SELECTOR, self.source_video_url_selector).get_attribute('href'),
            'title': root_element.find_element(By.CSS_SELECTOR, self.source_video_title_selector).text.strip()
        } for root_element in root_elements]

        print(video_links)

        for i, link in enumerate(video_links):
            download_link = self.convert_video(link['url'])
            self.download_video(download_link, id=i, title=link['title'])
            del video_links[i]
            time.sleep(random.randint(3, 5))
