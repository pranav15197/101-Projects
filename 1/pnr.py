from bs4 import BeautifulSoup
import urllib
import mechanize

url = "http://ipnrstatus.in/"

br  = mechanize.Browser()
br.set_handle_robots(False)
br.open(url)

br.select_form("pnrForm")
pnr = raw_input('enter pnr: ')
br['lccp_pnrno1'] = pnr#"8328145921"


response = br.submit()

r =  response.read()
soup  = BeautifulSoup(r)
i = 0;
for tr in soup.findAll('b'):
    i+=1
    if i==2:
        print"booking status ",
    elif i==3:
        print"current status ",
    print tr.getText()
    if i==3 :
        break
