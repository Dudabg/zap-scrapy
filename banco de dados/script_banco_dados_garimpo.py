import mysql.connector
import pandas as pd
import datetime

conexao = mysql.connector.connect(
    host='193.203.183.54',
    user='perdigueiro',
    password='V3nc3d0r3s@23',
    database='perdigueiro',
)

cursor = conexao.cursor()

df = pd.read_csv('banco de dados\\imoveis.csv')
id = df['id'].copy()
url = df['url'].copy()
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for i in range(0, 3511):
    idambiente = f'{id[i]/1000}'
    ambiente = 'ZAP_IMOVEIS'
    caminho = f'{url[i]}'
    criadopor = 'Duda'
    criadoem = time
    alteradopor = 'Duda'
    alteradoem = time

    comando_sql = f"INSERT INTO garimpo ( idambiente, ambiente, caminho, criadopor, criadoem, alteradopor, alteradoem) VALUES ('{idambiente}', '{ambiente}', '{caminho}', '{criadopor}', '{criadoem}', '{alteradopor}',' {alteradoem}')"
    cursor.execute(comando_sql)
    

    conexao.commit()
conexao.close()
