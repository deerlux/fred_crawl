# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from fred.items import FredItem

import os, re


class ScriptCrawlSpider(CrawlSpider):
    name = 'script_crawl'
    allowed_domains = ['www.fmwconcepts.com']
    start_urls = ['http://www.fmwconcepts.com/imagemagick/index.php']

    rules = (        
        Rule(LinkExtractor(restrict_xpaths='//table[@id="cat_table"]//td'), follow = True),
        Rule(LinkExtractor(restrict_xpaths='//a[text()="Download Script"]'), callback = 'parse_item'),
    )

    def parse_item(self, response):
        temp = response.body
        
        url_path, filename = os.path.split(response.url)
        
        dirname, scriptname = re.search('.+dirname=(.+)&scriptname=(.+)', filename).groups()
        
        dirname = os.path.join('./script',dirname)
        
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        
        file(os.path.join(dirname, scriptname), 'wb').write(temp)
        
        i = FredItem()        
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
