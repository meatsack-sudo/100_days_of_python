import requests
import data_manager
import datetime

SHEETY_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
AMADEUS_API_KEY = "s2VQrd5x9ZpQZJ2BnURgPhsIWDS6IBS6"
AMADEUS_API_SECRET = "8XTtr2N3k7dFsJsi"

AMADEUS_FLIGHT_OFFER_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    #This class is responsible for structuring the flight data.
    def __init__(self, data_manager: data_manager):
        self.data_manager = data_manager
        self.access_token = self.data_manager.amadeus_access_token

    def price_lookup(self, iata, price, departure_date):
          
        price_params = {
            "originLocationCode" : "DSM",
            "destinationLocationCode" : iata,
            "departureDate" : departure_date,
            "adults" : 1,
            "currencyCode" : "USD",
            "maxPrice" : price
        }

        airport_search_header = {
                "Authorization" : "Bearer " + self.access_token
            }
        
        flight_offer_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        flight_offer_response = requests.get(url=flight_offer_endpoint, params=price_params, headers=airport_search_header)
        
        return flight_offer_response.json() 

    def test_print(self):
        
        print(self.access_token)

        #amadeus_response = requests.get(url=AMADEUS_FLIGHT_OFFER_URL, params=price_params, )