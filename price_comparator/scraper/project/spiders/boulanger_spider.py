import scrapy
from ..project.items import ProductItem
class BoulangerSpider(scrapy.Spider):
    name = "boulanger"    
    start_urls = ["https://www.boulanger.com/c/gros-electro-menager#tr=electromenager"]

    def parse(self, response):
        for product in response.css(".product-list-item"):
            item = ProductItem()            
            item['name'] = product.css(".product-title::text").get()
            item['price'] = product.css(".product-price strong::text").get()
            item['link'] = response.urljoin(product.css("a::attr(href)").get())
            item['site'] = "Boulanger"
            yield item