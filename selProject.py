from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox() #initializing the firefox webdriver and open browser
driver.get('https://mail.google.com') #open the website mentioned
try:
    link = driver.find_element_by_link_text('Sign In')
    link.click()
except:
    sleep(2)
    
email = driver.find_element_by_id('Email') #find the text field to enter email id

email.send_keys('username@gmail.com') #type in your required mail id

nxt = driver.find_element_by_id('next')
nxt.click() #click the next button

sleep(1)

password = driver.find_element_by_id('Passwd') #find password text field

password.send_keys('password') #type in your required password
sleep(1)
driver.find_element_by_id('PersistentCookie').click() #to deselect "keep me signed in" option
sleep(1)
sign = driver.find_element_by_id('signIn') #find the sign in button
sign.click()

driver.close()

