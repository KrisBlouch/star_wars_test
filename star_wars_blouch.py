#!/bin/python

#challenge1: List the name and length of all starships
#that are less than 20 meters in length

#challenge2: List the name and length of all starships
#that are less than 20 meters in length that also
#appeared in “Revenge of the Sith

import requests
import json
from itertools import chain

pages = range(1,5)
starships_results = {}

print("These are the ships less than 20 meters:")

for page in pages:
    api = "https://swapi.dev/api/starships/?page=" + str(page)
    #print(api)
    response = requests.get(api)
    #print(response)
    starships_json = response.json()
    starships_results = starships_json["results"]
    count = len(starships_results)
    #print(count)
    count_list = list(range(0,count,1))
    #print(count_list)
    for var in count_list:
     s_length = (starships_results[var]["length"]).replace(",","")
     s_length = int(float(s_length))
     #print(s_length)
     if s_length < 20:
        print(starships_results[var]["name"])
        #print(starships_results[var]["length"])


print("\nThese ships were in Episode 3, Revenge of the Sith and are less than 20 meters:")
for page in pages:
  api = "https://swapi.dev/api/starships/?page=" + str(page)
  # print(api)
  response = requests.get(api)
  # print(response)
  starships_json = response.json()
  starships_results = starships_json["results"]
  count = len(starships_results)
  # print(count)
  count_list = list(range(0, count, 1))
  # print(count_list)
  for var in count_list:
     s_length = (starships_results[var]["length"]).replace(",", "")
     s_length = int(float(s_length))
     movies = (starships_results[var]["films"])
     movies_flat = list(chain.from_iterable(movies))
     #print(movies_flat)
     if "3" in movies_flat:
         sith_true = True
     else:
         sith_true = False
     #print(sith_true)
     #print(s_length)
     if s_length < 20 and sith_true:
       print(starships_results[var]["name"])
       #print(starships_results[var]["length"])
       #print(movies)


#print(starships_results)



#


#debug
#print(type(starships_json))

#print(starships_json)

#print(starships_json[1, "length"])

#don't need this, already returning a dictionary
#ship_index = json.loads(starships_json)

#ship_length = print(ship_index["length"])

#print(ship_length)

#count = range(36)