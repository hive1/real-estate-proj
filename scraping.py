from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def scrapeData(zip_code):

    prices = []
    addresses = []
    beds = []
    baths = []

    driver = webdriver.Chrome()
    driver.get("https://www.redfin.com")

    '''Yea but imagine if we didn't have to SEE selenium work
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")  # Enables headless mode
    chrome_options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration
    '''
    button=driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div[2]/div/section/div/div/div/div/div/div/div/div[2]/div/div/form/div/div/input')
    button.click()
    button.send_keys(zip_code)
    button.send_keys(Keys.ENTER)

    # This portion of the code is dedicated to finding the average 
    total=0
    counter=0

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bp-Homecard__Content"))
    )
    for element in driver.find_elements(By.CLASS_NAME, "bp-Homecard__Content"):

        price = element.find_element(By.CSS_SELECTOR,"span.bp-Homecard__Price--value").text
        addresses.append(element.find_element(By.CSS_SELECTOR, "div.bp-Homecard__Address.flex.align-center.color-text-primary.font-body-xsmall-compact").text)
        beds.append(element.find_element(By.CSS_SELECTOR, "span.bp-Homecard__Stats--beds.text-nowrap").text)
        baths.append(element.find_element(By.CSS_SELECTOR, "span.bp-Homecard__Stats--baths.text-nowrap").text)

        price = price.replace(",", "")
        price = price.replace("$", "")

        total += int(price)
        prices.append(price)

        counter+=1
    
    driver.quit
    return prices, addresses, beds, baths, (total/counter)


'''this is only for debugging'''
if __name__ == '__main__':
    print(scrapeData('11934'))
