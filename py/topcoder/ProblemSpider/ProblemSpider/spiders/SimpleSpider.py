# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ProblemSpider.items import *
class SimpleSpider(scrapy.Spider):
    name = "SimpleSpider"
    allowed_domains = ["community.topcoder.com"]
    start_urls = (
        'http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=1',
        'http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=201',
        'http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=401',
        'http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=601',
        'http://community.topcoder.com/tc?module=MatchList&sc=&sd=&nr=200&sr=801'
    )

    def parse(self, response):
        matchesls = response.xpath('//table[@class="stat"]/tr[@class="light"]')
        for sl in matchesls:
            matchItem = MatchItem()
            # print(sl.extract())
            matchItem['name'] = sl.xpath('td[1]/a/text()').extract()
            # print(sl.xpath('td[1]/text()').extract())
            matchItem['link'] = '{}{}'.format(u'http://community.topcoder.com', sl.xpath('td[1]/a//@href').extract_first())
            # print(matchItem['link'])
            tdsls = sl.xpath('td[position()>1]')
            tds = []
            for tdsl in tdsls:
                tds.append(tdsl.xpath('text()').extract_first(default='not-found'))
            if len(tds) < 12:
                tds.extend(['not-found']*(12-len(tds)))
            matchItem['time'] = tds[0]
            matchItem['competitorsTotal'] = tds[1]
            matchItem['competitorsDiv1'] = tds[2]
            matchItem['competitorsDiv2'] = tds[3]
            matchItem['submissionTotalDiv1'] = tds[4]
            matchItem['submissionAvgDiv1'] = tds[5]
            matchItem['challengeTotalDiv1'] = tds[6]
            matchItem['challengeAvgDiv1'] = tds[7]
            matchItem['submissionTotalDiv2'] = tds[8]
            matchItem['submissionAvgDiv2'] = tds[9]
            matchItem['challengeTotalDiv2'] = tds[10]
            matchItem['challengeAvgDiv2'] = tds[11]
            yield matchItem