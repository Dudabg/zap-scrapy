import pandas as pd
import mysql.connector
import datetime

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host='193.203.183.54',
    user='perdigueiro',
    password='V3nc3d0r3s@23',
    database='perdigueiro',
)

# Ler a planilha
cursor = conexao.cursor()

df = pd.read_csv('banco de dados\\imoveis.csv')
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Obter o último idgarimpo da tabela garimpo
cursor.execute(comando)
conexao.commit()
comando = """ SELECT LAST_INSERT_ID();"""
cursor.execute(comando)
id_garimpo = cursor.fetchall()
id_garimpo = id_garimpo[0][0]

# Inserir dados na tabela garimpo_dados
cursor = conexao.cursor()

for i in range(0, 3511):
    idgarimpo = id_garimpo
    chave =
    valor = 
    criadopor = 'Duda'
    criadoem = time
    alteradopor = 'Duda'
    alteradoem = time

    
    
    
    comando_sql = f'INSERT INTO garimpo_dados (idgarimpodados, idgarimpo, chave, valor, criadopor, criadoem, alteradopor, alteradoem) VALUES ('{idgarimpo}', '{chave}', '{valor}', '{criadopor}', '{criadoem}', '{alteradopor}',' {alteradoem}')'
    cursor.execute(comando_sql)     


    conexao.commit()
    cursor.close()

conexao.close()

print('Dados inseridos com sucesso na tabela garimpo_dados.')
