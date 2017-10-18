# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#http://py4e-data.dr-chuck.net/known_by_Fikret.html
#http://py4e-data.dr-chuck.net/known_by_Jago.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = 'http://py4e-data.dr-chuck.net/known_by_Jago.html'
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = input('Enter count: ')
position = input('Enter position: ')
#count = 7
#position = 18

#while True:
i = 0
while i < int(count):
      i= i+1
      html = urllib.request.urlopen(url, context=ctx).read()
      soup = BeautifulSoup(html, "html.parser")

      try:
            url = soup.find_all('a')[int(position)-1]["href"]
            print(url)
            x = re.findall('[a-z]+_([a-zA-Z]+).html' ,url)
            print(x[0])
      except IndexError:
            break  


