import urllib.request, urllib.parse, urllib.error
import ssl
import json

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

address = input('Enter location: ')

parms = dict()
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', address)
data = urllib.request.urlopen(address, context=ctx).read()

print ("Retrieved: " , str(len(data)) + " characters")

js = json.loads(data)

sum = 0
total_number = 0

for comment in js["comments"]:
    sum += int(comment["count"])
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
