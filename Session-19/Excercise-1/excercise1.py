import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/random"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()


# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
#print(text_json)

# -- Generate the object from the json file
jockes = json.loads(text_json)
print("The random jocke about Chuck Norris is:",jockes['value']['joke'])

#to get the ntype of categories
ENDPOINT = "/categories"
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()


# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
#print(text_json)

# -- Generate the object from the json file
total = json.loads(text_json)
categories = total ["value"]
print("The length of the categories is",len(categories))
for i in categories:
    print("One category is",i)

ENDPOINT = "/jokes/count"
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()


# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
#print(text_json)

# -- Generate the object from the json file
count_jockes = json.loads(text_json)
print("The total number of jockes about Chuck Norris are",count_jockes['value'])

