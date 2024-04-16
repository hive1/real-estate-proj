from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# https://sites.google.com/chromium.org/driver/

zip_code=input("Enter zip code: ")

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
    address=element.find_element(By.CSS_SELECTOR, "div.bp-Homecard__Address.flex.align-center.color-text-primary.font-body-xsmall-compact").text
    bed=element.find_element(By.CSS_SELECTOR, "span.bp-Homecard__Stats--beds.text-nowrap").text
    bath=element.find_element(By.CSS_SELECTOR, "span.bp-Homecard__Stats--baths.text-nowrap").text
    print(price,"\n",bed,bath,"\n",address,"\n")
    price=price.replace(",","")
    price=int(price.replace("$",""))
    total+=price
    counter+=1
print("$",(total/counter))
time.sleep(5)
driver.quit