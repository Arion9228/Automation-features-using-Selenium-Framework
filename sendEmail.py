#!/usr/bin/env python
# coding: utf-8

# In[40]:


#Importing the required Modules
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#Collecting the Target Mail ID
mail_id = input("Please Provide the Target Mail ID: ")
#Subject of Mail
sub = input("Please Enter the Subject: ")
#Description of Mail
desp = input("Please Enter the Mail: ")
#Setting up Chrome_Driver 
driver = webdriver.Chrome(executable_path="C:\\Users\\Acer\\Desktop\\driver\\chromedriver")

#Providing the Gmail URL
driver.get("http://www.gmail.com")

#Inputting the Source Email ID
driver.find_element_by_name("identifier").send_keys("karasuno.angel@gmail.com")
#Clicking Next Button
driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()

#Wait
driver.implicitly_wait(1)

#Inputting the password
driver.find_element_by_name("password").send_keys("ComeFly1")

#Delay for error Handling
element = WebDriverWait(driver, 0).until(
EC.invisibility_of_element_located((By.ID, "ANuIbb IdAqtf"))
)

#Clicking the Next Button after Inputting Password
driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()

#Wating time to completely open the Source Mail ID
driver.implicitly_wait(5)

#Fetching the "Compose Mail" using css_selector
driver.find_element_by_css_selector(".aic .z0 div").click()

#Providing the Target Mail ID
driver.find_element_by_css_selector(".oj div textarea").send_keys(mail_id)
#Providing the Subject
driver.find_element_by_css_selector(".aoD.az6 input").send_keys(sub)
#Providing Mail Description
driver.find_element_by_css_selector(".Ar.Au div").send_keys(desp)

#Clicking on Send Mail using css_Selector
driver.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3").click()
#Waiting Time
driver.implicitly_wait(5)

#Clicking on the Source ID Profile
driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a/span").click()

#Waiting to check for "Sent Mail" Notification
driver.implicitly_wait(3)
element = WebDriverWait(driver, 0).until(
EC.invisibility_of_element_located((By.ID, "J-J5-Ji"))
)

#Logging Out of the Source ID
driver.find_element_by_css_selector("#gb_71").click()

#Waiting time for proper functioning
driver.implicitly_wait(5)

#Closing & Quitting Driver
driver.close()
driver.quit()


# In[ ]:





# In[ ]:




