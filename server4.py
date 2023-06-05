import socket
s=socket.socket()
s.connect(("localhost", 8000))
while True:
    ip=input("Enter the website you want to ping:")
     
    s.send(ip.encode())
    print(s.recv(1024).decode())


