import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from chromedriver_py import binary_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_object = Service(binary_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service_object,options=options)

def login():
    driver.get('https://connect.soligent.net/sca/checkout.ssp?is=login&login=T&origin=home&origin_hash=search#login-register')

    login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="login-email"]'))
    )
    password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="login-password"]'))
    )

    login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="login-register-login-submit"]'))
    )

    login.send_keys('max@ware.solar')
    password.send_keys('Carbon3333')

    login_button.click()
    time.sleep(8)
    cookies = {}
    selenium_cookies = driver.get_cookies()
    for cookie in selenium_cookies:
        cookies[cookie['name']] = cookie['value']
    print(cookies,'\n')
    return cookies
    

def get_posts():    
    cookies = login()
    #print(cookies)
    response = requests.get('https://connect.soligent.net/api/items?language=en&currency=USD&c=3510556&offset=0&sitepath=%2Fsca%2FsearchApi.ssp&sort=custitem_ns_sc_ext_ts_90_amount%3Adesc&use_pcv=F&fieldset=search&n=2&include=facets&limit=12&country=US&pricelevel=4&', cookies=cookies)
    print(response.text)
    
get_posts()

