import scrapy
from satofuru.items import City

class NamesSpider(scrapy.Spider):
    """
    市町村名を取得する
    """
    name = 'names'
    allowed_domains = ['https://www.satofull.jp/products/list.php?s5=1&cnt=60&p=1']
    start_urls = ['https://www.satofull.jp/products/list.php?s5=1&cnt=60&p=1/']

    def parse(self, response):
        item = City()
        txts = response.css('.SideBox__tree')[3].css('a::text')
        
        for txt in txts:
            city = txt.get()
            item["city"] = city.split("（")[0]
            yield item
    

