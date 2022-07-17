from bs4 import BeautifulSoup as bs
from cookies import cookies, headers, data, cookies1, headers1
import requests
import json


session = requests.Session()


url = 'https://trudvsem.ru/iblocks/prr_auth/login?to=%252F&is_auth_response=true'
response = requests.post('https://trudvsem.ru/iblocks/prr_auth/login?to=/', cookies=cookies, headers=headers, data=data)
print(response)

# link = 'https://trudvsem.ru/auth/manager/'
link = 'https://trudvsem.ru/cv/card/print?candidateId=db2c96b0-a24f-11ea-b2aa-7bf9d8e248ac&cvId=14935060-a255-11ea-8870-79a78a7da306'
# url3 = 'https://trudvsem.ru/iblocks/flat_filter_prr_search_cv/candidates/db2c96b0-a24f-11ea-b2aa-7bf9d8e248ac/cvs/14935060-a255-11ea-8870-79a78a7da306/contactsData'

response = session.get(link, headers=headers1, cookies=cookies1)
print(response)

url3 = 'https://trudvsem.ru/iblocks/flat_filter_prr_search_cv/candidates/db2c96b0-a24f-11ea-b2aa-7bf9d8e248ac/cvs/14935060-a255-11ea-8870-79a78a7da306/contactsData'

response = session.get(url3, headers=headers1, cookies=cookies1)
print(response)

soup = bs(response.text, 'html.parser')
js = json.loads(response.text)['data']['contacts']

for j in js:
    if j['value']:
        print(j['contactType']['text'])



