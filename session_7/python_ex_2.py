import socket
IP="212.128.253.64"
PORT = 8080
while True:
    msg=input("Type a message: ")
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP,PORT))
    msg= s.recv(2048).decode("utf-8")
    print("Messaage from the server: /n")
    print(msg)
    s.close()