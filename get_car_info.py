from parse_func import car_plates_parser, get_vincode
import requests as r
import re



async def creat_info(num: str):
    
    base_object = await car_plates_parser(num)
    
    arr_year = base_object.find_all('div', class_="plate-model-card__content-date-model")
    arr_model = base_object.find_all('h4', class_='plate-model-card__content-title')
    arr_adition = base_object.find_all('li', class_="list-group-item plate-model__list-item")

    year = arr_year[0].text

    model = arr_model[0].text.strip()
    model = model.splitlines()[0].strip() + ' ' + model.splitlines()[2].strip()

    try:
        adres = arr_adition[3].text.strip()
        adres = adres.splitlines()[2].strip()
        
        registration = arr_adition[0].text.strip()
        registration = registration.splitlines()[1]
        
        things = arr_adition[1].text.strip()
        things = things.splitlines()[1]
        
        img = base_object.find_all('img', class_="card-img plate-model-card__img")
        img = img[0]['src']
        img = f'https://baza-gai.com.ua{img}'
        img  = re.sub(r"\s", "", img)
        
        
    except:
        except_object = base_object.find_all('span', class_="d-block plate-model__list-item-text")

        registration = except_object[0].text

        things = except_object[1].text
        
        adres = except_object[3].text.strip()
        
        img = None
 
    
    try:
        vincode = await get_vincode(base_object)
    except:
        vincode = None

    car = [year, model, registration, things, adres, img, vincode]

    return car


