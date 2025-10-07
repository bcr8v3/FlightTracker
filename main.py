# step 1: import requests
import requests
from dotenv import dotenv_values

# step 2: call api with given endpoint and key
key = dotenv_values(".env")["secret_key"]
response = requests.get(f"https://api.aviationstack.com/v1/flights?access_key={key}")

#print(response.json())
# step 3: convert to dictionary and grab only the "data" value

response = response.json()
response_data = response.get("data")



# step 4: loop through the flights and check which flights are active

for i in response_data:
    if i.get("flight_status") == "active": # step 5: if active, print the airline, date, departure airport and arrival airport
        print("Flight airline: ", (i.get("airline")).get("name"))
        print("Flight date: ", (i.get("flight_date")))
        print("Departure Airport: ", (i.get("departure")).get("airport"))
        print("Arrival Airport: ", (i.get("arrival")).get("airport"))
        print("----------------------------------------------------------")