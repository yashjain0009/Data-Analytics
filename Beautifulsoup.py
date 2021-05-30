from bs4 import BeautifulSoup
import requests
url="https://telfer.uottawa.ca/en/directory/abdoulkadre-ado/"
source=requests.get(url).text
soup=BeautifulSoup(source,'lxml')
print(soup.findAll('div',class_='col-auto'))
expertise =soup.find(id='research_areas')
print expertise.text
print info
span=(info.find('span'))

email=span.find('a')
print email.attrs






cl=soup.findAll('div')
dept=soup.find('header',class_='people__header')
expertise=soup.find('div',class_='expertise')
summary=soup.findAll('a',class_="peopleContact__link")
topic=expertise.findAll('span')
desc=soup.find('div',class_='people__bio')
website=desc.find('a',class_='external')
#expertise
teching=desc.find()
cv=desc.findAll('a',href=True)
#x=summary.find('div',class_="details")
#x=summary.find('script',class_="result-template")
#print summary.text
#print dept.h3.text
print expertise.text
#print expertise.p.span.text
#print website
#for x in topic:
#    print x.text
#print desc.text
print summary.a.text
for c in summary:
    if c.text=="Website":
        print (c.attrs['href'])

print
print
print
