import socket as suck
import time

sock=suck.socket(suck.AF_INET,suck.SOCK_STREAM)
sock.connect(('data.pr4e.org',80))
sock.send('GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode())
count=0
picture=b''

while True:
    image=sock.recv(5120)
    if len(image)<1: break
    # We use time.sleep to delay the loop so that the server can keep up with the data sending and we get constant amount of data 
    time.sleep(0.25) # (Optional [Called as flow control])
    count=count+len(image)
    print(len(image),count)
    picture+=image

sock.close()

pic=picture.find(b'\r\n\r\n')
print(picture[:pic].decode())

fhand=open('Socket_Image.jpg','wb')
fhand.write(picture[pic+4:])
fhand.close()