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

for location in our_flights_data.locations_we_want_to_go():
    print(location)
    for day in range(0, 180):
        date_to_search = now + timedelta(days=day)
        date_formatted = date_to_search.strftime("%Y-%m-%d")        #flight_search.price_lookup(location["iataCode"], location["lowestPrice"], date_to_search)
        flight_search.price_lookup(location["iataCode"], location["lowestPrice"], date_formatted)

        
        