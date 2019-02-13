import socket
from Seq import Seq
IP = "212.128.253.97"
PORT = 8082
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
while True:
    message = input("Type your sequence: ")
    if message == "Goodbye":
        break

    s1  =Seq(message)
    s2 = s1.complement()
    s3 = s1.reverse()
    text1 = "The complementary sequence is : "+ s2.strbase
    text2 = "The reverse sequence is : " + s3.strbase
    s.send(str.encode(text1))
    s.send(str.encode(text2))

    txt= s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER: /n")
    print(txt)
    s.close()

