import requests
import json 
import pandas as pd



payload = {}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
  'X-Domain': '.zapimoveis.com.br',
  'Cookie': '__cfruid=42d2a3aa93f72f906efb1036cc18470737173479-1698082455'
}

data_list = []

for j in range(1,3):
  url = 'https://glue-api.zapimoveis.com.br/v2/listings?user=df22c4a3-badb-4bdd-bd04-f4dd06c95b90&portal=ZAP&includeFields=search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%2Cpage%2Cfacets%2CfullUriFragments%2Cdevelopments%28search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%29%2CsuperPremium%28search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%29%2Cschema&categoryPage=RESULT&developmentsSize=0&superPremiumSize=0&__zt=&business=SALE&parentId=null&listingType=USED&addressCity=Uberl%C3%A2ndia&addressLocationId=BR%3EMinas+Gerais%3ENULL%3EUberlandia&addressState=Minas+Gerais&addressPointLat=-18.912775&addressPointLon=-48.275523&addressType=city&unitTypes=APARTMENT&unitTypesV3=APARTMENT&unitSubTypes=UnitSubType_NONE%2CDUPLEX%2CTRIPLEX&usageTypes=RESIDENTIAL&page=' + str(j) + '&size=100&from=9&levels=CITY&ref='
 
  response = requests.request("GET", url, headers=headers, data=payload,timeout=2)



  with open("teste.txt","w") as arquivo:
      arquivo.write(str(response))



  json = response.json()
  imoveis = json.get('search').get('result').get('listings')
  

  for i in imoveis:
    id = i.get('listing').get('id')
    descricao = i.get('listing').get('description')
    titulo = i.get('listing').get('title')
    preco = i.get('listing').get('price')
    data_anunciado = i.get('listing').get('createdAt')
    url = i.get('listing').get('url')
    portal = i.get('listing').get('portal')
    atualizacao_data = i.get('listing').get('updatedAt')
    endereco= i.get('listing').get('address')
    cidade = i.get('listing').get('city')
    estado = i.get('listing').get('state')
    cep = i.get('listing').get('zipCode')
    area_util = i.get('listing').get('usableAreas')
    area_total = i.get('listing').get('totalAreas')
    pais= i.get('listing').get('country')
    rua= i.get('listing').get('street')
    bairro= i.get('listing').get('neighborhood')
    imovel = i.get('listing').get('propertyType')
    area = i.get('listing').get('area')
    quartos = i.get('listing').get('bedrooms')
    banheiros = i.get('listing').get('bathrooms')
    suites = i.get('listing').get('suites')
    vagas = i.get('listing').get('parkingSpaces')
    proprietario = i.get('account').get('name')
    proprietario_id = i.get('account').get('id')
    proprietario_logo = i.get('account').get('logoUrl')
    proprietario_telefone = i.get('account').get('whatsappNumber')
    proprietario_email = i.get('account').get('email')
    proprietario_site = i.get('account').get('minisite')
    anunciante= i.get('account').get('name')
    anunciante_id = i.get('account').get('id')
    anunciante_logo = i.get('account').get('logoUrl')
    anunciante_telefone = i.get('account').get('whatsappNumber')
    anunciante_email = i.get('account').get('email')
    anunciante_site = i.get('account').get('minisite')



  
    print(id)
    print(titulo)
    print(preco)
    print(data_anunciado)
    print(url)
    print(portal)
    print(atualizacao_data)
    print(endereco)
    print(cidade)
    print(estado)
    print(quartos)
    print(banheiros)
    print(suites)
    print(vagas)
    print(proprietario)
    print(proprietario_id)
    print(proprietario_logo)
    print(proprietario_telefone)
    print(proprietario_email)
    print(proprietario_site)
    print(anunciante)
    print(anunciante_id)
    print(anunciante_logo)
    print(anunciante_telefone)
    print(anunciante_email)
    print(anunciante_site)

    
    data = {
          'id': id,
          'titulo': titulo,
          'preco': preco,
          'data_anunciado': data_anunciado,
          'url': url,
          'portal': portal,
          'atualizacao_data': atualizacao_data,
          'endereco': endereco,
          'cidade': cidade,
          'estado': estado,
          'quartos': quartos,
          'banheiros': banheiros,
          'suites': suites,
          'vagas': vagas,
          'proprietario': proprietario,
          'proprietario_id': proprietario_id,
          'proprietario_logo': proprietario_logo,
          'proprietario_telefone': proprietario_telefone,
          'proprietario_email': proprietario_email,
          'proprietario_site': proprietario_site,
          'anunciante': anunciante,
          'anunciante_id': anunciante_id,
          'anunciante_logo': anunciante_logo,
          'anunciante_telefone': anunciante_telefone,
          'anunciante_email': anunciante_email,
          'anunciante_site': anunciante_site
      }
    data_list.append(data)

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data_list)

# Save the DataFrame to a CSV file
df.to_excel('imoveis.xlsx', index=False)
  
  
  