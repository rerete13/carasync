import undetected_chromedriver as uc
from selenium.webdriver.common.by import By as by
import fake_useragent as fake
from asyncio import sleep



async def get_american_car_info(vin:str):

    try:   
        
        driver = uc.Chrome(version_main=121, headless=True)
        
        driver.get('https://bid.cars/ua/search')

        await sleep(3)

        enter_login = driver.find_element(by.XPATH, '//*[@id="search_field"]')
        enter_login.clear()
        await sleep(0.5)
        enter_login.send_keys(vin)

        await sleep(0.3)

        enter = driver.find_element(by.XPATH, '//*[@id="submit_search"]')
        enter.click()

        await sleep(3)

        photos = driver.find_element(by.ID, 'galleryThumbs')
        elements = driver.find_elements(by.CLASS_NAME, 'options-list')
        
        await sleep(6)
        
        
        photos = photos.find_elements(by.TAG_NAME, 'img')
        car_info = elements[0].text.split('\n')
        ditails_info = elements[1].text.split('\n')
        
        await sleep(3)

        photo = []
        for i in photos:
            photo.append(i.get_dom_attribute('src'))
            
        
        # print(car_info)
        # print('---------------------------------------')
        # print(ditails_info)
        # print('---------------------------------------')
        # print(photo)


        
        
        driver.close()
        driver.quit()
        
        # print(photo)
        # print(ditails_info)
        # print(car_info)

        return photo, ditails_info, car_info
        
    except:
        driver.close()
        driver.quit()

        return None, None, None