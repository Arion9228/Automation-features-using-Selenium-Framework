#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing the required modules
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import json

#Taking the Keyword to be searched
keyword=input("Enter the Keyword: ")
#Defining the number of images to download
num_requested=10

#Defining the extensions type
extensions = {"jpg", "jpeg", "png", "gif"}

#Providing thr File Download Path
file_path="C:\\Users\\Acer\\Pictures\\GRIP\\"

#Providing the Driver Path
driver = webdriver.Chrome(executable_path="C:\\Users\\Acer\\Desktop\\driver\\chromedriver")
#Fetching the Google Images Page
driver.get("https://www.google.com/imghp?hl=en")

#Selecting and inputting the Keyword in the Search Bar
driver.find_element_by_css_selector("#sbtc > div.SDkEP > div.a4bIc > input").send_keys(keyword)
#Clicking on Search Button
driver.find_element_by_css_selector("#sbtc > div.cafKYd > button").click()

#Waiting Time
driver.implicitly_wait(3)

#Fetching the Images required and stroing them in the list called "images"
images = driver.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
#Defining the Initial Counter
count=1
for i in range(0,num_requested):
    #Fetching the URL of the Image
    img_url = json.loads(images[i].get_attribute('innerHTML'))["ou"]
    
    #Fetching the TYPE of image
    img_type = json.loads(images[i].get_attribute('innerHTML'))["ity"]
    
    #Providing the Path and name of the Download Image
    full_path = file_path +keyword +"_" + str(count) + '.jpg'
    
    #Error Handling for HTTP Error
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    
    #Retrieving the Images
    urllib.request.urlretrieve(img_url, full_path)
    
    #Printing the Image URL
    print("Image Url: "+str(img_url))
    #Printing the information of the Download Image
    print("Download " + str(count) + " of 10 COMPLETED!"+"\n")
    count+=1
    
    #Exception Handling for Invalid Extension
    try:
        if img_type not in extensions:
            img_type = "jpg"
    except Exception as e:
        print ("Download failed:", e)
        
#Wait
driver.implicitly_wait(10)

#Closing and Quitting the Driver
driver.close()
driver.quit()


# In[ ]:





# In[ ]:




