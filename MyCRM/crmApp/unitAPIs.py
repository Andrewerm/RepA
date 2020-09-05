import requests, time, base64
from requests.exceptions import HTTPError
from abc import ABC
import hmac , pytz
from datetime import datetime


class providerAPI(ABC):

    BASE_URL=None
    AUTORIZATION_URL=None
    REQURL=None

    def __init__(self, **kwargs):
        self.auth_params=kwargs
        self.get_token()

    def check_time_session_valid(self):
        return time.time()-self.session_params['timestamp']<self.session_params['expires_in']

    def get_token(self):
        url=self.BASE_URL+self.AUTORIZATION_URL
        params = {'grant_type': 'client_credentials', 'client_id': self.auth_params['client_id'],
          'client_secret': self.auth_params['client_secret']}
        self.session_params=self.resp("POST", url, params=params)
        self.session_params['timestamp'] = time.time()
        self.bearer = {'Authorization': 'Bearer ' + self.session_params['access_token']}

    def resp(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, params=kwargs.get('params'), headers=kwargs.get('headers'),data=kwargs.get('data'))
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

class CdekAPI(providerAPI):
    BASE_URL='https://api.cdek.ru/v2'
    AUTORIZATION_URL='/oauth/token'
    REQURL='/deliverypoints'

    def GET_PVZ(self, **params):
        if not self.check_time_session_valid():
            self.get_token()
        url = self.BASE_URL + self.REQURL
        return self.resp('GET', url, headers=self.bearer, params=params)

class AvitoApi(providerAPI):
    BASE_URL='https://api.avito.ru'
    REQURL='/core/v1'
    AUTORIZATION_URL='/token'

    def info_adv(self, item_id):
        if not self.check_time_session_valid():
            self.get_token()
        url=self.BASE_URL+self.REQURL+'/accounts/'+self.auth_params['user_id']+'/items/'+item_id
        return self.resp("GET", url,headers=self.bearer )

class PochtaApi(providerAPI):
    BASE_URL = 'https://otpravka-api.pochta.ru'
    NORM_ADR='/1.0/clean/address'

    def get_token(self):
        auth_keys=f'{self.auth_params["client_id"]}:'f'{self.auth_params["client_secret"]}'
        auth_keysB=auth_keys.encode('UTF-8')
        userAuthB=base64.b64encode(auth_keysB)
        userAuth=userAuthB.decode('UTF-8')
        self.headers = {'X-User-Authorization': f'Basic {userAuth}',
                        'Authorization': f'AccessToken {self.auth_params["token"]}',
                        'Content-Type': 'application/json'
                        }
        print(userAuth)

    def normAddress(self, adresses):
        url=self.BASE_URL+self.NORM_ADR
        return self.resp("POST", url, headers=self.headers, data=adresses.encode('UTF-8'))


class AliApi(providerAPI):
    BASE_URL ='https://eco.taobao.com/router/rest'
    METHOD=None

    def __aop_signature(self, appsecret, kwargs):
        a = [(s, kwargs[s]) for s in kwargs] # словарь в список таплов
        a.sort() # сортировка
        result = "".join(["%s%s" % (s[0], s[1]) for s in a])
        signature = hmac.new(
            appsecret.encode("utf-8"),
            result.encode("utf-8"),
            'MD5'          # hmac_md5
        ).hexdigest()  # шестнадцатеричный
        return str(signature).upper()

    def __aop_timestamp(self):
        # временная метка по китайское вроеменной зоне
        tz = pytz.timezone('Asia/Shanghai')
        timestamp = datetime.now(tz=tz).strftime('%Y-%m-%d %H:%M:%S')
        return timestamp

    def get_token(self):
        pass

    def __reqApi(self, **kwargs):
        url=self.BASE_URL
        payload = {'app_key':self.auth_params['app_key'],
                   'format':'json',
                   'method':self.METHOD,
                   'partner_id':'apidoc',
                   'sign_method':'hmac',
                   'v':'2.0',
                   kwargs['key']: kwargs['value'],
                   'timestamp':self.__aop_timestamp(),
                   'session':self.auth_params['sessionkey']}
        sign=self.__aop_signature(self.auth_params['secret'], payload)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload['sign']=sign
        print(sign, '  ', payload['timestamp'])
        return self.resp("POST", url, headers=headers, data=payload)

    def aliProductList(self):
        self.METHOD='aliexpress.solution.product.list.get'
        key='aeop_a_e_product_list_query'
        value="{'product_status_type':'onSelling', page_size:5, current_page:3}"
        return self.__reqApi(key=key, value=value)

    def aliProductInfo(self):
        self.METHOD='aliexpress.solution.product.info.get'
        key='product_id'
        value="1005001369514231"
        return self.__reqApi(key=key, value=value)

    def aliOrderList(self):
        self.METHOD='aliexpress.solution.order.get'
        key='param0'
        value="{page_size:20, current_page:1, create_date_start:	'2017-10-12 12:12:12'}"
        return self.__reqApi(key=key, value=value)