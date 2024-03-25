import socket as su 

url=input('Enter a Url: ')
hostname=url.split('/')[2]
sock=su.socket(su.AF_INET,su.SOCK_STREAM)

try: sock.connect((hostname,80))
except:
    print('Please Recheck the provided Url !!!') 
    exit()

sock.sendall(f'GET {url} HTTP/1.0\r\n\r\n'.encode())

data_recv=''

while True:
    data=sock.recv(512).decode()
    data_recv+=data
    if len(data)<1 or len(data_recv)>=3000:break

totalchar=data_recv[:3000]
print(totalchar,'\nTotal Charaters:',len(totalchar),'\n',end='')

sock.close()