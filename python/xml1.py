import urllib.request as ur_mom
import xml.etree.ElementTree as ET

url=input('Enter a URL: ')

xml=ur_mom.urlopen(url).read()
tree=ET.fromstring(xml.decode())

xml_lst=tree.findall('comments/comment')

count=[int(node.find('count').text) for node in xml_lst]
print(sum(count))