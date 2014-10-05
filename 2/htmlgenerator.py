from bs4 import BeautifulSoup
import json
import webbrowser
import urllib2
base_url = "http://9gag.com"
url = ""


nsfwcount = 0  
for i in range(1,5):
    file = open('url.txt','r')
    url = file.read()
    file.close()
   
    html=''
    s = urllib2.urlopen(url)
    s = s.read()
    nexturl = ''
    data = json.loads(s)
    j=0
    for post in data['data']['posts']: 
        j+=1
        title =  post['title'].encode('ascii', 'ignore')
        href  =  post['sourceUrl'].encode('ascii', 'ignore')
        src   =  post['ogImageUrl'].encode('ascii', 'ignore')
        src   =  src.replace('\\','')
        if 'NSFW' in title:
            nsfwcount+=1
            html += '<li><a href="'+href+'">'+title+'</a><br><img src="'+src+'"></li>\n'
        html += ''
        if j==50:
            nexturl = post['nextPostId']
    url = "http://9gag.tv/api/index/LJEGX?ref_key="+nexturl+"&count=50&direction=1&includeSelf=0"
    file = open('url.txt','w')
    file.write(url)
    file.close()
    
    file = open('110.html','a')
    file.write(html)
    file.close()
webbrowser.open('110.html')
    


