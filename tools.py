print (" ############################################ " )
print (" ###########            ######   ############ " )
print (" ####################   ######   ############ " )
print (" ####################   ######   ############ " )
print (" ###########                     ############ " )
print (" ###########   ######   ##################### " )
print (" ###########   ######   ##################### " )
print (" ###########   ######            ############ " )
print (" ############################################ " )

print ("                Tools : By Lia                " )


from time import sleep
from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get('https://www.instagram.com/')

login = chrome.find_element_by_xpath("//a[text()='Log in']")
login.click()

username = chrome.find_element_by_css_selector("input[name='username']")
password = chrome.find_element_by_css_selector("input[name='password']")

username.send_keys("<your username>")
password.send_keys("<your password>")

login = chrome.find_element_by_xpath("//button[@type='submit']")

sleep(5)
chrome.close()
