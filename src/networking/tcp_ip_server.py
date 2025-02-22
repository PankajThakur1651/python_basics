import socket

host = 'localhost'
port = 4242
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s. bind((host, port))
print('Server listening on port {}'.format(port))
s.listen(1)
c, addr = s.accept()
print("Connection from{}".format(str(addr)))

for i in range (0,10):
    data = input("Send data to client")
    c.send((data + "\n").encode())  # Add newline and encode

c.close()