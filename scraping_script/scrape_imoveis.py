import scrapy
import json

class ZapApartamentos(scrapy.Spider):
    name = 'zap'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 10,
    }
    
    def start_requests(self):
        yield scrapy.Request('https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/')

    def parse(self, response):
        json_data = response.css('script#__NEXT_DATA__::text').get()
        data = json.loads(json_data)
        ads = data['props']['pageProps']['ads']

        for ad in ads:
            yield {
                'titulo': ad['title'],
                'preco': ad['price'],
                'localizacao': ad['location']
            }

