#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller
import time
import urllib.request
import os
from  selenium.webdriver.common.by import By

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def crawling_img(val):
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element("name", "q")
    elem.send_keys(searchKey)
    elem.send_keys(Keys.RETURN)

    imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd") 
    dir = "C:/Users/sungr/OneDrive/바탕 화면/imgs" + "//" + val
    print(imgs)
    createDirectory(dir) 
    count = 1
    for img in imgs: 
        if count > 5: 
            break
        try:
            img.click() 
            time.sleep(1)
            imgUrl  = driver.find_element(By.XPATH,
                f'//*[@id="islrg"]/div[1]/div[{count}]/a[1]/div[1]/img').get_attribute(
                "src")
            
            path = dir + "\\"
            urllib.request.urlretrieve(imgUrl, path + val + str(count) + ".jpg")
            count = count + 1
            if count >= 260:
                break
        except Exception as e:
            print(e)
    driver.close()

searchKey = input('검색 키워드 입력:')
crawling_img(searchKey)

