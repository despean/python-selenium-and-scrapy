



from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')

username_or_email =''
password = ''

try:
    username_email = browser.find_element(By.NAME,  'username')
    username_email.send_keys(username_or_email)
    nextbtn = browser.find_element(By.NAME,  'signin')
    nextbtn.click()
    passwd =WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, 'passwd')))
    passwd.send_keys(password)
    nextbtn = browser.find_element(By.NAME, 'signin')
    nextbtn.click()
    if browser.find_element(By.TAG_NAME, 'button').text == 'Looks good':
        gd = browser.find_element(By.TAG_NAME, 'button').text == 'Looks good'
        gd.click()
except NoSuchElementException:
      print('error', NoSuchElementException.msg)
