# -*- coding: utf-8 -*-
import scrapy


class SimpleproblemSpider(scrapy.Spider):
    name = "SimpleProblem"
    allowed_domains = ["community.topcoder.com"]
    start_urls = (
        'http://community.topcoder.com/tc?module=ProblemArchive',
    )

    def parse(self, response):

        trsls = response.css('body > table > tbody > tr > td.bodyText > table.paddingTable > tbody > tr:nth-child(1) > td > form > table:nth-child(11) > tbody > tr:nth-child(n+4)')
        for trsl in trsls:
            problem = ProblemItem()
            problem['name'] = trsl.xpath('//td[position()=2]/a/text()').extract()
            problem['link'] = trsl.xpath('//td[position()=2]/a//@href').extract()
            problem['match'] = trsl.xpath('//td[position()=3]/a/text()').extract()
            problem['category'] = trsl.xpath('//td[position()=6]/a/text()').extract()
            problem['match'] = trsl.xpath('//td[position()=3]/a/text()').extract()
            problem['match'] = trsl.xpath('//td[position()=3]/a/text()').extract()
            problem['match'] = trsl.xpath('//td[position()=3]/a/text()').extract()



