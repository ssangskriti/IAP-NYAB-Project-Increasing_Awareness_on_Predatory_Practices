import scrapy
from ..items import ScholarItem

class SscholarSpider(scrapy.Spider):
    name = 'sscholar'
    # allowed_domains = ['omicsonline.org']
    start_urls = ['https://beallslist.net/standalone-journals/']
    
#     crawl author name, email, scholar
    def parse(self, response):
        
        items = ScholarItem()
        
        title = response.css('ul:nth-child(5) a:nth-child(1) ::text').extract()
        items['title'] = title
        # print(items)
        # yield{'titletext' : title}
        yield items