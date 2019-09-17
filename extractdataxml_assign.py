import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', address)
    xml = urllib.request.urlopen(address, context=ctx).read()

    print ("Retrieved: " , str(len(xml)) + " characters")

    tree = ET.fromstring(xml)

    counts =  tree.findall('.//count')
    print ("Count: " + str(len(counts)))

    accumulator = 0

    for count in counts:
        accumulator += int(count.text)

    print ("Sum:" + str(accumulator))
    break


# url = input("Enter location: ")
# if len(url) < 1:
#     url = "http://python-data.dr-chuck.net/comments_242051.xml"
# print ("Retrieving " + url)
#
# xml = urllib.request.urlopen(url).read()
# print ("Retrieved: " + str(len(xml)) + " characters")
#
# tree = ET.fromstring(xml)
#
# counts =  tree.findall('.//count')
# print ("Count: " + str(len(counts)))
#
# accumulator = 0
#
# for count in counts:
#     accumulator += int(count.text)
#
# print ("Sum:" + str(accumulator))
