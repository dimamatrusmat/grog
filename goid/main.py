# from bitrix24.bitrix24 import Bitrix24

# bx24 = Bitrix24('corp.synergy.ru', 'ef38763a07191319ced72a719d478fa8.97ba772d9aeb72a25b1549fd9b5b5b3321c7eeec/cbc207ca1ed8729bc0e82eaf10cc862d.fe8264e216f349104d2be15fc5f29b0bfdb9bfd6')

# print(bx24.call('app.info'))
import requests
from bs4 import BeautifulSoup as bs

session = requests.Session()



cookies = {
    '_ym_d': '1653469886',
    '_ym_uid': '1653469886843321974',
    'tmr_lvid': '77ce676a7a3c56dad2dcaac934b995da',
    'tmr_lvidTS': '1655877024105',
    '_ga': 'GA1.2.639543111.1655877024',
    '_tt_enable_cookie': '1',
    '_ttp': '2b5c1c2d-46e3-47c5-a490-384463dd7a29',
    '_gaexp': 'GAX1.2.AUkJa6q4RgiYRrBf6qd6MA.19263.1',
    'tmr_reqNum': '12',
    'PHPSESSID': 'wb17z1Ig1rY0Z54mc4w8xyI914SMLojR',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ym_d=1653469886; _ym_uid=1653469886843321974; tmr_lvid=77ce676a7a3c56dad2dcaac934b995da; tmr_lvidTS=1655877024105; _ga=GA1.2.639543111.1655877024; _tt_enable_cookie=1; _ttp=2b5c1c2d-46e3-47c5-a490-384463dd7a29; _gaexp=GAX1.2.AUkJa6q4RgiYRrBf6qd6MA.19263.1; tmr_reqNum=12; PHPSESSID=wb17z1Ig1rY0Z54mc4w8xyI914SMLojR',
    'DNT': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'back_url': '/index.php',
}

response = session.get('https://corp.synergy.ru:8891/', params=params, cookies=cookies, headers=headers)

print(response.text)

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru,en;q=0.9,de;q=0.8,la;q=0.7,sr;q=0.6',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'BITRIX_SM_TIME_ZONE=-300; _ym_uid=1651645586362519718; _ym_d=1651645586; _ga=GA1.3.923623742.1651645586; lang_bitrix_new=ru; tmr_lvidTS=1651726339998; tmr_lvid=0c1614d4136ef481e59ac01c73c84736; _ga=GA1.2.1752467328.1651726341; _tt_enable_cookie=1; _ttp=c68e3133-52e4-4fad-949a-e28709ebbcad; _gcl_au=1.1.1171903548.1654752529; advcake_session_id=7f61baac-6efd-5793-9d97-e16b7b96bf63; tmr_reqNum=101; PHPSESSID=OhcZC0tyh4m6GaJw40dC0qlbZDAAYDiI; BITRIX_SM_NCC=Y; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; _gid=GA1.3.321296331.1658115861; _ym_isad=1',
    'Referer': 'https://corp.synergy.ru/crm/deal/tablet.php?dealId=4967716&tablet=Y',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1842 Yowser/2.5 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = session.get('https://corp.synergy.ru/bitrix/sub/?CHANNEL_ID=ef38763a07191319ced72a719d478fa8.97ba772d9aeb72a25b1549fd9b5b5b3321c7eeec/cbc207ca1ed8729bc0e82eaf10cc862d.fe8264e216f349104d2be15fc5f29b0bfdb9bfd6&tag=453&time=Mon,%2018%20Jul%202022%2009:11:24%20GMT&mid=16490557400000000211138993&rnd=1658135479151', cookies=cookies, headers=headers)

print(response.text)

with open('ddd.html', 'w', encoding="utf-8") as f:
    f.write(response.text)


# url = 'https://trudvsem.ru/iblocks/prr_auth/login?to=%252F&is_auth_response=true'   
# response = requests.post('https://trudvsem.ru/iblocks/prr_auth/login?to=/', cookies=cookies, headers=headers, data=data)
# print(response)

# # link = 'https://trudvsem.ru/auth/manager/'
# link = 'https://trudvsem.ru/cv/card/print?candidateId=db2c96b0-a24f-11ea-b2aa-7bf9d8e248ac&cvId=14935060-a255-11ea-8870-79a78a7da306'
# # url3 = 'https://trudvsem.ru/iblocks/flat_filter_prr_search_cv/candidates/db2c96b0-a24f-11ea-b2aa-7bf9d8e248ac/cvs/14935060-a255-11ea-8870-79a78a7da306/contactsData'

# response = session.get(link, headers=headers1, cookies=cookies1)
# print(response)

# url3 = 'https://trudvsem.ru/iblocks/flat_filter_prr_search_cv/candidates/db2c96b0-a24f-11ea-b2aa-7bf9d8e248ac/cvs/14935060-a255-11ea-8870-79a78a7da306/contactsData'

# response = session.get(url3, headers=headers1, cookies=cookies1)
# print(response)

# soup = bs(response.text, 'html.parser')
# js = json.loads(response.text)['data']['contacts']

# for j in js:
#     if j['value']:
#         print(j['contactType']['text'])



