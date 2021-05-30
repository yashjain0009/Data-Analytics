from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from bs4 import BeautifulSoup
import numpy as np
path='/Users/yashjain/Downloads/chromedriver'
driver=webdriver.Chrome(path)
x=driver.get("https://www.lse.ac.uk/economics/people/faculty")
#search=driver.find_element_by_class_name('siteSearchTrigger')
#search.send_keys("masters")
#search.send_keys(return keys)

links=driver.find_elements_by_class_name("accordion__txt")
print links.text
x=np.array(links)
#for link in links:
#    print link.text
#    print (link.text).dtype
print x