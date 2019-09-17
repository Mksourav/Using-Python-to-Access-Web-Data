import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:  ')
cnt= int(input('Enter count: '))
pos= int(input('Enter position: '))

print('Retrieving: ', url)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
count=0
p=0

for i in range(cnt):
   for tag in tags:
        link=(tag.get('href'))
        p=p+1
        if p==pos:
               print("Retrieving:", link)
               url = (link)
               html = urllib.request.urlopen(url, context=ctx).read()
               soup = BeautifulSoup(html, 'html.parser')
               tags = soup('a')
               count=count+1
               p=0
               break
