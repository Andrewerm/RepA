import requests, time
from requests.exceptions import HTTPError
from abc import ABC
from crmApp.models import tokensApi
from datetime import datetime, timedelta, timezone

def check_funcs(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        print('начало выполнения '+func.__name__)
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'конец выполнения {func.__name__}, время выполнения: {round(end-start)} секунд.')
        return return_value
    return wrapper


class providerAPI(ABC):

    BASE_URL=None
    AUTORIZATION_URL=None
    REQURL=None

    def __init__(self, **kwargs):
        self.auth_params=kwargs
        self.get_token()

    # def check_time_session_valid(self):
    #     return time.time()-self.session_params['timestamp']<self.session_params['expires_in']

    def get_token(self):
        data, created=tokensApi.objects.get_or_create(nameApi='cdek')
        if created or not data.token or data.data_expires<datetime.now(timezone.utc):
            # если в БД ещё нет записи cdek или есть, но токена нет, или он просрочен
            # self.get_token()
            url=self.BASE_URL+self.AUTORIZATION_URL
            params = {'grant_type': 'client_credentials', 'client_id': self.auth_params['client_id'],
              'client_secret': self.auth_params['client_secret']}
            self.session_params = self.resp("POST", url, params=params)
            data.token=self.session_params['access_token']
            delta = timedelta(seconds=int(self.session_params['expires_in']))
            data.data_expires=datetime.now(timezone.utc)+delta
            data.save()
            print('Получаем новый сессионный ключ от СДЭК')
        else:
            # если токен в БД есть и не просрочен
            print('Используем старый сессионный ключ от СДЭК')
            self.session_params={'access_token':data.token}
        self.bearer = {'Authorization': 'Bearer ' + self.session_params['access_token']}

    @check_funcs
    def resp(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, params=kwargs.get('params'), headers=kwargs.get('headers'),data=kwargs.get('data'))
            print('url: '+url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            # return {'errorOfResp':True}
        except Exception as err:
            print(f'Other error occurred: {err}')
            # return {'errorOfResp': True}
        else:
            res=response.json()
            # res['errorOfResp']=False
            return res