import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from chromedriver_py import binary_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# url = "https://connect.soligent.net/api/items"
service_object = Service(binary_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
#driver = webdriver.Chrome(options=options)
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
# querystring = {"language":"en","currency":"USD","c":"3510556","offset":"0","sitepath":"/sca/searchApi.ssp","sort":"custitem_ns_sc_ext_ts_90_amount:desc","use_pcv":"F","fieldset":"search","n":"2","include":"facets","limit":"100","country":"US","pricelevel":"4"}

# payload = ""
# headers = {
#     "cookie": "NLShopperId2=_hLrdW4VA2FxSWc_; NLVisitorId=UZwMgW4VA2JxSe9n; NS_VER=2023.1; JSESSIONID=LJP8QsG021ZSXl-WlsMsgDXgBSgZHFJyNVEgHlR05ddj8uGSa79_yjdOXkB9u86PZ3sUeANxlhxw_SWm5242yuV4AneSHr_H6_-YHQwm6Hld2Koj-HHOBf0G8_dKqmj9\u0021154194789; chrole=1125:306749:2dd353aa; jsid_own=3510556.-83967632; SSPOperationId_ba51ba3a=05a1be0e-9ef2-4d9e-a814-5c739fd0c85a; SSPOperationId_2ec15251=890cd3ca-a0d7-4212-a099-887e978a4deb; SSPOperationId_6208967a=3d516026-14a1-46d1-909e-f78fb9e90333; recentlyViewedIds=[60596%2C65939]; SSPOperationId_6480fef=9a614971-3e7a-45a3-94e9-6d4123506b50",
#     "authority": "connect.soligent.net",
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-language": "en-US,en;q=0.9",
#     "cache-control": "no-cache",
#     "dnt": "1",
#     "pragma": "no-cache",
#     "referer": "https://connect.soligent.net/search",
#     "sec-ch-ua-mobile": "?0",

#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "sec-gpc": "1",
#     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
#     "x-requested-with": "XMLHttpRequest",
#     "x-sc-touchpoint": "shopping"
# }

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
