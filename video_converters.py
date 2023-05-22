from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def snaptik_converter(link_to_video, driver):
    url = "https://snaptik.app/"
    input_selector = '.link-input'
    button_selector = '.button-go'  
    download_button_selector = '.video-links a'

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")

    # 1. Open URL in Selenium
    # driver = webdriver.Chrome(options=chrome_options)
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
    
def ssstik_converter(video_url, driver):
    url = 'https://ssstik.io'
    input_selector = '#main_page_text'
    button_selector = '#submit'
    download_link_selector = '.without_watermark'

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")

    # 1. Open URL in Selenium
    driver = webdriver.Chrome() #options=chrome_options
    driver.get(url)

    # 2. Find input, put value
    input_element = driver.find_element(By.CSS_SELECTOR, input_selector)
    input_element.send_keys(video_url)
    time.sleep(1)

    # 3. Find button and click
    button_element = driver.find_element(By.CSS_SELECTOR, button_selector)
    button_element.click()
    time.sleep(5)

    # 4. Find link and retrieve the URL
    link_element = driver.find_element(By.CSS_SELECTOR, download_link_selector)
    link_url = link_element.get_attribute("href")
    driver.quit()

    return link_url
