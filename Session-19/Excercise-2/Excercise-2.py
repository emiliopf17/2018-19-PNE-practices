# Example of getting information about the weather of
# a location
import http.client
import json
import sys



capital_city=input("Put a capital city that you would like to know the weather:")
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query="+capital_city
METHOD = "GET"
headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)
# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status


# -- Read the response's body and close
# -- the connection
raw = r1.read().decode("utf-8")
conn.close()
info = json.loads(raw)
if len(info)==0:
    print("Sorry but this city doesn´t exist or the web not have information")
    sys.exit()
#print(info)
woeid=info[0]['woeid']

ENDPOINT = "/api/location/"
conn.request(METHOD, ENDPOINT + str(woeid) + '/', None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
weather = json.loads(text_json)

# -- Get the data
time = weather['time']
temp0 = weather['consolidated_weather'][0]

description = temp0['weather_state_name']
temp = temp0['the_temp']
place = weather['title']
sun_set=weather['sun_set']

print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Sun set time: {}".format(sun_set))
print("Weather description: {}".format(description))
print("Current temp: {} degrees".format(temp))














