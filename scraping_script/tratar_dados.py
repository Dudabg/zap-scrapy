import re
import json

# 1. Seu script com os dados (substitua com seus dados reais)
script = """
[SEU SCRIPT AQUI]
"""

# 2. Defina seu padrão de expressão regular para encontrar os dados desejados
padrao_regex = r'SEU_PADRAO_REGEX_AQUI'
padrao = re.compile(padrao_regex)
resultados = padrao.findall(script)

# 3. Estruture os dados extraídos (substitua com a lógica específica do seu caso)
dados_extraidos = []
for resultado in resultados:
    # Processar resultado conforme necessário e adicionar à lista dados_extraidos
    # Exemplo de processamento: dados_extraidos.append(processar_resultado(resultado))
    dados_extraidos.append(resultado)

# 4. Converta os dados para o formato JSON
dados_json = json.dumps(dados_extraidos, indent=4)

# 5. Salve os dados JSON em um arquivo (opcional)
with open('dados.json', 'w') as arquivo:
    arquivo.write(dados_json)

# OU manipule os dados JSON diretamente no seu código
dados = json.loads(dados_json)
# Agora você pode acessar os dados como um objeto Python
print(dados[0]['campo'])  # Substitua 'campo' pelo nome real do campo que você deseja acessar

# Lembre-se de personalizar SEU_PADRAO_REGEX_AQUI e a lógica de processamento de dados conforme necessário para o seu caso específico.
