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

# Lista para armazenar detalhes dos apartamentos
apartamentos_totais = []

# Loop através das páginas de 1 a 100
for pagina in range(1, 3):
    # Construir a URL da página atual
    url = f'https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/?pagina={pagina}'

    # Abre a página que você deseja
    navegador.get(url)

    # Define o tempo de espera para Selenium
    wait = WebDriverWait(navegador, 20)

    # Agora você pode usar WebDriverWait para esperar que o elemento de interesse apareça antes de rolar a página
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'l-card__content')))

    # Obtém o conteúdo da página após rolar e espera para garantir que todos os apartamentos sejam carregados
    

    for i in range(0,6000):
            navegador.execute_script('window.scrollBy(0,54)')
            # Espera um curto período de tempo para permitir o carregamento do conteúdo
           



    # Obtém o conteúdo da página após rolar
    soup = BeautifulSoup(navegador.page_source, 'html.parser')

    # Encontra todos os apartamentos na página atual
    apartamentos = soup.find_all('div', class_='l-card__content')

    # Loop através dos apartamentos e extrai detalhes
    for apartamento in apartamentos:
        detalhes_apartamento = {}

    header_wrapper = apartamento.find('div', class_='header__wrapper')
    if header_wrapper:
        titulo_element = header_wrapper.find('a', class_='js-card-title')
        titulo = titulo_element.text.strip() if titulo_element else 'N/A'
    else:
        titulo = 'N/A'

    preco_element = apartamento.find('div', class_='listing-price')
    preco = preco_element.text.strip() if preco_element else 'N/A'

    localizacao_element = apartamento.find('h2', class_='l-text l-u-color-neutral-28 l-text--variant-heading-small l-text--weight-medium card__address')
    localizacao = localizacao_element.text.strip() if localizacao_element else 'N/A'

    descricao_element = apartamento.find('p', class_='l-text l-u-color-neutral-44 l-text--variant-body-small l-text--weight-regular card__description')
    descricao = descricao_element.text.strip() if descricao_element else 'N/A'

    tamanho_element = apartamento.find('p', class_='l-text l-u-color-neutral-28 l-text--variant-body-small l-text--weight-regular card__amenity')
    tamanho = tamanho_element.text.strip() if tamanho_element else 'N/A'

    anunciante_element = apartamento.find('div', class_='publisher__title heading-small align-left')
    anunciante = anunciante_element.text.strip() if anunciante_element else 'N/A'

    telefone_element = apartamento.find('a', class_='publisher__phone js-publisher-phone link link-cta link--bold')
    telefone = telefone_element.text.strip() if anunciante_element else 'N/A'

    codigo_element = apartamento.find('ul', class_='postlead-modal__code')
    codigo = codigo_element.text.strip() if anunciante_element else 'N/A'


    # Adicionar informações ao dicionário
    detalhes_apartamento['Titulo'] = titulo
    detalhes_apartamento['Preco'] = preco
    detalhes_apartamento['Localizacao'] = localizacao
    detalhes_apartamento['Descricao'] = descricao
    detalhes_apartamento['Tamanho'] = tamanho
    detalhes_apartamento['Anunciante'] = anunciante
    detalhes_apartamento['Telefone'] = telefone
    detalhes_apartamento['Codigo'] = codigo
    

    # Adicionar o dicionário à lista de imóveis totais
    apartamentos_totais.append(detalhes_apartamento)

print(apartamentos_totais)

# Cria um DataFrame com os dados extraídos
df = pd.DataFrame(apartamentos_totais)

# Salva o DataFrame em um arquivo Excel
df.to_excel('C:/Users/HP/Desktop/zap-scrapy/scraping_script/apartamentos.xlsx', index=False)

print('Dados exportados para apartamentos.xlsx com sucesso!')





        data_list.append(data) #adicionando o dicionário na lista
    except:
      time.sleep(100)

      df = pd.DataFrame(data_list) #criando o dataframe
      df.to_excel('imoveis_teste.xlsx', index=False) #salvando o dataframe em um arquivo

