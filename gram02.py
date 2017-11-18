import os
import urllib.request
import scrapy

class MySpider(scrapy.spiders.Spider):
    name='Tobby'
    allowed_domians=['www.sdibt.edu.cn']
    start_urls=['http://www.sdibt.edu.cn/info/1026/11238.htm']

    def parse(self,response):
        self.dowloadWebpage(response)
        self.dowloadImages(response)

        hxs=scrapy.Selector(response)
        sites=hxs.xpath('//ul/li')
        for site in sites:
            link=site.xpath('a/@href').extract()[0]
            if link == '#':
                next_url=os.path.dirname(respomse.url)
                next_url += '/'+link
            else:
                next_url=link
            yield scrapy.Request(url=next_url,callback=self.parse_item)

    def parse_item(self,respose):
        self.dowloadWbepage(response)
        self.dowloadImages(response)
    def dowloadImages(self,response):
        hxs=scrapy.Selector(response)
        images=hxs.xpath('//img/@src').extract()
        for image_url in images:
            imageFilename=image_url.split('/')[-1]
            if os.path.exists(imageFilename):
                continue
            if iamge_url.startswith('..'):
                iamge_url=os.path.dirname(response.url)+'/'+image_url
                fp=urlib.request.urlopen(image_url)
                with open(imageFilename,'wb')as f:
                    f.write(fp.read())
                fp.close
    def dowloadWepage(self,response):
        filename=response.url.split('/')[-1]
        with open(filename,'wb')as f:
            f.write(response.body)
    
