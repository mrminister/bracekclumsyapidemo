import scrapy
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup

links = pd.read_csv(r'C:\Users\jacoo\OneDrive\Desktop\jobs_scraping\utils\all_links.csv')
job_details_path = r'C:\Users\jacoo\OneDrive\Desktop\jobs_scraping\utils\job_details.csv'
job_links = [l for l in links['job_link']]
data = []

class JobSpider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        urls = job_links

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, features="lxml")
        divs = soup.find_all("div", {"class": "val"})
        attrs = [d.get_text() for d in divs]
        row = [attrs[1], attrs[2], attrs[3], attrs[4], attrs[5]]

        record = {
            'date': [attrs[1]],
            'place': [attrs[2]],
            'rate': [attrs[3]],
            'time': [attrs[4]],
            'description': [attrs[5]]

        }
        new_records = pd.DataFrame(record)
        records = pd.read_csv(job_details_path)
        records = pd.concat([records, new_records], ignore_index=True)
        records.to_csv(job_details_path)
