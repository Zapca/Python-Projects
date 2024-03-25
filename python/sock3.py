import socket as su

socks=su.socket(su.AF_INET,su.SOCK_STREAM)
socks.connect(('data.pr4e.org',80))
socks.send('GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode())

body=' '
while True:
    data=socks.recv(512).decode()
    if len(data)<1 : break
    body+=data

whitespace_find=body.find('\r\n\r\n')
print(body[whitespace_find+4:])