import undetected_chromedriver as uc
from selenium.webdriver.common.by import By as by
from asyncio import sleep


async def get_american_car_info(vin:str, chrome:int = 120):

    try:   
        driver = uc.Chrome(version_main=chrome)
        driver.get('https://bid.cars/ua/search')

        await sleep(2)

        enter_login = driver.find_element(by.XPATH, '//*[@id="search_field"]')
        enter_login.clear()
        await sleep(0.1)
        enter_login.send_keys(vin)

        await sleep(0.2)

        enter = driver.find_element(by.XPATH, '//*[@id="submit_search"]')
        enter.click()

        await sleep(7)

        car_info = []
        ditails_info = []
        for i in range(1, 7):
            d_info = driver.find_element(by.XPATH, f'/html/body/section[1]/div/div[5]/div[1]/div/div/div/div/div[3]/div[2]/div[{i}]/span')
            c_info = driver.find_element(by.XPATH, f'/html/body/section[1]/div/div[5]/div[1]/div/div/div/div/div[4]/div[2]/div[{i}]/span')
            ditails_info.append(d_info.text)
            car_info.append(c_info.text)


        photos = driver.find_element(by.CLASS_NAME, 'gallery-thumbnails')

        await sleep(1)
        photos = photos.find_elements(by.TAG_NAME, 'a')
        await sleep(1)

        photos_link = []
        for i in photos:
            try:
                photos_link.append(i.get_dom_attribute('style'))
                
            except:
                pass


        photos = []
        for i in photos_link:
            x = False
            link = ''
            for j in i:
                if (j == "'" or x == 1) and j != ')':
                    x = True
                    if j == "'":
                        continue
                    else:
                        link += j
                    
            photos.append(link)
            
        driver.save_screenshot('debug_show.png')
        
        driver.close()
        driver.quit()

        return photos, ditails_info, car_info
        
    except:
        driver.close()
        driver.quit()

        return None, None, None
    




