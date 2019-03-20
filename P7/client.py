import http.client
import json
from Seq import Seq

#Port and server
PORT = 80
SERVER = 'rest.ensembl.org'


conn = http.client.HTTPConnection(SERVER, PORT)

#Find the id of the DNA seq
conn.request("GET", "/homology/symbol/human/FRAT1?content-type=application/json")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))

data1 = r1.read().decode("utf-8")
response = json.loads(data1)
id=response['data'][0]['id']
print(id)


conn.request("GET", "/sequence/id/"+id+"?content-type=application/json")
r1 = conn.getresponse()
data1=r1.read().decode("utf-8")
response = json.loads(data1)
print(response)
chain=response['seq']
print(chain)

s1= Seq(chain)

#Number of bases of DNA seq
print("The total of bases in the DNA seq is :", len(chain))


#Number of T nucleotids in the DNA chain
print ("Number of bases of T:", s1.count('T'))

#Which nucleotid has more presence in the DNA chain and his percetage
if s1.count('A')>s1.count('T') and s1.count('A')>s1.count('G') and s1.count('A')>s1.count('C'):
    print("The most repeted nucleotid is A and its repited",s1.count('A')," times and his percentage is",s1.perc('A'),"%")
elif s1.count('C')>s1.count('T') and s1.count('C')>s1.count('G') and s1.count('C')>s1.count('A'):
    print("The most repeted nucleotid is C and its repited",s1.count('C'),"times and his percentage is",s1.perc('C'),"%")
elif s1.count('T')>s1.count('A') and s1.count('T')>s1.count('G') and s1.count('T')>s1.count('C'):
    print("The most repeted nucleotid is T and its repited",s1.count('T'),"times and his percentage is",s1.perc('T'),"%")
elif s1.count('G')>s1.count('T') and s1.count('G')>s1.count('A') and s1.count('G')>s1.count('C'):
    print("The most repeted nucleotid is G and its repited",s1.count('G'),"times and his percentage is",s1.perc('G'),"%")


#Percentage al nucleotids
print ("The percentage of T is", s1.perc('T'),"%")
print ("The percentage of A is", s1.perc('A'),"%")
print ("The percentage of C is", s1.perc('C'),"%")
print ("The percentage of G is", s1.perc('G'),"%")

