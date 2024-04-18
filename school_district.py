from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

zipcode = 10506

def school_district_finder(zipcode):
    driver = webdriver.Chrome()
    driver.get("https://www.greatschools.org/school-district-boundaries-map/")
    search = driver.find_element(By.NAME, "search-term")
    search.send_keys(zipcode)
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    school_link = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[1]/div[3]/label/a')
    school_name = school_link.text
    time.sleep(5)
    driver.quit()
    return school_name

print(school_district_finder(zipcode))
