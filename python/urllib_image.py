import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('urllib_image.jpg', 'wb')

for data in img:
    fhand.write(data)
fhand.close()