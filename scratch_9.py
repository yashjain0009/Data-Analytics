from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import openpyxl
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
from bs4 import BeautifulSoup
options=Options()
options.page_load_strategy='none'
path='/Users/yashjain/Downloads/chromedriver'
driver=webdriver.Chrome(path,options=options)
faculty_list=driver.get("https://www.rotman.utoronto.ca/FacultyAndResearch/Faculty/FacultyBios")
url="https://www.rotman.utoronto.ca/FacultyAndResearch/Faculty/FacultyBios"
source=requests.get(url).text
faculty_soup=BeautifulSoup(source,'lxml')
links=faculty_soup.findAll('li',class_='clearfix')
print links.text
y=0
faculty_name_list=[]
website=[]
email=[]
cv=[]
position=[]
dept=[]
name=[]
expertise=[]

#wb=openpyxl.Workbook()
#ws1 = wb.create_sheet("London School of Economics ")
#ws1.title = "Schulich"
y=0
for link in links:
    y+=1
    faculty_list = link.find('a')
    #print (y)
    faculty_name_list.append(faculty_list.text)
for i in range (0,len(faculty_name_list)):
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    #y += 1

    try:
        mai = WebDriverWait(driver, 5, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.LINK_TEXT, faculty_name_list[i]))

        )
        mai.click()
        urlpage = driver.current_url
        source = requests.get(urlpage).text
        soup = BeautifulSoup(source, 'lxml')
        basic_info=soup.find('div',class_='mediaBody')
        name.append(soup.find('div',class_='col-md-12').h2.text)
        position.append(soup.findNext('div',class_='col-md-12').h2.text)

        print name
    except:
        pass



