from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = ''
password = ''
authkey = ''

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("no-sandbox")
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
browser = webdriver.Chrome("C:/workspace/python/chromedriver/chromedriver.exe")
browser.get("https://hd.mobileindex.com/member/login?url=https%3A%2F%2Fhd.mobileindex.com%2F")

def log_in_mobile_index(browser, email, password, authkey):
    browser.find_element_by_name('igawEmail').send_keys(email)
    browser.find_element_by_name('igawPw').send_keys(password)
    browser.find_element_by_css_selector('.btn--sign').click()
    time.sleep(1.5)
    browser.find_element_by_name('authKey').send_keys(authkey)
    browser.find_element_by_css_selector('body > div.frm--sign > div.sign-box > div.sign-box__area-for-form > main > form > div.form__main > a').click()
    time.sleep(1.0)
    browser.find_element_by_css_selector('#md-certkey-checked > div > div > div.modal-footer.justify-content-center > button.btn.btn-primary').click()
    time.sleep(1.0)

def go_to_rank(browser):
    browser.get("https://hd.mobileindex.com/rank/biz?cm=%EA%B8%88%EC%9C%B5&genre=%EC%A6%9D%EA%B6%8C/%ED%88%AC%EC%9E%90&c=76")
    time.sleep(0.5)

def change_date_rank(browser, date = '2020-12-01'):
    element = browser.find_element_by_css_selector('#eDay')
    element.clear()
    element.send_keys(date)
    element.send_keys(Keys.ENTER)
    time.sleep(3)

def download_btn_click(browser):
    element = browser.find_element_by_css_selector('body > div.frm > main > div.content > div > div.boundarybar > div:nth-child(5) > a')
    element.click()
    time.sleep(3)

def get_daily_rank(browser, date):
    change_date_rank(browser, date)
    download_btn_click(browser)
    print(f'{date} download done')

import pandas as pd
dates = pd.date_range(start="2020-05-01",end="2020-11-05").tolist()
dates = [pd.Timestamp.strftime(x, '%Y-%m-%d') for x in dates]

log_in_mobile_index(browser, email, password, authkey)
go_to_rank(browser)
for date in dates:
    get_daily_rank(browser, date)
