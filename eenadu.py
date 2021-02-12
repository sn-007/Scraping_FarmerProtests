from requests_html import HTMLSession
import sys
import os
width = os.get_terminal_size().columns
session = HTMLSession()
url = "https://www.eenadu.net/tagsrelatednews/farmers%20protest"
pointer=session.get(url)
pointer.html.render()
titles = pointer.html.find('p')
newslist=[]
desc=[]

for item in titles:
    # try:
    #     req=item.find('strong', first=True)
    #     temp={
    #     'title':req.text,
    #     }
    #     newslist.append(temp)
    # except:
    #     pass
    #collecting the sub part too
    try:
        if(item.find('strong') and item.find('a') ):
            req=item.find('a', first=True)
            temp={
            'desc':req.text
            }
            desc.append(temp)
    except:
        print(Exception)
        


i=0
# for item in newslist:
#     print(i)
#     print(item['title'])
#     print(" ")
#     i=i+1
sys.stdout = open("test.txt", "w")

for item in desc:
    print(i+1)
    print(item['desc'])
    print(" ")
    print("--------------------------!@@!--------------------------".center(width))
    print(" ")
    i=i+1

sys.stdout.close()