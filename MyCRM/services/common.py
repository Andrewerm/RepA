import requests, time
from requests.exceptions import HTTPError
from abc import ABC



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