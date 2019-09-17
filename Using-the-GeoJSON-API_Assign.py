import urllib.request, urllib.error, urllib.parse
import json
import ssl

end_point = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42 #this is required for connecting to the end_point

#ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
# address = 'South Federal University'

parms = dict()
parms['address'] = address
parms['key'] = api_key

url = end_point + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context = ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None
if not js or 'status' not in js or js['status'] != 'OK':
    print('=== Failure To Retrieve ====')
    print(data)
    exit()

# print(json.dumps(js, indent = 4))
print(js['results'][0]['place_id'])
