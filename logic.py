import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def prepare_browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.get('https://translate.google.com/?hl=ru')
    return browser


def get_translate(browser, text):
    browser.find_element_by_css_selector('#source').clear()
    browser.find_element_by_css_selector('#source').send_keys(text)
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tlid-translation'))
    )
    time.sleep(0.5)
    return browser.find_element_by_css_selector('.tlid-translation').text
