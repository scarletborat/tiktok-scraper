from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = "https://snaptik.app/"
input_selector = '.link-input'
button_selector = '.button-go'  
download_button_selector = '.video-links a'

def process_video(link_to_video):
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

process_video('https://www.tiktok.com/@akodor2012/video/7233034333999680811')
