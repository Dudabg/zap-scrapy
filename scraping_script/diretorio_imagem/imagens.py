import os
import requests
import json 
import time

# Cabeçalhos e payload como no seu exemplo
payload = {}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Domain': '.zapimoveis.com.br',
    'Cookie': '__cfruid=42d2a3aa93f72f906efb1036cc18470737173479-1698082455'
}

data_list = []

index = 10
for j in range(1,3): 
  for i in range(0,6):
    
      url = f'https://glue-api.zapimoveis.com.br/v2/listings?user=df22c4a3-badb-4bdd-bd04-f4dd06c95b90&portal=ZAP&includeFields=search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%2Cpage%2Cfacets%2CfullUriFragments%2Cdevelopments%28search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%29%2CsuperPremium%28search%28result%28listings%28listing%28listingsCount%2CsourceId%2CdisplayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2Cstamps%2CcreatedAt%2Cfloors%2CunitTypes%2CnonActivationReason%2CproviderId%2CpropertyType%2CunitSubTypes%2CunitsOnTheFloor%2ClegacyId%2Cid%2Cportal%2CunitFloor%2CparkingSpaces%2CupdatedAt%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2CadvertiserContact%2CwhatsappNumber%2Cbedrooms%2CacceptExchange%2CpricingInfos%2CshowPrice%2Cresale%2Cbuildings%2CcapacityLimit%2Cstatus%2CpriceSuggestion%29%2Caccount%28id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2ClegacyZapId%2CcreatedDate%2Cminisite%2Ctier%29%2Cmedias%2CaccountLink%2Clink%29%29%2CtotalCount%29%29%2Cschema&categoryPage=RESULT&developmentsSize=0&superPremiumSize=0&__zt=&business=SALE&parentId=null&listingType=USED&addressCity=Uberl%C3%A2ndia&addressLocationId=BR%3EMinas+Gerais%3ENULL%3EUberlandia&addressState=Minas+Gerais&addressPointLat=-18.912775&addressPointLon=-48.275523&addressType=city&unitTypes=APARTMENT&unitTypesV3=APARTMENT&unitSubTypes=UnitSubType_NONE%2CDUPLEX%2CTRIPLEX&usageTypes=RESIDENTIAL&page=' + str(j) + '&size=15&from='  + str(index) + '&levels=CITY&ref='
      response = requests.request("GET", url, headers=headers, data=payload,timeout=2)
      time.sleep(2)
      json = response.json()
      imoveis = json.get('search').get('result').get('listings')
      index+=15

# Iterar sobre os apartamentos obtidos na resposta JSON
for i in imoveis:
    codigo_apartamento = i.get('listing').get('Id')

    # Verificar se o código do apartamento é válido
    if codigo_apartamento:
        # Criar o nome do diretório com base no código do apartamento
        nome_diretorio = f"apartamentos/{codigo_apartamento}"

        # Verificar se o diretório já existe, se não, criar
        if not os.path.exists(nome_diretorio):
            os.makedirs(nome_diretorio)
            print(f"Pasta '{nome_diretorio}' criada com sucesso!")
        else:
            print(f"Pasta '{nome_diretorio}' já existe.")
    else:
        print("Código do apartamento não encontrado na resposta JSON.")

    # Aqui você pode adicionar o código para baixar as imagens ou outras operações relacionadas ao apartamento
    # ...

    # Aguarde por algum tempo para evitar fazer muitas requisições rapidamente
    time.sleep(2)



# Continuar o restante do seu código, se houver
