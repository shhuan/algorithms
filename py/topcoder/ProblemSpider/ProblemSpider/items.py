# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProblemItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    match = scrapy.Field()
    category = scrapy.Field()
    div = scrapy.Field()
    level = scrapy.Field()
    submissions = scrapy.Field()
    correct = scrapy.Field()
    avgPts = scrapy.Field()
    statement = scrapy.Field()
    definition = scrapy.Field()
    constraint = scrapy.Field()
    examples = scrapy.Field()
    note = scrapy.Field()


class MatchItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    time = scrapy.Field()
    competitorsTotal = scrapy.Field()
    competitorsDiv1 = scrapy.Field()
    competitorsDiv2 = scrapy.Field()
    submissionTotalDiv1 = scrapy.Field()
    submissionAvgDiv1 = scrapy.Field()
    challengeTotalDiv1 = scrapy.Field()
    challengeAvgDiv1 = scrapy.Field()
    submissionTotalDiv2 = scrapy.Field()
    submissionAvgDiv2 = scrapy.Field()
    challengeTotalDiv2 = scrapy.Field()
    challengeAvgDiv2 = scrapy.Field()
    problems = scrapy.Field()
