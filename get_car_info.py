from parse_func import car_plates_parser, get_vincode
import re
from func import change_symbols, cleaning
from parse_func import parser, plates_mania_parser
from aiogram import Bot


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


async def check_name(link):
    panel = (await parser(link)).find_all('h3', class_='text-center margin-bottom-10')
    
    panel = panel[0].find_all('a')
    panel = panel[0].text.split()
    panel = panel[0].upper()

    return panel


async def get_ukr_links_img(num, date, name):
    panels = (await plates_mania_parser(f'{num}')).find_all('div', class_='panel-body')

    verify = f'{date}'

    name = name.upper()

    arr_panel_links = []
    for i in range(len(panels)):
        link = panels[i].find_all('a')[0]['href']
        arr_panel_links.append(link)

    arr_panels_filter_img = []
    for i in arr_panel_links:

        link = f'https://platesmania.com{i}'
        panel = (await parser(link)).find_all('ul', class_='list-unstyled')

        try:
            date = panel[1]

        except:
            continue


        date = date.find_all('li')[0]
        date = (await cleaning(str(date))).replace('-', ' ').split()
        date = f'{date[2]}.{date[1]}.{date[0]}'

        if date == verify and name == (await check_name(link)):
            # print('find')
            arr_panels_filter_img.append(link)

    return arr_panels_filter_img


async def get_ukr_img(links):

    arr_ukr_img = []
    for i in links:

        img = (await parser(i)).find_all('img', class_='img-responsive center-block')
        arr_ukr_img.append(img[0]['src'])

    # print(arr_ukr_img)

    return arr_ukr_img



async def process_number(bot, message, number, delete):
    try:
        number = (await change_symbols(number))
        
        car_info = (await creat_info(number))
        
        date_registration = (await cleaning(car_info[2]))
        
        car_name = car_info[1].split()
        car_name = car_name[0]
        
        real_img_links = (await get_ukr_links_img(str(number), date_registration, car_name))
        real_img = (await get_ukr_img(real_img_links))
    
    except:
        await bot.delete_message(message_id=delete.message_id, chat_id=message.chat.id)
        await message.answer(f'Машину з номерним знаком\n"<b>{number}</b>" \nне знайдено')
        return False
    
    

    if len(real_img) > 0:
        for i in real_img:
            await message.answer_photo(i)
            pass
        
        await bot.delete_message(message_id=delete.message_id, chat_id=message.chat.id)
        await message.answer(f'{car_info[1]} <code>{number}</code>\n{car_info[0]}\n{car_info[3]} \n{car_info[2]}\n{car_info[4]}\n\n Інформація надана від: @autoparse_bot')
        await message.answer(f'Бажаєте найти більше інформації про номер?:\n\n<code>{number}</code>')
        return True
    
    else:
        if car_info != None:
            try:
                await message.answer_photo(car_info[5], f'{car_info[1]} <code>{number}</code>\n{car_info[0]}\n{car_info[3]} \n{car_info[2]}\n{car_info[4]}\n\n Інформація надана від: @autoparse_bot')
            
            except:
                await message.answer(f'{car_info[1]} <code>{number}</code>\n{car_info[0]}\n{car_info[3]} \n{car_info[2]}\n{car_info[4]}\n\n Інформація надана від: @autoparse_bot')
                
            await bot.delete_message(message_id=delete.message_id, chat_id=message.chat.id)
            await message.answer(f'Бажаєте найти більше інформації про номер?:\n\n<code>{number}</code>')
            return True
        
        else:
            await bot.delete_message(message_id=delete.message_id, chat_id=message.chat.id)
            await message.answer(f'{car_info[1]} <code>{number}</code>\n{car_info[0]}\n{car_info[3]} \n{car_info[2]}\n{car_info[4]}\n\n Інформація надана від: @autoparse_bot')
            await message.answer(f'Бажаєте найти більше інформації про номер?:\n\n<code>{number}</code>')
            return True
            
        
    
    
    