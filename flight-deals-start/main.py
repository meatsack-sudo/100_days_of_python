#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from datetime import datetime, timedelta

from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager

our_flights_data = DataManager()
flight_search = FlightSearch(our_flights_data)

now = datetime.now()
todays_date = now.strftime("%m-%d-%Y")


#print(our_flights_data.locations_we_want_to_go())
#print(our_flights_data.get_access_token())

# print(flight_search.test_print())

for location in our_flights_data.locations_we_want_to_go():
    print(location)
    for day in range(0, 180):
        date_to_search = now + timedelta(days=day)
        date_formatted = date_to_search.strftime("%Y-%m-%d")        #flight_search.price_lookup(location["iataCode"], location["lowestPrice"], date_to_search)
        flight_search.price_lookup(location["iataCode"], location["lowestPrice"], date_to_search)

# def price_lookup(iata, price, departure_date):
        
#     price_params = {
#         "originLocationCode" : "DSM",
#         "destinationLocationCode" : iata,
#         "departureDate" : departure_date,
#         "adults" : 1,
#         "currencyCode" : "USD",
#         "maxPrice" : price
#     }
#     print(price_params)

#     airport_search_header = {
#             "Authorization" : "Bearer " + our_flights_data.get_access_token()
#         }

#     flight_offer_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

#     flight_offer_response = requests.get(url=flight_offer_endpoint, params=price_params, headers=airport_search_header)
    
#     return flight_offer_response.json()

# for day in range(0, 180):
#     date_to_search = now + timedelta(days=day)
#     date_formatted = date_to_search.strftime("%Y-%m-%d")
#     print(date_formatted)
#     #flight_search.price_lookup(location["iataCode"], location["lowestPrice"], date_to_search)
#     price_lookup("DEN", 200, date_formatted)


        
        