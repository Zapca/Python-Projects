import urllib.request
from bs4 import BeautifulSoup

url=input('Enter a URL:')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_1745391.html'

cmd=urllib.request.urlopen(url).read()
souppy_time=BeautifulSoup(cmd,'html.parser')

tags=souppy_time('span')
lst=[int(tag.contents[0]) for tag in tags]
    
print(f'{len(lst)}\n{sum(lst)}')