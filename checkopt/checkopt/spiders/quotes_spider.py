import scrapy
from scrapy.http import FormRequest  
from ..items import CheckoptItem
from pync import Notifier

RECEIPT_NUMBER = 'YSC1990XXXXXX'

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['uscis.gov']
    start_urls = ['https://egov.uscis.gov/casestatus/landing.do']   
 
    def parse(self, response): 
        return FormRequest.from_response(response,
                                        formdata={"appReceiptNum": RECEIPT_NUMBER},
                                        callback=self.CheckOptResponse)

    def CheckOptResponse(self, response):      
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)       
        item = CheckoptItem()
        item['status_headline'] = response.xpath('/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/h1/text()').extract()
        states_headline = ''.join(item['status_headline'])
        Notifier.notify(states_headline)