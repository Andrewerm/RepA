from unitAPIs import CdekAPI, AvitoApi, PochtaApi, AliApi

# ключи API СДЭК
accountCDEK='0372b3fff5d6707cd1633469403952df'
client_secretCDEK='afc14015cce5555ce582bf97b963d2d2'
# ключи Авито
accountAvito='nAJ20oDgxFfBiBDpDa-Q'
client_secretAvito='twsAhk0OkOHongPvQ1un0GNkBO2baNcFRWebn6WA'

# ключи Почты РФ
tokenPochta='IomDCsxKO_jjc3yx7eocmSZ3FYDIMMGn'
loginPochta='andrewerm@yandex.ru'
secretPochta='531930Ab-'

# ключи Али
appAliKey='31102380'
Alisecret='ea36c75363323184e6779cff827368d4'
AlisSessionKey='50000000b46gvlSAoYNrD9bGtGosBVRl9gEyhqRvenhMpaltVZEzoLTORH13ec5298w'




# sessionAvito=Avito_oper(client_id=accountAvito, client_secret=client_secretAvito, user_id='10608733')
# sessionAvito.info_adv('1915250556')
sessCDEK=CdekAPI(client_id=accountCDEK, client_secret=client_secretCDEK)
sessAvito=AvitoApi(client_id=accountAvito, client_secret=client_secretAvito, user_id='10608733')
print(sessCDEK.GET_PVZ(postal_code='423800'))
print(sessAvito.info_adv('1915024987'))
sessPochta=PochtaApi(client_id=loginPochta, client_secret=secretPochta, token=tokenPochta)
print(sessPochta.normAddress('[{"id": "adr 1","original-address": "Lenina 177/2, Pleshanovo, Orenburgskaya oblast, Russian Federation, 461150"},'
                         '{"id": "adr 2","original-address": "ул. Мясницкая, д. 26, г. Москва, 1"}]'))
sessAli=AliApi(app_key=appAliKey, secret=Alisecret, sessionkey=AlisSessionKey)
# sessAli.aliProductList()
#sessAli.aliProductInfo()
print(sessAli.aliOrderList())

