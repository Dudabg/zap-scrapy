import requests
import json 
import pandas as pd
import time



payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
  'X-Domain': '.zapimoveis.com.br',
  'Cookie': '__cfruid=42d2a3aa93f72f906efb1036cc18470737173479-1698082455'
}

data_list = []

index = 10
for j in range(1, 40): 
  for i in range(0,6):
    try:
      url = f'https://glue-api.zapimoveis.com.br/v2/listings?user=df22c4a3-badb-4bdd-bd04-f4dd06c95b90&portal=ZAP&includeFields=search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%2Cpage%2Cfacets%2CfullUriFragments%2Cdevelopments%28search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%29%2CsuperPremium%28search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%29%2Cschema&categoryPage=RESULT&developmentsSize=0&superPremiumSize=0&__zt=&business=SALE&parentId=null&listingType=USED&priceMin=1000000&addressCity=Uberl%C3%A2ndia&addressLocationId=BR%3EMinas+Gerais%3ENULL%3EUberlandia&addressState=Minas+Gerais&addressPointLat=-24.003067&addressPointLon=-46.417853&addressType=city&unitTypes=HOME&unitTypesV3=CONDOMINIUM&unitSubTypes=CONDOMINIUM&usageTypes=RESIDENTIAL&page=' + str(j) + '&size=15&from='+ str(index) +'&levels=CITY&ref='
      response = requests.request("GET", url, headers=headers, data=payload,timeout=2)
      time.sleep(2)
      json = response.json()
      imoveis = json.get('search').get('result').get('listings')
      index+=15

      for i in imoveis:

        try:
          id = i.get('listing').get('id')
        except:
          id = None

        try:
          descricao = i.get('listing').get('description')
        except:
            descricao = None

        try:
          titulo = i.get('listing').get('title')
        except:
          titulo = None

        try:
          preco = i.get('listing').get('priceSuggestion') [0].get('price')
        except:
          preco = None
        
        try:
          data_anunciado = i.get('listing').get('createdAt')
        except:
          data_anunciado = None
        
        try:
          atualizacao_data = i.get('listing').get('updatedAt')
        except:
          atualizacao_data = None

        try:
          url = i.get('link').get('href')
        except:
            url = None
        try:
          url = i.get('link').get('href')
        except:
            url = None
        url_link = "https://www.zapimoveis.com.br" + url

        try:
          portal = i.get('listing').get('portal')
        except:
          portal = None

        try:
          pais= i.get('listing').get('address').get('country')
        except:
          pais = None

        try:
          cidade = i.get('listing').get('address').get('city')
        except:
          cidade = None

        try:
          estado = i.get('listing').get('address').get('state')
        except:
          estado = None

        try:
          rua= i.get('listing').get('address').get('street')
        except:
          rua = None

        try:
          bairro= i.get('listing').get('address').get('neighborhood')
        except:
          bairro = None

        try:
          imovel = i.get('listing').get('propertyType')
        except:
          imovel = None

        try:
          cep = i.get('listing').get('zipCode')
        except:
          cep = None

        try:  
          area_util = i.get('listing').get('usableAreas')
        except:         
          area_util = None

        try:
          area_total = i.get('listing').get('totalAreas')
        except:
          area_total = None

        try:
          area = i.get('listing').get('area')
        except:
          area = None

        try:
          portal = i.get('listing').get('portal')
        except:
          portal = None

        try:
          atualizacao_data = i.get('listing').get('updatedAt')
        except:
          atualizacao_data = None

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
          vagas = i.get('listing').get('parkingSpaces')
        except:
          vagas = None

        try:
          proprietario = i.get('account').get('name')
        except:
          proprietario = None

        try:
          proprietario_id = i.get('account').get('id')
        except:
          proprietario_id = None

        try:
          proprietario_telefone = i.get('listing').get('whatsappNumber')
        except:
          proprietario_telefone = None

        try:
          anunciante= i.get('account').get('name')
        except:
          anunciante = None

        try:
          anunciante_id = i.get('account').get('id')
        except:
          anunciante_id = None

        try:
          anunciante_telefone = i.get('listing').get('whatsappNumber')
        except:
          anunciante_telefone = None

        try:
          amenties = i.get('listing').get('amenities')
        except:
          amenties = None

           

    
        print(id)
        print(titulo)
        print(preco)
        print(descricao)
        print(data_anunciado)
        print(url)
        print(cep)
        print(area_util)
        print(area_total)
        print(area)
        print(portal)
        print(atualizacao_data)
        print(rua)
        print(bairro)
        print(pais)
        print(cidade)
        print(estado)
        print(quartos)
        print(banheiros)
        print(suites)
        print(vagas)
        print(proprietario)
        print(proprietario_id)
        print(proprietario_telefone)
        print(anunciante)
        print(anunciante_id)
        print(anunciante_telefone)
        print(amenties)
       
          

          
        data = {
                'id': id,
                'titulo': titulo,
                'descricao':descricao,
                'preco': preco,
                'data_anunciado': data_anunciado,
                'url': url_link,
                'portal': portal,
                'atualizacao_data': atualizacao_data,
                'cep': cep,
                'area_util': area_util,
                'area_total': area_total,
                'area': area,
                'cidade': cidade,
                'estado': estado,
                'rua': rua,
                'bairro': bairro,
                'pais': pais,
                'quartos': quartos,
                'banheiros': banheiros,
                'suites': suites,
                'vagas': vagas,
                'proprietario': proprietario,
                'proprietario_id': proprietario_id,
                'proprietario_telefone': proprietario_telefone,
                'anunciante': anunciante,
                'anunciante_id': anunciante_id,
                'anunciante_telefone': anunciante_telefone,
                'amenties': amenties
               
                
            }
        data_list.append(data)
    except:
      time.sleep(300)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data_list)

# Save the DataFrame to a CSV file
df.to_excel('imoveis.xlsx', index=False)
  
  
  