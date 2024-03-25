import urllib.request

url=input('Enter a URL:')
shand=urllib.request.urlopen(url)

for files in shand:
    print(files.decode().strip())