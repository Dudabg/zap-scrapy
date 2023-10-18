import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  # Importe a classe Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializa o driver do Chrome sem exibir a interface gráfica
chrome_options = Options()  # Use Options() aqui
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)  # Passe as opções como argumento

# Abre a página
driver.get('https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/?pagina=1')

# Espera até que os apartamentos sejam carregados (você pode ajustar o tempo conforme necessário)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'l-card__content')))

# Rola a página para baixo para carregar mais apartamentos (você pode ajustar o número de vezes conforme necessário)
for _ in range(3):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    # Espera um pouco após rolar para dar tempo de carregar mais apartamentos
    time.sleep(2)

# Obtém o conteúdo da página após rolar
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Encontra todos os apartamentos
apartamentos = soup.find_all('div', class_='l-card__content')

# Lista para armazenar detalhes dos apartamentos
apartamentos_totais = []

# Loop através dos apartamentos e extrai detalhes
for apartamento in apartamentos:
    detalhes_apartamento = {}
    # Extrai informações do imóvel
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

    anunciante_element = apartamento.find('div', class_='publisher__info')
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

# Fecha o navegador
driver.quit()

# Cria um DataFrame com os dados extraídos
df = pd.DataFrame(apartamentos_totais)

# Salva o DataFrame em um arquivo Excel
df.to_excel('apartamentos.xlsx', index=False)

print('Dados exportados para apartamentos.xlsx com sucesso!')
