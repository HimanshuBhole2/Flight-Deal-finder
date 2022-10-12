import requests
from flight_data import FlightData
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "TEQUILA API KEY"

class FlightSearch:
    # This for getting the iata code.
    def __init__(self):
        pass

    def get_destination_code(self, city_name):
        # print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
    #datefrom.strftime("%d/%m/%Y")
    #This function searches flight
    def search_flight(self,destination_city,from_time,to_time,price):
        params = {"fly_from": "IND", "fly_to": destination_city, "date_from":from_time, "date_to": to_time,
                  "flight_type": "round", "max_stopovers": 0, "nights_in_dst_from": 7, "nights_in_dst_to": 28,
                  "price_to": price, "curr": "USD"
                  }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers={"apikey": TEQUILA_API_KEY})


        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"NO flight for this destination.{destination_city}")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data





