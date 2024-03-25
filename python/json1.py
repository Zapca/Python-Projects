import urllib.request
import json 

url=input('Enter a URL: ')
print('Retreiving',url)
data=urllib.request.urlopen(url)
js_data=data.read().decode()
print(len(js_data),'characters')

js=json.loads(js_data)

total_value=0
for i in js['comments']:
    total_value+=i['count']
    print(i['count'])

print('Sum',total_value)