import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


df= pd.read_excel('imoveis.xlsx')
print(df)
lista_links = df['url'].copy()

lista_id = df['id'].copy()
diretorio_pai = 'C:\\Users\\HP\\Desktop\\zap-scrapy\\fotos'
if(not os.path.exists(diretorio_pai)):
    os.makedirs(diretorio_pai)


for i in range(0,10):

    url =lista_links[i] 

    diretorio = diretorio_pai + "\\" + str(lista_id[i])
    if(not os.path.exists(diretorio)):
        os.makedirs(diretorio)


    

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'

    }


    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.content, 'html.parser')



    img = html.find_all('li', class_='js-carousel-item carousel__item')
    for j in range(0, len(img)):
        img_src= img[j].find('img').get('src').replace('400x180', '800x360')
        print(img_src)



        with open(diretorio+f'\\imagens{j}.jpg', 'wb') as imagem:
            resposta = requests.get(img_src, headers=headers)
            imagem.write(resposta.content)

