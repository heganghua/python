# -*- coding: utf-8 -*-
import scrapy
import logging

class ExaSpider(scrapy.Spider):
    name = 'exa'
    allowed_domains = ['']
    start_urls = ['F:\HBT50.13.90SX.pdf']

    def parse(self, response):

        print(response.text)
        #logging.log('\n')
        #logging.log(logging.WARNING, response.text+"\n")

