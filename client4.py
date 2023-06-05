import socket
from pythonping import ping
s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
c, addr = s.accept()

while True:
   ip=c.recv(1024).decode()
   try:
       c.send(str(ping(ip,verbose=False)).encode())
   except KeyError:
       c.send("Not found".encode())

