import requests
from bs4 import BeautifulSoup
a='https://www.sakshi.com/tags/farmers-protest'
b=requests.get(a)
title=[]
news=[]
date=[]
link=[]
dd='https://www.sakshi.com'
c=BeautifulSoup(b.content,'lxml')
for j in c.find_all('div',{'class':'view view-taxonomy-term view-id-taxonomy_term view-display-id-page view-dom-id-68c108575c8482510e0f518dd8756a83'}):
    for i in j.find_all('div',{'class':'views-field views-field-title'}):
        title.append(i.text)
        for k in i.find_all('a',href=True):
            link.append(dd+k['href'])
    for i in j.find_all('div',{'class':'views-field views-field-changed'}):
        date.append(i.text)
    for i in j.find_all('div',{'class':'views-field views-field-body'}):
        news.append(i.text)
for i in range(len(news)):
    print(" "+str(i+1))
    print(date[i])
    print(title[i])
    print(news[i])
    print(link[i])
    print("-----------(**)------------")
