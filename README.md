# Tiktok scraper

## 1. Tiktok scraper Description

The Tiktok Scraper application is designed to automate the process of extracting and processin tiktok video links and their associated titles from a specified TikTok page and removing watermarks. Once these tiktok video links are retrieved, the application downloads them remove watermark and stores them in a specified directory. The scraper is built using the Selenium WebDriver and the chandgable converters 'video_converters.py' for video processin.

## 2. Class Parameters

The `Scraper` class takes the following parameters:

| Parameter | Default Value | Description |
| --- | --- | --- |
| `source_url` | N/A | The URL of the TikTok page to scrape. |
| `root_element_selector` | '.tiktok-x6y88p-DivItemContainerV2' | The CSS selector of the root element. |
| `source_video_url_selector` | '.tiktok-yz6ijl-DivWrapper a' | The CSS selector of the video URL. |
| `source_video_title_selector` | '.tiktok-j2a19r-SpanText' | The CSS selector of the video title. |
| `user_agent` | 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36' | The User-Agent string to send with requests. |
| `is_scroll_to_bottom` | True | Whether to scroll to the bottom of the page. |
| `download_directory` | 'videos' | The directory where downloaded videos are saved. |
| `scroll_pause_time` | 3 | The time to pause between scrolling actions. |

## 3. Main Processing Stages

The main processing stages of the scraper are:

1. Initialization: Set up the scraper with the provided parameters.
2. Element Extraction: Find the root elements in the page and extract video URLs and titles.
3. Video Conversion and Download: For each extracted video URL, convert it and download the resulting video file.

## 4. How to Use It

Here's an example of how you can use this scraper:

```python
source_url = 'https://www.tiktok.com/your_channel'
scraper = Scraper(source_url)
scraper.process()
```

## 5. How to override video converter

Video converter implementation should obey contract wher input parameter is url to the tiktok video, return value is url to processed video

```python
from tiktok_scraper import Scraper

class SubScraper(Scraper):
    def convert_video(self, video_url):
      # Your converter implementation

source_url = 'https://www.tiktok.com/your_channel'
scraper = Scraper(source_url)
scraper.process()
```
For more details 'override-video-convertion-method.example.py'

## 5. Ethical aspect of web scraping

It is crucial to respect website owners' terms of service, adhere to any applicable laws and regulations, and obtain proper authorization if required. Additionally, it is recommended to use web scraping tools and scripts for informational or educational purposes only, ensuring that the collected data is used in a legal and responsible manner.