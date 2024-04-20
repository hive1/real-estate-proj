from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json

from bs4 import BeautifulSoup
import requests


def scrapeData(zip_code):

    prices = []
    addresses = []
    beds = []
    baths = []
    images = []
    sqft = []
    acres = []

    '''Yea but imagine if we didn't have to SEE selenium work'''
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu") # Disables GPU hardware acceleration
    #chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    #chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.redfin.com")

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/div[2]/div/section/div/div/div/div/div/div/div/div[2]/div/div/form/div/div/input'))
    )

    button=driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[2]/div/section/div/div/div/div/div/div/div/div[2]/div/div/form/div/div/input')
    button.click()
    button.send_keys(zip_code)
    button.send_keys(Keys.ENTER)

    # This portion of the code is dedicated to finding the average 
    total=0
    counter=0
    
    '''This portion of the code is dedicated to finding the image URLs and then displaying them.
        We had issues doing this with selenium so we decided using bs4 and then implementing that
        src data through the tkinter canvas'''
    
    # response = requests.get(f'https://www.redfin.com/zipcode/{zip_code}')
    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text, 'html.parser')


    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.MapHomeCardReact.MapHomeCard'))
    )

    images = []
    results = driver.find_element(By.CSS_SELECTOR,'div.homes.summary').text
    results = results.replace(" homes•","")
    results = int(results)
    for x in range(results):
        mapHomeCard = driver.find_element(By.ID, f'MapHomeCard_{x}')
        img_link = mapHomeCard.find_element(By.CLASS_NAME, 'bp-Homecard__Photo--image').get_attribute('src')
        images.append(img_link)
        x+=1
    # print(images)        

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bp-Homecard__Content"))
    )

    y = 0
    for element in driver.find_elements(By.CLASS_NAME, "bp-Homecard__Content"):

        price = element.find_element(By.CSS_SELECTOR,"span.bp-Homecard__Price--value").text
        addresses.append(element.find_element(By.CSS_SELECTOR, "div.bp-Homecard__Address.flex.align-center.color-text-primary.font-body-xsmall-compact").text)
        beds.append(element.find_element(By.CSS_SELECTOR, "span.bp-Homecard__Stats--beds.text-nowrap").text)
        baths.append(element.find_element(By.CSS_SELECTOR, "span.bp-Homecard__Stats--baths.text-nowrap").text)
        
        acreDebug = element.find_element(By.CSS_SELECTOR,"span.bp-Homecard__Stats--lotsize.text-ellipsis").text
        if len(acreDebug.split()) > 1:
            if ',' in acreDebug:
                pass
            else:
                acres.append(acreDebug.split()[0])

        sqftDebug = element.find_element(By.CSS_SELECTOR, "span.bp-Homecard__Stats--sqft.text-nowrap").text
        if len(sqftDebug.split()) > 1:
            if '.' in sqftDebug.split()[0]:
                pass
            else:
                sqft.append(sqftDebug)

        price_num = price
        price_num = price_num.replace(",", "")
        price_num = price_num.replace("$", "")

        total += int(price_num)
        prices.append(price)

        counter+=1
        y += 1
    
    driver.quit
    return images, prices, addresses, beds, baths, sqft, acres, (total/counter)


'''this is only for debugging'''
if __name__ == '__main__':
    scrapeData('11934')
