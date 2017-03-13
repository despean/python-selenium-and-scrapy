






import scrapy

class myspider(scrapy.Spider):
    name = 'uscraping'
    start_urls =['http://www.dmoz.org/Computers/Programming/Languages/Python/Books','http://www.dmoz.org/Computers/Programming/Languages/Python/Resources']

    def parse(self, response):
        for elem in response.xpath('//div[@class="title-and-desc"]/a'):
            yield {
                'title':elem.xpath('div/text()').extract_first(),
                'Link': elem.xpath('@href').extract()
            }



