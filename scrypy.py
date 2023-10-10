import requests
import re
import math
from bs4 import BeautifulSoup
import pandas as pd
import selenium


url =  "https://www.zapimoveis.com.br/venda/apartamentos/mg+uberlandia/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
}

site = requests.get (url, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")
imoveis = soup.find_all('div', class_="i-card__content")
ultima_pagina = soup.find('span', class_="pagination__next")



