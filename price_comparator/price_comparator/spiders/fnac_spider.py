import scrapy
from ..items import ProductItem
class FnacSpider(scrapy.Spider):
    name = "fnac"    
    start_urls = ["https://www.fnac.com/Maison-Electromenager/shi181432/w-4#bl=Mmpem"]

    def parse(self, response):
        for product in response.css(".Article-item"):
            item = ProductItem()            
            item['name'] = product.css(".Article-title::text").get()
            item['price'] = product.css(".Article-price::text").get()
            item['link'] = response.urljoin(product.css("a.Article-titleLink::attr(href)").get())
            item['site'] = "Fnac"
            yield item
        
            