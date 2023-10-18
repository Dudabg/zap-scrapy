import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

apartamentos_totais = []

for pagina in range(1, 101):  # Loop de 1 a 100
    url = f'https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/?pagina={pagina}'  
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    apartamentos = soup.find_all('div', class_="l-card__content")
    
    for apartamento in apartamentos:
        detalhes_apartamento = {}
        
        # Extrair informações do imóvel
        titulo = apartamento.find('section', class_='class="card__location')['title']
        preco = apartamento.find('div', class_='class="listing-price')['content']
        localizacao = apartamento.find('h2', class_='class="l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-medium card__address').text
        
        # Adicionar informações ao dicionário
        detalhes_apartamento['Titulo'] = titulo
        detalhes_apartamento['Preco'] = preco
        detalhes_apartamento['Localizacao'] = localizacao
        
        # Adicionar o dicionário à lista de imóveis totais
        apartamentos_totais.append(detalhes_apartamento)

# Exemplo de como acessar os dados extraídos
for apartamento in apartamentos_totais:
    print('Título:', apartamento['Titulo'])
    print('Preço:', apartamento['Preco'])
    print('Localização:', apartamento['Localizacao'])
    print('---')
