from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# https://sites.google.com/chromium.org/driver/


'''
This returns the bed, bath, price, and address of each listing and then the subsequent average price of the listings as a whole
'''

def scrapeData(zip_code):

    prices = []
    addresses = []
    beds = []
    baths = []

    driver = webdriver.Chrome()
    driver.get("https://www.redfin.com")

    button=driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[2]/div/section/div/div/div/div/div/div/div/div[2]/div/div/form/div/div/input')
    button.click()
    button.send_keys(zip_code)
    button.send_keys(Keys.ENTER)
    
    total=0
    counter=0

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bp-Homecard__Content"))
    )
    for element in driver.find_elements(By.CLASS_NAME, "bp-Homecard__Content"):
        price= element.find_element(By.CSS_SELECTOR,"span.bp-Homecard__Price--value").text
        prices += price

        address=element.find_element(By.CSS_SELECTOR, "div.bp-Homecard__Address.flex.align-center.color-text-primary.font-body-xsmall-compact").text
        addresses += address

        bed=element.find_element(By.CSS_SELECTOR, "span.bp-Homecard__Stats--beds.text-nowrap").text
        beds += bed

        bath=element.find_element(By.CSS_SELECTOR, "span.bp-Homecard__Stats--baths.text-nowrap").text
        baths += bath

        print(price,"\n",bed,bath,"\n",address,"\n")
        price=price.replace(",","")
        price=int(price.replace("$",""))
        total+=price
        counter+=1  
    
    driver.quit()
    return prices, addresses, beds, baths, (total / counter)
   