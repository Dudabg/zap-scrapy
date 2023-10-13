import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

apartamentos_totais = []

for pagina in range(1, 101):  # Loop de 1 a 100
    url = f'https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/?pagina={pagina}'  
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    apartamentos = soup.find_all('div', class_='l-card__content')
    
    for apartamento in apartamentos:
        detalhes_apartamento = {}
        
        # Extrair informações do imóvel
        titulo_element = apartamento.find('div', class_='header__wrapper').find('a', class_='js-card-title')
        titulo = titulo_element.text.strip() if titulo_element else 'N/A'
        
        preco_element = apartamento.find('div', class_='listing-price')
        preco = preco_element.text.strip() if preco_element else 'N/A'
        
        localizacao_element = apartamento.find('h2', class_='l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-medium card__address')
        localizacao = localizacao_element.text.strip() if localizacao_element else 'N/A'
        
        descricao_element = apartamento.find('p', class_='l-text l-u-color-neutral-44 l-text--variant-body-small l-text--weight-regular card__description')
        descricao = descricao_element.text.strip() if descricao_element else 'N/A'

        tamanho_element = apartamento.find('p', class_='l-text l-u-color-neutral-28 l-text--variant-body-small l-text--weight-regular card__amenity')
        tamanho = tamanho_element.text.strip() if tamanho_element else 'N/A'

        anunciante_element = apartamento.find('ul', class_='postlead-modal__code')
        anunciante = anunciante_element.text.strip() if anunciante_element else 'N/A'

        # Adicionar informações ao dicionário
        detalhes_apartamento['Titulo'] = titulo
        detalhes_apartamento['Preco'] = preco
        detalhes_apartamento['Localizacao'] = localizacao
        detalhes_apartamento['Descricao'] = descricao
        detalhes_apartamento['Tamanho'] = tamanho
        detalhes_apartamento['Anunciante'] = anunciante
        
        # Adicionar o dicionário à lista de imóveis totais
        apartamentos_totais.append(detalhes_apartamento)


