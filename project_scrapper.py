from bs4 import BeautifulSoup
import requests
url="https://www.anderson.ucla.edu/faculty-and-research/decisions-operations-and-technology-management/faculty/ahmadi#tabItem-x145894"
source=requests.get(url).text
soup=BeautifulSoup(source,'lxml')
basic_info=soup.find('div',class_='faculty-bio-profile')
contact_details=soup.find('div',class_="display-email")
name= basic_info.h1.text
#position=basic_info.h2.text
#dept=basic_info.h3.text
#for contact in contact_details:
    #print contact.attrs
#    if contact.text=="Website":
#        website= (contact.attrs['href'])
#    if contact.attrs['href'].startswith("mailto:"):
#        email= contact.attrs['href'][7:]
desc=soup.find('div',class_='people__bio')
cv=(desc.find('a',href=True)).attrs['href']
expertise=(soup.find('div',class_='expertise')).text


print (name)
print (position)
print (dept)
print (website)
print (email)
print (cv)
print (expertise)