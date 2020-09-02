import requests
from requests.exceptions import HTTPError


# headers={'Yandex-API-Key': 'dfb766de-1a3e-4618-b791-e1fc3e52dbc7'}
headers={}
url='https://jsonplaceholder.typicode.com/comments'
# url='https://api.weather.yandex.ru/v1/informers'
params={'postId':'1'}
r=requests.get(url,headers=headers, params=params)

print(r.url)
print(r.status_code)
print(r.json())
print(r.headers)

