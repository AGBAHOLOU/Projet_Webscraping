import scrapy
from ..items import ProductItem
class AmazonSpider(scrapy.Spider):
    name = "amazon"    
    start_urls = ["https://www.amazon.fr/s?k=%C3%A9lectrom%C3%A9nager&crid=2022MTZC24UWT&sprefix=%C3%A9lectrom%C3%A9%2Caps%2C573&ref=nb_sb_ss_ts-doa-p_1_9"]

    def parse(self, response):
        for product in response.css(".s-main-slot .s-result-item"):
            item = ProductItem()            
            item['name'] = product.css("h2 a span::text").get()
            item['price'] = product.css(".a-price-whole::text").get()
            item['link'] = response.urljoin(product.css("h2 a::attr(href)").get())
            item['site'] = "Amazon"
            yield item
 