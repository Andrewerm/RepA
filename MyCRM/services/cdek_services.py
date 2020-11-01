from services.common import providerAPI
import time, json



class CdekOrder():
    def __init__(self, **params):
        self.data=dict()
        self.data['orderID']='aecrm'+str(time.time())
        self.data['tariff_code']=params['tariff_code'] or 136
        self.data['shipment_point']=params.get('shipment_point') or 'SAR4'
        self.data['delivery_point']=params.get('delivery_point')
        self.data['delivery_recipient_cost']=params.get('delivery_recipient_cost') or {'value':0}
        self.data['value']=params.get('value') or 0 # сумма дополнительного сбора за доставку
        self.data['seller']={'name':'ИП Ижболдин А.А.', 'inn':'165053023146', 'phone':'+79063337333', 'ownership_form':63}
        self.data['recipient']={'name': params['name'],'phones': [{'number': params['phone']}]}
        self.data['packages']=params.get('packages')
        self.data['number']=params.get('number')

    def retJson(self):
        d=json.dumps(self.data)
        return d



class CdekAPI(providerAPI):
    BASE_URL='https://api.cdek.ru/v2'
    AUTORIZATION_URL='/oauth/token'
    REQURL='/deliverypoints'
    REQORDER='/orders'

    def GET_PVZ(self, **params):
        if not self.check_time_session_valid():
            self.get_token()
        url = self.BASE_URL + self.REQURL
        res=self.resp('GET', url, headers=self.bearer, params=params)
        return res

    def Get_order_info(self, **params):
        if not self.check_time_session_valid():
            self.get_token()
        url = self.BASE_URL + self.REQORDER
        if params.get('uuid'):
            url+= '/'+params['uuid']
        elif params.get('cdek_number'):
            url += '?' + params['cdek_number']
        return self.resp('GET', url, headers=self.bearer)

    def new_order(self, newOrderData):
        data=newOrderData.retJson()
        if not self.check_time_session_valid():
            self.get_token()
        url = self.BASE_URL + self.REQORDER
        headers= self.bearer
        headers['Content-Type']='application/json'
        r=self.resp('POST', url, headers=headers, data=data.encode('UTF-8'))
        return r
