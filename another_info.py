from parse_func import parser, parser_io


# from 0 to 9
async def all_comments(num):
    soup = await parser('https://baza-gai.com.ua')
    comments = soup.find_all('tr', class_='pt-3 pb-3')
    finall_comment = comments[num].text.strip()
    finall_comment = finall_comment.splitlines()
    out = f'Номер: <code>{finall_comment[4].strip()}</code>\nАвтор: {finall_comment[15].strip()}\nВідгук: \n{finall_comment[20].strip()}\n{finall_comment[23].strip()}'
    number = f'{finall_comment[4].strip()}'
    number = number.replace(' ', '')
    return out, number


async def top_cars_sales():
    all = (await parser('https://baza-gai.com.ua')).find_all('li', class_="list-item px-1")

    all_cars = []
    for i in range(50):
        all_cars.append(all[i].text)

    all_cars_out = []
    for i in range(50):
        all_cars_edit = all_cars[i].splitlines()

        all_cars_edit = all_cars_edit[1].strip() + ' ' + all_cars_edit[3].strip()

        out = f'{i+1}: {all_cars_edit}'

        all_cars_out.append(out)


    return all_cars_out


async def repairs_and_citys():
    #110 - 136
    #145 - 171
    links = (await parser('https://baza-gai.com.ua')).find_all('a')
    let = 'href'
    all_citys_link = []
    all_citys = []
    for i in range(145, 172):
        link = f'https://baza-gai.com.ua{links[i][let]}'
        all_citys_link.append(link)
        all_citys.append(links[i].text)
        
    return all_citys_link, all_citys


async def get_city_repaire(num:int):
    
    link, citys = (await repairs_and_citys())
    city =  (await parser(link[num])).find_all('tr')

                
    arr_about_places = []
    maps = []

    for i in range(1, len(city)):
        x = city[i].text.splitlines()
        out = f'{x[4].strip()}\n{x[9].strip()}\n{x[10][0:15]}'
        arr_about_places.append(out)
    
    for i in range(1, len(city)):
        location = city[i].find_all('a', target='_blank')
        link_prepair = location[0]['href']
        
        map_link = ''
        for j in link_prepair:
            if j == ' ':
                j = '+'
                map_link += j
                continue
            
            else:
                map_link += j
        
        maps.append(map_link)
        
    
    return arr_about_places, maps