import socket as su

my_sock=su.socket(su.AF_INET,su.SOCK_STREAM)
my_sock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

while True:
    oh_yeah=my_sock.recv(1024)
    if len(oh_yeah)<1:
        break
    print(oh_yeah.decode())

my_sock.close()