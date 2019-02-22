from Seq import Seq
import socket
import termcolor
# Configure the Server's IP and PORT
PORT = 8082
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5


def dim (s1,comand):
    print("Making comand",comand)
    if (comand == "len"):
        return s1.len()
    elif (comand == "complement"):
        return s1.complement().get_strbase
    elif (comand == "countA"):
        return s1.count('A')
    elif (comand == "countC"):
        return s1.count('C')
    elif (comand == "countG"):
        return s1.count('G')
    elif (comand == "countT"):
        return s1.count('T')
    elif (comand =="percA"):
        return s1.perc("A")
    elif (comand =="percC"):
        return s1.perc("C")
    elif (comand =="percG"):
        return s1.perc("G")
    elif (comand =="percT"):
        return s1.perc("T")
    else:
        return("Error")


def validS(s):
    V = 'ACTG'
    for letter in s:
        if letter not in V:
            return False
        return True



def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    termcolor.cprint(msg,'red')
    if msg == '\n':
        response = 'ALIVE'
    else:#trozos= parts
        part = msg.split('\n')
        print("Rating", parts [0])
        if (validS(parts[0])):
            responde = 'OK\n'
            s1= Seq(parts[0])
            for i in range (1,len(parts)-1):
                print("Doing the comand",i,parts [i])
                r= dim (s1,parts[i])
                response =  response +str(r)+'\n'
        else:
            response = 'ERROR'
    # Print the received message, for debugging
    print("Request message: {}".format(msg))

    # Send the msg back to the client (echo)
    cs.send(str.encode(msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))