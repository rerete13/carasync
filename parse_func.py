import requests as r
from bs4 import BeautifulSoup as bs
import fake_useragent as fu


async def parser(link:str):
    headers = {'User-Agent': fu.FakeUserAgent().random}

    url = link
    req = r.get(url, headers=headers)
    html = bs(req.content, 'lxml')

    return html



async def get_vincode(base_object):
    vincode = base_object.find_all('span', class_='vin-code-erased')
    return str(vincode[0]['data-full'])
    
    
    

async def car_plates_parser(num:str):
    headers = {'User-Agent': fu.FakeUserAgent().random}

    url = f'https://baza-gai.com.ua/nomer/{num}'
    req = r.get(url, headers=headers)
    html = bs(req.content, 'lxml')

    return html

