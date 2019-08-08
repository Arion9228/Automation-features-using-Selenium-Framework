#!/usr/bin/env python
# coding: utf-8

# In[47]:


#importing the required Modules
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#Provide the URL of the Page you want to check
url = input("Enter the Url to check for Broken Links: ")
print("\n")

#Running the Chrome Driver
driver = webdriver.Chrome(executable_path="C:\\Users\\Acer\\Desktop\\driver\\chromedriver")

#Fetching the required Page
driver.get(url)

#Creating a list named "links" to store all the hyperlinks
links = driver.find_elements_by_css_selector('a')

#Intializing Counter
count=0

#Searching for Broken Links
for link in links:
    #Setting the Status Code to a variable "r"
    r = requests.head(link.get_attribute('href')).status_code
    #If status code is not equal to 200, then it implies that the link is Broken
    if (r != 200):
        #Printing the Broken Links With their respective Status Code
        print(link.get_attribute('href'), "Broken Link!\n", "Status Code: ", r,"\n")
        count+=1

#Total Broken Links Found
print("Total Broken Links: ", count)

#Closing and Quitting the Driver
driver.close()
driver.quit()


# In[ ]:





# In[ ]:




