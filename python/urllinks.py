import urllib.request
from bs4 import BeautifulSoup 
import ssl 

certificate=ssl.create_default_context()
certificate.check_hostname=False
certificate.verify_mode=False

url=input('Enter a URL:')
data=urllib.request.urlopen(url,context=certificate).read()
html=BeautifulSoup(data,'html.parser')

print(len(html('p')),end=' ')