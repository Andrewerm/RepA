from services.common import providerAPI
import json
from datetime import datetime, timedelta, timezone
from crmApp.models import tokensApi

class CdekOrder():
    def __init__(self, **params):
        self.data=params
        self.data['delivery_recipient_cost']=params.get('delivery_recipient_cost') or {'value':0}
        self.data['value']=params.get('value') or 0 # сумма дополнительного сбора за доставку
        self.data['seller']={'name':'ИП Ижболдин А.А.', 'inn':'165053023146', 'phone':'+79063337333', 'ownership_form':63}
        self.data['recipient']={'name': params['name'],'phones': [{'number': params['phone']}]}
        self.data['packages'][0]['length']=10
        self.data['packages'][0]['width'] = 10
        self.data['packages'][0]['height'] = 5

    def retJson(self):
        return json.dumps(self.data)



class CdekAPI(providerAPI):
    BASE_URL='https://api.cdek.ru/v2'
    AUTORIZATION_URL='/oauth/token'
    REQURL='/deliverypoints'
    REQORDER='/orders'

    # def __init__(self, **kwargs):
    #     self.auth_params=kwargs
    #     self.get_token_from_base()

    # def get_token_from_base(self):
    #     data, created=tokensApi.objects.get_or_create(nameApi='cdek')
    #     if created or not data.token or data.data_expires<datetime.now(timezone.utc):
    #         # если в БД ещё нет записи cdek или есть, но токена нет, или он просрочен
    #         self.get_token()
    #         data.token=self.session_params['access_token']
    #         delta = timedelta(seconds=int(self.session_params['expires_in']))
    #         data.data_expires=datetime.now(timezone.utc)+delta
    #         data.save()
    #         print('Получаем новый сессионный ключ от СДЭК')
    #     else:
    #         # если токен в БД есть и не просрочен
    #         self.session_params['access_token']=data.token
    #         print('Используем старый сессионный ключ от СДЭК')


    def GET_PVZ(self, **params):

        url = self.BASE_URL + self.REQURL
        res=self.resp('GET', url, headers=self.bearer, params=params)
        return res

    def get_order_info(self, **params):
        self.get_token()
        url = self.BASE_URL + self.REQORDER
        if params.get('uuid'):
            url+= '/'+params['uuid']
        elif params.get('cdek_number'):
            url += '?' + params['cdek_number']
        return self.resp('GET', url, headers=self.bearer)

    def new_order(self, newOrderData):
        data=newOrderData.retJson()
        self.get_token()
        url = self.BASE_URL + self.REQORDER
        headers= self.bearer
        headers['Content-Type']='application/json'
        return self.resp('POST', url, headers=headers, data=data.encode('UTF-8'))


class  Calc_tarif(providerAPI):
    BASE_URL = 'https://kit.cdek-calc.ru/api'
    def __init__(self):
        pass


    def get_tarif(self,  **kwargs):
        self.params=dict()
        self.params['weight'] =kwargs.get('weight','0.1')
        self.params['height'] = kwargs.get('height','10')
        self.params['width'] = kwargs.get('width','10')
        self.params['length'] = kwargs.get('length','10')
        self.params['from_post_code'] = kwargs.get('from_post_code')
        self.params['to_post_code'] = kwargs.get('to_post_code')
        tarifs='136,137,138,139,10,11,12,1,5,233,234,301,302'
        self.params['contract'] = kwargs.get('contract', '2')
        self.params['tariffs'] = kwargs.get('tariffs', tarifs)
        resp = self.resp('GET', self.BASE_URL, params=self.params)
        self.response=[val for key,val in resp.items() if not val.get('error')]
        self.response.sort(key=lambda x: float((x['result']['total_price']).replace(',','')))
        return self.response

