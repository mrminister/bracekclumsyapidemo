import scrapy
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

indices = range(1,51,1)
master_pages = [f'https://www.brigada.sk/brigady-na-slovensku?page={i}#zoznam' for i in indices]
full_links_path = r'C:\Users\jacoo\OneDrive\Desktop\jobs_scraping\utils\all_links.csv'

class QuotesSpider(scrapy.Spider):
    name = "links"

    def start_requests(self):
        urls = master_pages
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        path = "//a/@href"#/@href"#'/html/body/div[4]/div/div[2]/div/div[1]/div[8]/div[3]/div[1]/div[2]'
        sub_links = response.xpath(path).getall()
        clean = ['https://www.brigada.sk'+s for s in sub_links if '/brigady-na-slovensku/' in s]

        new_records = pd.DataFrame({
            'job_link': clean
        })
        records = pd.read_csv(full_links_path)
        records = pd.concat([records, new_records],ignore_index = True)
        records.to_csv(full_links_path)