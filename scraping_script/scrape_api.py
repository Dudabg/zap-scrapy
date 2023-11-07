import requests #blibioteca para fazer requisições do site
import json #blibioteca para transformar o json em um dicionario
import pandas as pd #biblioteca para manipular os dados
import time #biblioteca para manipular o tempo
import mysql.connector #blibioteca para conectar no banco de dados
import datetime #biblioteca para manipular o tempo


conexao = mysql.connector.connect(
          host='193.203.183.54',
          user='perdigueiro',
          password='V3nc3d0r3s@23',
          database='perdigueiro',
      )


payload = {} #dicionario vazio
headers = { #mostrar o navegador que nao é um robo
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
  'X-Domain': '.zapimoveis.com.br',
  'Cookie': '__cfruid=42d2a3aa93f72f906efb1036cc18470737173479-1698082455'
} #cabecalhos

data_list = [] #lista vazia

def traduz_palavra(palavra):
    dicionario_traducao = {
        'ADMINISTRATION': 'administracao',
        'ADULT_GAME_ROOM': 'salao_de_jogos',
        'ADULT_POOL': 'piscina_para_adultos',
        'AIR_CONDITIONING': 'ar_condicionado',
        'ALARM_SYSTEM': 'sistema_de_alarme',
        'ALUMINUM_WINDOW': 'janela_de_aluminio',
        'AMERICAN_KITCHEN': 'cozinha_americana',
        'ARMORED_SECURITY_CABIN': 'cabine_de_seguranca_blindada',
        'ARTESIAN_WELL': 'poco_artesiano',
        'BACKYARD': 'quintal',
        'BALCONY': 'sacada',
        'BAR': 'bar',
        'BARBECUE_BALCONY': 'sacada_com_churrasqueira',
        'BARBECUE_GRILL': 'churrasqueira',
        'BATHROOM_CABINETS': 'armarios_de_banheiro',
        'BATHTUB': 'banheira',
        'BEAUTY_CENTER': 'centro_de_beleza',
        'BEDROOM_WARDROBE': 'guarda_roupa_de_quarto',
        'BICYCLES_PLACE': 'bicicletario',
        'BLINDEX_BOX': 'box_de_blindex',
        'BUILTIN_WARDROBE': 'guarda_roupa_embutido',
        'BURNT_CEMENT': 'cimento_queimado',
        'CABLE_TV': 'tv_a_cabo',
        'CARETAKER': 'zelador',
        'CARETAKER_HOUSE': 'casa_do_zelador',
        'CHILDRENS_POOL': 'piscina_infantil',
        'CINEMA': 'cinema',
        'CLOSET': 'closet',
        'COLD_FLOOR': 'piso_frio',
        'CONCIERGE_24H': 'portaria_24_horas',
        'COOKER': 'fogao',
        'COPA': 'copa',
        'CORNER_PROPERTY': 'propriedade_de_esquina',
        'COVENTION_HALL': 'salao_de_festas',
        'COVERAGE': 'cobertura',
        'COVERED_POOL': 'piscina_coberta',
        'COWORKING': 'coworking',
        'DECK': 'deck',
        'DEPOSIT': 'deposito',
        'DIGITAL_LOCKER': 'cadeado_digital',
        'DINNER_ROOM': 'sala_de_jantar',
        'DISABLED_ACCESS': 'acesso_para_deficientes',
        'ECO_CONDOMINIUM': 'condominio_ecologico',
        'ECO_GARBAGE_COLLECTOR': 'coletor_de_lixo',
        'EDICULE': 'edicula',
        'ELECTRIC_GENERATOR': 'gerador_eletrico',
        'ELECTRONIC_GATE': 'portao_eletronico',
        'ELEVATOR': 'elevador',
        'EMPLOYEE_DEPENDENCY': 'quarto_de_servico',
        'ENTRANCE_HALL': 'hall_de_entrada',
        'ESSENTIAL_PUBLIC_SERVICES': 'servicos_publicos_essenciais',
        'EXTERIOR_VIEW': 'vista_exterior',
        'FENCE': 'cerca',
        'FIREPLACE': 'lareira',
        'FITNESS_ROOM': 'sala_de_ginastica',
        'FOOTBALL_FIELD': 'campo_de_futebol',
        'FRUIT_TREES': 'arvores_frutiferas',
        'FULL_CABLING': 'cabeamento_completo',
        'FURNISHED': 'piso_inteiro',
        'GAMES_ROOM': 'mobiliado',
        'GARAGE': 'sala_de_jogos',
        'GARAGE_BAND': 'garagem',
        'GARDEN': 'estudio_de_musica',
        'GATED_COMMUNITY': 'jardim',
        'GOLF_FIELD': 'condominio_fechado',
        'GOURMET_BALCONY': 'campo_de_golfe',
        'GOURMET_KITCHEN': 'sacada_gourmet',
        'GOURMET_SPACE': 'cozinha_gourmet',
        'GRASS': 'espaco_gourmet',
        'GREEN_SPACE': 'grama',
        'GUEST_PARKING': 'cascalho',
        'GYM': 'espaco_verde',
        'HEATED_POOL': 'estacionamento_para_visitantes',
        'HEATING': 'academia',
        'HIGH_CEILING_HEIGHT': 'piscina_aquecida',
        'HIKING_TRAIL': 'aquecimento',
        'HOME_CINEMA': 'pe_direito_alto',
        'HOME_OFFICE': 'pista_caminhada',
        'HOT_TUB': 'cinema_em_casa',
        'INDOOR_SOCCER': 'escritorio_em_casa',
        'INTEGRATED_ENVIRONMENTS': 'ofuro',
        'INTERCOM': 'futebol_de_salao',
        'INTERNET_ACCESS': 'ambientes_integrados',
        'KITCHEN': 'interfone',
        'KITCHEN_CABINETS': 'acesso_a_internet',
        'LAKE': 'cozinha',
        'LAKE_VIEW': 'armarios_de_cozinha',
        'LAMINATED_FLOOR': 'lago',
        'LARGE_KITCHEN': 'vista_para_o_lago',
        'LARGE_ROOM': 'piso_laminado',
        'LARGE_WINDOW': 'cozinha_ampla',
        'LAUNDRY': 'sala_ampla',
        'LAVABO': 'janela_grande',
        'LIBRARY': 'lavanderia',
        'LUNCH_ROOM': 'lavabo',
        'MASSAGE_ROOM': 'biblioteca',
        'MEETING_ROOM': 'sala_de_jantar',
        'MEZZANINE': 'sala_de_massagem',
        'MOUNTAIN_VIEW': 'mezanino',
        'NATURAL_VENTILATION': 'vista_para_a_montanha',
        'NEAR_ACCESS_ROADS': 'ventilacao_natural',
        'NEAR_HOSPITAL': 'proximo_a_vias_de_acesso',
        'NEAR_PUBLIC_TRANSPORT': 'proximo_a_hospital',
        'NEAR_SCHOOL': 'proximo_a_transporte_publico',
        
        }

        if palavra in dicionario_traducao:
            return dicionario_traducao [palavra]
        else:
            return palavra

    
    
   


