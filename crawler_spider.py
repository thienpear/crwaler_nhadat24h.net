from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem

class CrawlerSpider(Spider):
    BASE_DOMAIN = "nhadat24h.net"
    BASE_URL_PATH = f"https://{BASE_DOMAIN}"
    name = "crawler"
    allowed_domains = [BASE_DOMAIN]
    num_of_pages_to_fetch = 3

    def __init__(self):
        self.start_urls = self.get_start_urls(self.num_of_pages_to_fetch)

    def get_start_urls(self, num_of_pages_to_fetch):
        return [f"{self.BASE_URL_PATH}/nha-dat-ban/page{i}" for i in range(1, num_of_pages_to_fetch + 1)]

    def parse(self, response):
        real_estates = Selector(response).css('div > div.pn1')

        for real_estate in real_estates:
            item = CrawlerItem()

            # Get estate's title
            item['Title'] = real_estate.css('a::attr(title)').get()
            # Get estate's URL
            item['URL'] = self.BASE_URL_PATH + real_estate.css('a::attr(href)').get()
            # Get estate's price
            item['Price'] = (real_estate.css('p:nth-child(n) > label.a-txt-cl1::text').get() or
                 real_estate.css('p:nth-child(n) > label.a-txt-cl1 > strong::text').get())
            # Get estate's square footage
            item['SquareFootage'] = real_estate.css('p:nth-child(n) > label.a-txt-cl2::text').get()
            # Get estate's location
            item['Location'] = real_estate.css('div.reviewproperty1 > label.rvVitri > span::text').get()
            # Get estate's access road width
            item['AccessRoadWidth'] = real_estate.css('div.reviewproperty1 > label:nth-child(n) > span:has(i.fa-road)::text').get()
            # Get estate's frontage width
            item['FrontageWidth'] = real_estate.css('div.reviewproperty1 > label:nth-child(n) > span:has(i.fa-arrows-alt)::text').get()
            # Get estate's direction
            item['Direction'] = real_estate.css('div.reviewproperty1 > label:nth-child(n) > span:has(i.fa-compass)::text').get()
            # Get estate's building floors
            item['BuildingFloors'] = real_estate.css('div.reviewproperty1 > label:nth-child(n) > span:has(i.fa-building)::text').get()
            # Get estate's car parking slots
            item['CarParkingSlots'] = real_estate.css('div.reviewproperty1 > label:nth-child(n) > span:has(i.fa-car)::text').get()
            # Get estate's bedrooms
            item['Bedrooms'] = real_estate.css('div.reviewproperty1 > label:nth-child(n) > span:has(i.fa-bed)::text').get()
            # Get estate's bathrooms
            item['Bathrooms'] = real_estate.css('div.reviewproperty1 > label:nth-child(n) > span:has(i.fa-bath)::text').get()
            # Get estate's description
            item['Description'] = real_estate.css('label.lb-des::text').get()
            # Get category
            item['Category'] = real_estate.css ('div.review1 > span:nth-child(1)::text').get()
            
    
        
            yield item