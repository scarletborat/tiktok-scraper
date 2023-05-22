from tiktok_scraper import Scraper
from video_converters import ssstik_converter

# Inherit from the parent class and override the method
class SubScraper(Scraper):
    # We receive a URL to a TikTok link as input 'video_url' which needs to be processed
    def convert_video(self, video_url):
        # Return a URL to the file that needs to be saved
      return ssstik_converter(video_url)

# By adhering to this contract, you can write any custom video processor.
# Please check 'video_converters.py' file for more details
scraper = Scraper(source_url='https://www.tiktok.com/@pkllipe', is_scroll_to_bottom=False)
scraper.process()