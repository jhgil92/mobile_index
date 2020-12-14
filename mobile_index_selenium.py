from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = ''
password = ''
auth = ''

driver = webdriver.Chrome("C:/workspace/python/chromedriver/chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://hd.mobileindex.com/member/login?url=https%3A%2F%2Fhd.mobileindex.com%2F")

def log_in_mobile_index(driver, email, password, auth):
    driver.find_element_by_name('igawEmail').send_keys(email)
    driver.find_element_by_name('igawPw').send_keys(password)
    driver.find_element_by_css_selector('.btn--sign').click()
    time.sleep(1.5)
    driver.find_element_by_name('authKey').send_keys(auth)
    driver.find_element_by_css_selector('body > div.frm--sign > div.sign-box > div.sign-box__area-for-form > main > form > div.form__main > a').click()
    time.sleep(1.0)
    driver.find_element_by_css_selector('#md-certkey-checked > div > div > div.modal-footer.justify-content-center > button.btn.btn-primary').click()
    time.sleep(1.0)

def go_to_rank(driver):
    driver.get("https://hd.mobileindex.com/rank/biz?cm=%EA%B8%88%EC%9C%B5&genre=%EC%A6%9D%EA%B6%8C/%ED%88%AC%EC%9E%90&c=76")
    time.sleep(1.0)

def change_date_rank(driver, date = '2020-12-01'):
    element = driver.find_element_by_css_selector('#eDay')
    element.clear()
    element.send_keys(date)
    element.send_keys(Keys.ENTER)
    time.sleep(2.5)

def download_btn_click(driver):
    element = driver.find_element_by_css_selector('body > div.frm > main > div.content > div > div.boundarybar > div:nth-child(5) > a')
    element.click()
    time.sleep(2.5)

def get_daily_rank(driver, date):
    change_date_rank(driver, date)
    download_btn_click(driver)
    print(f'{date} download done')

import pandas as pd
dates = pd.date_range(start="2020-11-11",end="2020-11-13").tolist()
dates = [pd.Timestamp.strftime(x, '%Y-%m-%d') for x in dates]

log_in_mobile_index(driver)
go_to_rank(driver)
for date in dates:
    get_daily_rank(driver, date)
