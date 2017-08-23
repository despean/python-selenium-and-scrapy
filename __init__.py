#facebook signup script using selenuim firefox web drivers




from selenium import webdriver as wb


browser = wb.Firefox()
browser.get('http://facebook.com')

# email = browser.find_element_by_name('email')
# password = browser.find_element_by_name('pass')
# login = browser.find_element_by_id('u_0_p')
#
# email.send_keys('')
# password.send_keys('')
# login.click()

def click_options_value( select, value):
    for slm in select.find_elements_by_tag_name('option'):
        if str(slm.get_attribute('value')) == value:
            slm.click()

first ='asher'
last= 'john'
email_a = ''
password = ''
sex_fm =['1', '2']
month_ = '5'
day ='5'
year= '1984'

firstname = browser.find_element_by_name('firstname')
lastname = browser.find_element_by_name('lastname')
email = browser.find_element_by_name('reg_email__')
conf_email = browser.find_element_by_name('reg_email_confirmation__')
reg_pass = browser.find_element_by_name('reg_passwd__')
sex = browser.find_elements_by_name('sex')
birth_month =browser.find_element_by_name('birthday_month')
birth_day =browser.find_element_by_name('birthday_day')
birth_year =browser.find_element_by_name('birthday_year')

create_acount = browser.find_element_by_id('u_0_g')

#setting values

firstname.send_keys(first)
lastname.send_keys(last)
email.send_keys(email_a)
conf_email.send_keys(email_a)
reg_pass.send_keys(password)
for sex in sex:
   if str(sex.get_attribute('value')) == '1':
       sex.click()

click_options_value(birth_month, month_)
click_options_value(birth_day, day)
click_options_value(birth_year, year)

create_acount.click()

xpath ='//*[@id="m_-4332863546320661342email_content"]/table/tbody/tr[5]/td[2]/table/tbody/tr[2]/td[1]'



