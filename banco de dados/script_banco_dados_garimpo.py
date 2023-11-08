import mysql.connector
import pandas as pd
import datetime

conexao = mysql.connector.connect(
    host='uberlandiaonline.com.br',
    user='uberla14_perdigueiro',
    password='V3nc3d0r3s@23',
    database='uberla14_perdigueiro',
)

cursor = conexao.cursor()

df = pd.read_csv('banco de dados\\imoveis_zap.csv')
id_ambiente = df['id_ambiente'].copy()
url_anunciante = df['url_anunciante'].copy()
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for i in range(len(df)):
    idambiente = f'{id_ambiente[i]}'
    ambiente = 'ZAP_IMOVEIS'
    caminho = f'{url_anunciante[i]}'
    criadopor = 'Duda'
    criadoem = time
    alteradopor = 'Duda'
    alteradoem = time

    comando_sql = f"INSERT INTO garimpo ( idambiente, ambiente, caminho, criadopor, criadoem, alteradopor, alteradoem) VALUES ('{idambiente}', '{ambiente}', '{caminho}', '{criadopor}', '{criadoem}', '{alteradopor}',' {alteradoem}')"
    cursor.execute(comando_sql)
    

    conexao.commit()
conexao.close()
