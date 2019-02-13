import socket
from Seq import Seq
IP = "212.128.253.97"
PORT = 8083
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT)
while True :
    message = input("Type your sequence: ")
    if message == "Goodbye":
        break

    s.send(str.encode(message))
    txt= s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER: /n")
    print(txt)
    s.close()