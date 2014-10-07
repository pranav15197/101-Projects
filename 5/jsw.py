from bs4 import BeautifulSoup
import urllib
import mechanize

url = "http://jswinterns.biz/forgot_password.aspx"

br  = mechanize.Browser()
br.set_handle_robots(False)
br.open(url)


br.form = list(br.forms())[0]
pnr = raw_input('enter email ')
br['txtUsername'] = pnr

#response = br.submit()

#r =  response.read()
#print r

#soup  = BeautifulSoup(r)
