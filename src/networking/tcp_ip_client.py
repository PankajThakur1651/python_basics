import  socket

s = socket.socket()
s.connect(('localhost', 4242))

msg = s.recv(1024)

while msg:
    print("Received  \n", msg.decode())
    msg = s.recv(1024)

s.close()