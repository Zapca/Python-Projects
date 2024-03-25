import urllib.request
from bs4 import BeautifulSoup

url=input('Enter URL:')
count=int(input('Enter count:'))
pos=int(input('Enter position:'))-1

if len(url)<1:
    url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'

def openurl(chicken):
    cmd=urllib.request.urlopen(chicken).read()
    soup=BeautifulSoup(cmd,'html.parser')
    return soup

while True:
    chicken_soup=openurl(url)
    tags=chicken_soup('a')
    url=[tag.get('href',None) for tag in tags][pos]
    print('Retreiving:',url)
    count-=1
    if count==0:break