from requests_html import HTMLSession
session = HTMLSession()
url = "https://www.eenadu.net/tagsrelatednews/farmers%20protest"
pointer=session.get(url)
pointer.html.render()
titles = pointer.html.find('p')
newslist=[]

for item in titles:
    try:
        req=item.find('strong', first=True)
        temp={
        'title':req.text,
        }
        newslist.append(temp)
    except:
        pass

i=0
for item in newslist:
    print(i)
    print(item['title'])
    print(" ")
    i=i+1

