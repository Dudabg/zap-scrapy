import requests
from bs4 import BeautifulSoup
import time ,re
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

try:
    # Inicializa o driver do Chrome sem exibir a interface gráfica
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    # Abre a página
    driver.get('https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/?pagina=1')

    
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

    # Cria um DataFrame com os dados extraídos
    df = pd.DataFrame(apartamentos_totais)

    # Salva o DataFrame em um arquivo Excel
    df.to_excel('apartamentos.xlsx', index=False)

    print('Dados exportados para apartamentos.xlsx com sucesso!')

except Exception as e:
    print('Ocorreu um erro:', e)

finally:
    # Fecha o navegador, mesmo se ocorrer uma exceção
    driver.quit()

    from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd

# Configura o serviço do ChromeDriver
servico = Service(ChromeDriverManager().install())

# Configura as opções do Chrome
opcoes = Options()

# Inicializa o driver do Selenium com o serviço e as opções configuradas
navegador = webdriver.Chrome(service=servico, options=opcoes)

# Abre a página que você deseja
navegador.get('https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia')

# Define o tempo de espera para Selenium
wait = WebDriverWait(navegador, 10)

# Agora você pode usar WebDriverWait para esperar que o elemento de interesse apareça antes de rolar a página
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'l-card__content')))

# Obtém o conteúdo da página após rolar e espera para garantir que todos os apartamentos sejam carregados
for _ in range(10):  # Rola 10 vezes para carregar mais conteúdo (ajuste conforme necessário)
    navegador.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    # Espera um curto período de tempo para permitir o carregamento do conteúdo
    time.sleep(2)

# Obtém o conteúdo da página após rolar
soup = BeautifulSoup(navegador.page_source, 'html.parser')

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

# Após extrair todos os dados necessários, você pode imprimir ou processar os resultados
print(apartamentos_totais)

# Fechar o navegador
navegador.quit()

# Cria um DataFrame com os dados extraídos
df = pd.DataFrame(apartamentos_totais)

# Salva o DataFrame em um arquivo Excel
df.to_excel('apartamentos.xlsx', index=False)

print('Dados exportados para apartamentos.xlsx com sucesso!')