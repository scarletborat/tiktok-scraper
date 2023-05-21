from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup

def snaptik_converter(link_to_video):
    url = "https://snaptik.app/"
    input_selector = '.link-input'
    button_selector = '.button-go'  
    download_button_selector = '.video-links a'

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # 1. Open URL in Selenium
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # 2. Find input, put value
    input_element = driver.find_element(By.CSS_SELECTOR, input_selector)
    input_element.send_keys(link_to_video)
    time.sleep(5)

    # 3. Find button and click
    button_element = driver.find_element(By.CSS_SELECTOR, button_selector)
    button_element.click()
    time.sleep(5)

    # 4. Find link and retrieve the URL
    link_element = driver.find_element(By.CSS_SELECTOR, download_button_selector)
    link_url = link_element.get_attribute("href")
    return link_url

    # driver.quit()

snaptik_converter('https://www.tiktok.com/@akodor2012/video/7233034333999680811')

def ssstik_converter(video_url):
    url = 'https://ssstik.io'
    form_selector = '.pure-form'
    name_attribute = 'include-vals'
    download_link_selector = '.without_watermark'

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # 1. Open URL in Selenium
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)

    # 2. Find input, put value
    form = driver.find_element(By.CSS_SELECTOR, form_selector)
    token = form.get_attribute(name_attribute)

    session = requests.Session()
    session.get(url)
    
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

    token_key, token_value = token.replace("'", "").split(':')

    data = {
        'id': video_url,
        'locale': 'en',
        token_key: token_value
    }

    response = session.post(url + '/abc', headers=headers, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.select_one(download_link_selector)
    return link['href']
    
ssstik_converter('https://www.tiktok.com/@akodor2012/video/7233034333999680811')