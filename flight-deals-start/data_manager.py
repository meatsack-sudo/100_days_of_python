import requests

SHEETY_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
AMADEUS_API_KEY = "s2VQrd5x9ZpQZJ2BnURgPhsIWDS6IBS6"
AMADEUS_API_SECRET = "8XTtr2N3k7dFsJsi"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
        def __init__(self):
            self.sheety_endpoint = "https://api.sheety.co/4eb3e425f8c9d43b430d4b9317fe8142/flightDeals/prices"
            self.sheety_header = {
                  "Authorization" : f"Bearer {SHEETY_TOKEN}"
            }
            self.sheety_response = requests.get(url=self.sheety_endpoint, headers=self.sheety_header)
            if self.sheety_response.status_code == 200:
                 
                self.data = self.sheety_response.json()

            self.amadeus_access_token = self.get_access_token()

        def get_access_token(self):

            token_params = {
                "grant_type": "client_credentials",
                "client_id": AMADEUS_API_KEY,  # Replace with your actual API key
                "client_secret": AMADEUS_API_SECRET  # Replace with your actual API secret
            }

            token_headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            token_response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", data=token_params, headers=token_headers)

            try:
                token_response.raise_for_status()  # Check if the request was successful
                token_data = token_response.json()
                #print(token_data)
                self.access_token = token_data['access_token']
                #print(access_token)
                return self.access_token
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                if token_response.content:
                    print(token_response.content.decode())


        def get_iata_code(self, city):
             
            flight_search_params = {
                "keyword" : city,
                "max" : 1
            }

            airport_search_header = {
                "Authorization" : "Bearer " + self.amadeus_access_token
            }

            airport_search_response = requests.get("https://test.api.amadeus.com/v1/reference-data/locations/cities", params=flight_search_params, headers=airport_search_header)
            airport_search_data = airport_search_response.json()
            #print(airport_search_data)
            return airport_search_data["data"][0]["iataCode"]       
                    
        #This method will grab all locations in the spreadsheet and if IATA is missing
        # update them.
        #                 
        def locations_we_want_to_go(self):
              if self.sheety_response.status_code == 200:
                    #self.data = self.sheety_response.json()
                    #print(self.data)
                    for location in self.data["prices"]:
                        if location["iataCode"] == '':
                            print(f"{location["city"]} doesn't have an IATA code. Searching for one and adding it. I recommend double-checking the IATA I find.")
                            iata_code = self.get_iata_code(location["city"])
                            if iata_code:
                                id = location['id']
                                spreadsheet_data = {
                                    "price" : {
                                        "iataCode" : iata_code
                                    }
                                }

                                self.sheety_response = requests.put(url=self.sheety_endpoint+"/"+str(id), json=spreadsheet_data, headers=self.sheety_header)
                                #print(self.sheety_response.status_code)
                                #print(self.sheety_response.text)
                        #print(location["city"])
                        #print(location["iataCode"])
                         
                    
                    return self.data["prices"]
        