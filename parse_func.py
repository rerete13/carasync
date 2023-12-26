import requests as r
from bs4 import BeautifulSoup as bs
import fake_useragent as fu
import aiohttp

async def parser(link:str):
    headers = {'User-Agent': fu.FakeUserAgent().random}

    req = r.get(link, headers=headers)
    html = bs(req.content, 'lxml')

    return html



async def parser_io(url):
    headers = {'User-Agent': fu.FakeUserAgent().random}
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            soup = bs(html, 'lxml', headers=headers)
            return soup



async def get_vincode(base_object):
    vincode = base_object.find_all('span', class_='vin-code-erased')
    return str(vincode[0]['data-full'])
    
    
    

async def car_plates_parser(num:str):
    headers = {'User-Agent': fu.FakeUserAgent().random}

    url = f'https://baza-gai.com.ua/nomer/{num}'
    req = r.get(url, headers=headers)
    html = bs(req.content, 'lxml')

    return html




async def plates_mania_parser(num:str):
    headers = {'User-Agent': fu.FakeUserAgent().random}

    url = f'https://platesmania.com/ua/gallery.php?fastsearch={num}'
    req = r.get(url, headers=headers)
    html = bs(req.content, 'lxml')

    return html
