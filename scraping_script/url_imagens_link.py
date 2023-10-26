import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

url = 'https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

data_list = []
index = 10

for j in range(1, 10): 
    for i in range(0, 6):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        div_tags = soup.find_all('li', class_='js-carousel-item carousel__item')

        img_urls = []
        for div_tag in div_tags:
            img_tag = div_tag.find('img').get('src')  
            if img_tag and 'src' in img_tag.attrs:
                img_urls.append(img_tag['src'])  

        for img_url in img_urls:
            print(img_url)

            data = {
                'url_imagens': img_url
            }
            data_list.append(data)

# Fora do loop, após terminar de coletar todas as URLs de imagens
# df = pd.DataFrame(data_list)
# df.to_excel('imoveis.xlsx', index=False)


df=pd.read_excel('imoveis.xlsx')
lista_link =df ('url_imagens').copy()
lista_imoveis= []