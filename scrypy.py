import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

apartamentos_totais = []
pagina = 1
for pagina in range(1, 101):  # Loop de 1 a 100
    url = f'https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/?pagina={pagina}'  
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    #apartamentos_totais #= soup
    print(site.status_code)
    apartamentos = soup.find_all('div', class_="l-card__content")
    print (len(apartamentos))   


    
