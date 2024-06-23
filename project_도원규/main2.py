import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver=webdriver.Chrome('/home/bdh/chromedriver',chrome_options=chrome_options)

driver.implicitly_wait(3)
driver.get('https://portal.korea.ac.kr/front/Intro.kpd')
login_x_path='/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/div/form/input'
driver.find_element_by_name('id').send_keys('iceman1011')
driver.find_element_by_name('pw').send_keys('pincet84!@#')
driver.find_element_by_x_path(login_x_path).click()

url_sample ='<https://portal.korea.ac.kr/front/Main.kpd>'