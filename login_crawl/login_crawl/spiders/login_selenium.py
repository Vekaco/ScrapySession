import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver

class LoginSeleniumSpider(CrawlSpider):
    name = 'login_selenium'
    allowed_domains = ['github.com']
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--gpu-disable')
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    #start_urls = ['http://github.com/']
    def start_requests(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'referer': 'https://github.com'
        }
        cookies = self.get_cookies()
        yield Request(url="https://github.com/vekaco", headers=headers, cookies=cookies, callback=self.parse, dont_filter=True)

    # fill login info in selenium and get the login cookies
    def get_cookies(self):
        self.driver.get(url='https://github.com/login')
        self.driver.find_element(by='xpath', value='//*[@id="login_field"]').send_keys('youraccount')
        self.driver.find_element(by='xpath', value='//*[@id="password"]').send_keys('yourpassword')
        self.driver.find_element(by='xpath', value='//*[@id="login"]/div[4]/form/div/input[12]').click()
        self.driver.get(url='https://github.com/vekaco')
        logined = self.driver.current_url
        self.log('login to ' + logined)
        cookies = {}
        if logined == "https://github.com/vekaco":
            cookies_list = self.driver.get_cookies()
            # self.log(cookies_list)
            cookies = {dict['name']: dict['value'] for dict in cookies_list}
            return cookies

    def parse(self, response, **kwargs):
        self.log("parse profile items...")
        counter = response.xpath('//span[@class="Counter"]/text()')
        self.log(counter)








    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
