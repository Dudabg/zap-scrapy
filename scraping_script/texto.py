import scrapy
import jsonhttps_url = 'https://pastebin.com`
 
class OlxHouses(scrapy.Spider):
    name = 'olx'
 
    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'AUTOTHROTTLE_ENABLED': True,
    }
 
    def start_requests(self):
        for page in range(1,101):
            yield scrapy.Request(f'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?o={page}')
 
    def parse(self, response, **kwargs):
        html = json.loads(response.xpath('//script[@id="__NEXT_DATA__"]/text()').get())
        houses = html.get('props').get('pageProps').get('ads')
        for house in houses:
            yield{
                'title' : house.get('title'),
                'price' : house.get('price'),
                'locations' : house.get('location')
            }
 
 