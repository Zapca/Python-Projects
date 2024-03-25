import urllib.request,urllib.parse
import json 
import ssl

serviceurl='https://py4e-data.dr-chuck.net/json?'

ctf=ssl.create_default_context()
ctf.check_hostname=False
ctf.verify_mode=ssl.CERT_NONE

parameters={}
while True:
    address=input('Enter a Address: ')
    if len(address)<1:
        print('Enter a Valid Address')
        exit()

    parameters['address']=address
    parameters['key']=42

    url=serviceurl+urllib.parse.urlencode(parameters)
    print('Retrieving',url)
    ap=urllib.request.urlopen(url,context=ctf)
    data=ap.read().decode()
    print(len(data))

    try:js=json.loads(data)
    except:js=None

    if not js or 'status' not in js or js['status']!='OK':
        print('Tu Chutiya hai')
        continue

    print(json.dumps(js,indent=2))

    print('Place ID:',js['results'][0]['place_id'])
