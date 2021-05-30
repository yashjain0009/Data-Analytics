import urllib3
from bs4 import BeautifulSoup as soup
import requests
http=urllib3.PoolManager()
url='https://www.london.edu/faculty-and-research/strategy-and-entrepreneurship/faculty-profiles#sort=%40profilesurname%20ascending'
url2='https://www.amazon.in/gp/product/B07HMTGJ3T?pf_rd_r=KRS4MC4H97M5PG2B48T9&pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4'
uclient=http.request("GET",url)
x=requests.get(url)
page_html=uclient.read()
page_soup=soup(uclient.data,features='lxml')
page=soup(x.content,'html.parser')
#print page
#print page_soup.body.main
container= page_soup.find_all_next('div',{"class":"coveo-list-layout CoveoResult"})
container2= page.find_all('span',class_="a-profile-name")
print (container)
print container2
