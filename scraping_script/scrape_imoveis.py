import requests
import json
import pandas as pd
from bs4 import BeautifulSoup  # Importe o BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

apartamentos_totais = []

url = 'https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/'

# Fazendo a requisição para a página
response = requests.get(url, headers=headers)

# Use o BeautifulSoup para analisar o conteúdo da página
soup = BeautifulSoup(response.content, 'html.parser')

# Encontre o script com os dados JSON no código-fonte da página
script_data = None
scripts = soup.find_all('script')
for script in scripts:
    if 'window.__INITIAL_STATE__' in str(script):
        script_data = script
        break

# Extraindo e analisando o JSON do script
if script_data:
    json_data = json.loads(script_data.string.split('window.__INITIAL_STATE__ = ')[1])
    imoveis = json_data['results']['listings']

    for imovel in imoveis:
        detalhes_imovel = {
            'Titulo': imovel['listing']['title'],
            'Preco': imovel['listing']['price']['price'],
            'Localizacao': imovel['listing']['address']['neighborhood'],
            'Descricao': imovel['listing']['description'],
            'Tamanho': imovel['listing']['usableAreas']
        }
        apartamentos_totais.append(detalhes_imovel)

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame(apartamentos_totais)

# Salvar o DataFrame em um arquivo Excel
df.to_excel('apartamentos.json.xlsx', index=False)

print('Dados exportados para apartamentos.json.xlsx com sucesso!')
