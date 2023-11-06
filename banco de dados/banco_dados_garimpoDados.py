import mysql.connector
import pandas as pd
import datetime

# Configurando as informações de conexão
conexao = mysql.connector.connect(
    host='193.203.183.54',
    user='perdigueiro',
    password='V3nc3d0r3s@23',
    database='perdigueiro',
)

# Conectando ao banco de dados
connection = mysql.connector.connect(host=193.203.183.54, port=port, database=perdigueiro, user=perdigueiro, password=password)

# Criando um cursor
cursor = connection.cursor()

# Obtendo o último id garimpo
cursor.execute("SELECT id_garimpo FROM garimpo ORDER BY id_garimpo DESC LIMIT 1")
last_id_garimpo = cursor.fetchone()[0]

# Abrindo a planilha
with open("data.csv", "r") as f:
    for line in f:
        # Separando os dados da linha
        chave, valor = line.split(",")

        # Inserindo os dados na tabela
        cursor.execute(
            "INSERT INTO garimpo_dados (id_garimpo, chave, valor) VALUES (%s, %s, %s)",
            (last_id_garimpo, chave, valor),
        )

# Confirmando as alterações
connection.commit()

# Fechando a conexão
cursor.close()
connection.close()

