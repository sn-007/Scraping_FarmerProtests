from requests_html import HTMLSession
session = HTMLSession()
url = "https://news.google.com/topics/CAAqLAgKIiZDQkFTRmdvTkwyY3ZNVEZ0ZG1kd2VISndiQklGWlc0dFIwSW9BQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
pointer=session.get(url)
pointer.html.render(sleep=1, scrolldown=2)
titles = pointer.html.find('article')
newslist=[]

for item in titles:
    try:
        req=item.find('h3', first=True)
        temp={
        'title':req.text,
        'link':req.absolute_links
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

