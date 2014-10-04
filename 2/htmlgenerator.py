from bs4 import BeautifulSoup
import json
import urllib2
base_url = "http://9gag.com"
url = "http://9gag.tv/api/index/LJEGX?ref_key=9a8BV&count=50&direction=1&includeSelf=0"


nsfwcount = 0  
for i in range(1,50):
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
    print url
    print nsfwcount
    file = open('110.html','a')
    file.write(html)
    file.close()
    


