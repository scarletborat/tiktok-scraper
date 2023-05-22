# To use scraper create instance of scraper, pass necessary parameters
# and call process method

from tiktok_scraper import Scraper

scraper = Scraper(source_url='https://www.tiktok.com/@pkllipe')
scraper.process()