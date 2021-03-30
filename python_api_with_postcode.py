# API for postcode.io

import requests

url = "http://api.postcodes.io/postcodes/"
postcode = "e147le"

url_arg = url + postcode
print(url_arg)

# to check status code
response = requests.get(url_arg)
print(response.status_code)

# json is a method of request
# converting data into dict
response_dict = response.json()
response_keys = response_dict["result"]
for items in response_dict.keys():
    if items == "postcode":
        print("Your postcode location is " + str(response_keys["result"]))

    if items == "longitude":
        print("Your longitude is " + str(response_keys["longitude"]))
    elif items == "latitude":
        print("your longitude is " + str(response_keys["latitude"]))


# another example of above code
for key, val in response_dict.items():
    print(key)
    if key == "result":
        #print(val['postcode'])
        print(response_dict[key]['postcode'])




# print(type(response_dict))






# To print the content of this website
# print(type(response.content))
# print(response.headers.keys())
# print(response.encoding.isdigit())
# print(response.is_redirect)
