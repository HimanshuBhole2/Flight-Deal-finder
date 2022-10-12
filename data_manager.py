import requests
SHEET_ENDPOINT = "YOUR SHEETY DOC. LINK "

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination = {}

    # This is our fuction for getting the data.
    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        self.destination = response.json()["prices"]
        return self.destination


    #This is for updating of data.
    def update_destination_data(self):
        for city in self.destination:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}",json=new_data)