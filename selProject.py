from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome('/Users/amrs/Downloads/chromedriver') #initializing the chrome webdriver and open browser
driver.get('https://mail.google.com') #open the website mentioned
try:
    link = driver.find_element_by_link_text('Sign In')
    link.click()
except:
    sleep(1)
    
email = driver.find_element_by_id('identifierId') #find the input field to enter email id

email.send_keys('your_mail_id_@gmail.com') #type in your required mail id

nxt = driver.find_element_by_id('identifierNext')
nxt.click() #click the next button for this email id

sleep(1)

password = driver.find_element_by_name('password') #find password input field

password.send_keys('*********') #type in your required password
sleep(1)
driver.find_element_by_id('passwordNext').click() #to signin with this password option
sleep(3)

#wait till the email is open and signout option is visible
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a"))
    )
finally:
	sleep(1)
	driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a").click()
	sleep(1)
	driver.find_element_by_id('gb_71').click()

sleep(1)
driver.close()