index = 10 #indice inicial
for j in range(1, 2): #quantidade de paginas
  for i in range(0,6): #quantidade de apartamentos

    try: #tratamento de erros
      url = f'https://glue-api.zapimoveis.com.br/v2/listings?user=df22c4a3-badb-4bdd-bd04-f4dd06c95b90&portal=ZAP&includeFields=search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%2Cpage%2Cfacets%2CfullUriFragments%2Cdevelopments%28search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%29%2CsuperPremium%28search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%29%2Cschema&categoryPage=RESULT&developmentsSize=0&superPremiumSize=0&__zt=&business=SALE&parentId=null&listingType=USED&priceMin=1000000&addressCity=Uberl%C3%A2ndia&addressLocationId=BR%3EMinas+Gerais%3ENULL%3EUberlandia&addressState=Minas+Gerais&addressPointLat=-24.003067&addressPointLon=-46.417853&addressType=city&unitTypes=HOME&unitTypesV3=CONDOMINIUM&unitSubTypes=CONDOMINIUM&usageTypes=RESIDENTIAL&page=' + str(j) + '&size=15&from='+ str(index) +'&levels=CITY&ref='
      response = requests.request("GET", url, headers=headers, data=payload,timeout=2) 
      time.sleep(2)
      json = response.json()
      imoveis = json.get('search').get('result').get('listings') #pegando do json os dados que eu preciso
      index+=15 #aumentando o indice

      for i in imoveis: #percorrendo os imoveis

        try:
          id_ambiente = i.get('listing').get('id')                                       
          
        except:
          id_ambiente = None

        try:
          tipo_imovel = i.get('listing').get('unitTypes')
        except:
          tipo_imovel = None

        try:
          novo_usado = i.get('listing').get('listingType')
        except:
          novo_usado = None


        try:
          titulo = i.get('listing').get('title')
        except:
          titulo = None

        try:
          rua= i.get('listing').get('address').get('street')
        except:
          rua = None

        try:
          numero= i.get('listing').get('address').get('streetNumber')
        except:
          numero = None

        try:
          bairro= i.get('listing').get('address').get('neighborhood')
        except:
          bairro = None

        try:
          cidade = i.get('listing').get('address').get('city')
        except:
          cidade = None

        try:
          estado = i.get('listing').get('address').get('state')
        except:
          estado = None

        try:
          cep = i.get('listing').get('address').get('zipCode')
        except:
          cep = None

        try:
          preco = i.get('listing').get('priceSuggestion') [0].get('price')
        except:
          preco = None

        try:  
          area_privativa = i.get('listing').get('usableAreas')
        except:         
          area_privativa = None

        try:
          area_total = i.get('listing').get('totalAreas')
        except:
          area_total = None

        try:
          quartos = i.get('listing').get('bedrooms')
        except:
          quartos = None

        try:
          banheiros = i.get('listing').get('bathrooms')
        except:
          banheiros = None

        try:
          suites = i.get('listing').get('suites')
        except:
          suites = None

        try:
          garages = i.get('listing').get('parkingSpaces')
        except:
          garages = None

        try:
          andares = i.get('listing').get('floors')
        except: 
          andares = None

        try:
          iptu = i.get('listing').get('pricingInfos')[0].get('yearlyIptu')
        except:
          iptu = None

        try:
          taxa_condominio = i.get('listing').get('pricingInfos')[0].get('monthlyCondoFee')
        except:
          taxa_condominio = None

        try:
          descricao = i.get('listing').get('description')
        except:
          descricao = None

        try:
          caracteristicas = i.get('listing').get('amenities')
        except:
          caracteristicas = None

        try:
          data_anuncio = i.get('listing').get('createdAt')
        except:
          data_anuncio = None

        try:
          nome_anunciante= i.get('account').get('name')
        except:
          nome_anunciante = None

        try:
          cod_anunciante = i.get('account').get('id')
        except:
          cod_anunciante = None

        try:
          numero_anunciante_1 = i.get('listing').get('phones')
        except:     
          numero_anunciante_1 = None

        try:
          numero_anunciante_2 = i.get('listing').get('whatsappNumber')
        except:
          numero_anunciante_2 = None

        try:
          status = i.get('listing').get('status')
        except:
          status = None

        try:
          url_anunciante = i.get('link').get('href')
        except:
          url_anunciante = None
          url_link = "https://www.zapimoveis.com.br" + url
      






       #dados que nao sei se vai ser necessario
        
        try:
          atualizacao_data = i.get('listing').get('updatedAt')
        except:
          atualizacao_data = None

      
        try:
          portal = i.get('listing').get('portal')
        except:
          portal = None

        try:
          pais= i.get('listing').get('address').get('country')
        except:
          pais = None


        try:
          portal = i.get('listing').get('portal')
        except:
          portal = None

        try:
          atualizacao_data = i.get('listing').get('updatedAt')
        except:
          atualizacao_data = None

        
        
        #printando os dados na tela
        print(id_ambiente)
        print (tipo_imovel)
        print(novo_usado)
        print(titulo)
        print(rua)
        print(numero)
        print(bairro)
        print(cidade)
        print(estado)
        print(cep)
        print(preco)
        print(area_privativa)
        print(area_total)
        print(quartos)
        print(banheiros)
        print(suites)
        print(garages)
        print(andares)
        print(iptu)
        print(taxa_condominio)
        print(descricao)
        print(caracteristicas)
        print(data_anuncio)
        print(nome_anunciante)
        print(cod_anunciante)
        print(numero_anunciante_1)
        print(numero_anunciante_2)
        print(status)
        print(url_anunciante)

        
          

          
        data = { #criando um dicionário para pegar as informações
                'id_ambiente': id_ambiente,
                'tipo_imovel': tipo_imovel,
                'novo_usado': novo_usado,
                'titulo': titulo,
                'rua': rua,
                'numero': numero,
                'bairro': bairro,
                'cidade': cidade,
                'estado': estado,
                'cep': cep,
                'preco': preco,
                'area_privativa': area_privativa,
                'area_total': area_total,
                'quartos': quartos,
                'banheiros': banheiros,
                'suites': suites,
                'garages': garages,
                'andares': andares,
                'iptu': iptu,
                'taxa_condominio': taxa_condominio,
                'descricao':descricao,
                'caracteristicas': caracteristicas,
                'data_anuncio': data_anuncio,
                'nome_anunciante': nome_anunciante,
                'cod_anunciante': cod_anunciante,
                'numero_anunciante_1': numero_anunciante_1,
                'numero_anunciante_2': numero_anunciante_2,
                'url_anunciante': url_anunciante,
                'status': status,

                
                  
            }


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

tempo = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for item in data.itens():
  if item[1] is not None:
   if isinstance(item[1], list):
      for i in item[1]:
        comando = f"""INSERT INTO garimpo_dados (idgarimpo, chave, valor, criadopor, criadoem, alteradopor, alteradoem) VALUES ('{id_garimpo}', '{traduz_palavra(i)}', 'sim', 'Duda', '{tempo}', 'Duda', '{tempo}')"""
        cursor.execute(comando)
        conexao.commit()

    else
       
      comando = f"""INSERT INTO garimpo_dados (idgarimpo, chave, valor, criadopor, criadoem, alteradopor, alteradoem) VALUES ('{id_garimpo}', '{item[0]}', '{traduz_palavra(item[1])}', 'Duda', '{tempo}', 'Duda', '{tempo}')"""
      cursor.execute(comando)
      conexao.commit()


  else 

    pass      

  print('posiçao = ', pos)

  conexao.commit()
conexao.close()



   



  
  