import urllib.request as ur

url=input('Enter a URL: ')
try: whand=ur.urlopen(url)
except: 
    print('Please Enter a Valid or Correct URL !!!')
    exit()

data=' '
for lines in whand:
    data+=lines.decode().strip()
    if lines<1 or data+lines>=3000 : break

data_limit=data[:3000]
print(data_limit,f'\n {print("Total Characters:",len(data_limit))}')