import scrapy
from scrapy.spiders import CrawlSpider


class LoginSpiderSpider(CrawlSpider):
    name = 'login_spider'
    allowed_domains = ['github.com']
    # start_urls = ['https://github.com/login']

    def start_requests(self):
        yield scrapy.Request(url="https://github.com/login", callback=self.parse, dont_filter=True)

    def parse(self, response):
        authenticity_token = response.xpath('//*[@id="login"]/div[4]/form/input[1]/@value').extract_first()
        required_field = response.xpath('//*[@id="login"]/div[4]/form/div/input[9]/@name').extract_first()
        timestamp = response.xpath('//*[@id="login"]/div[4]/form/div/input[10]/@value').extract_first()
        timestamp_secret = response.xpath('//*[@id="login"]/div[4]/form/div/input[11]/@value').extract_first()
        form_data = {
            'commit': 'Sign in',
            'authenticity_token': authenticity_token,
            'login': 'youraccount',
            'password': 'yourpassword',
            'trusted_device': '',
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'unsupported',
            'return_to': 'https://github.com/login',
            'allow_signup': '',
            'client_id': '',
            'integration': '',
            required_field: '',
            'timestamp': timestamp,
            'timestamp_secret': timestamp_secret

        }
        print(form_data)
        yield scrapy.FormRequest(url="https://github.com/session", formdata=form_data, callback=self.fetch_profile)

    def fetch_profile(self, response):
        print("fetching profile...")
        yield scrapy.Request(url="https://github.com/vekaco", callback=self.verify_content)

    def verify_content(self, response):
        print("parsing item...")
        count = response.xpath('//span[@class="Counter"]/text()')
        print(count)




