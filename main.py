from data_manager import DataManager
from datetime import  datetime,timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager


flight_search = FlightSearch()
deta = DataManager()
sheet_data  = deta.get_destination_data()
notification_manager = NotificationManager()


tommorow_date = (datetime.now() + timedelta(days = 1)).strftime("%d/%m/%Y")
six_month_date = (datetime.now()+ timedelta(days=6*30)).strftime("%d/%m/%Y")


# Here is our iata codex
b = 0
for row in sheet_data:
    if sheet_data[b]["iataCode"] == "":
        row['iataCode']= flight_search.get_destination_code(row["city"])
        b+=1
        deta.destination = sheet_data
        deta.update_destination_data()
    b += 1

for destination in sheet_data:
    flight_list = flight_search.search_flight(destination_city=destination['iataCode'],from_time=tommorow_date,to_time=six_month_date,price=destination['lowestPrice'])

    try:
        if flight_list.price < destination['lowestPrice']:
            notification_manager.send_sms(text=f"Low price alert! Only ${flight_list.price} to fly from {flight_list.origin_city}-{flight_list.origin_airport} to {flight_list.destination_city}-{flight_list.destination_airport}, from {flight_list.out_date}. to {flight_list.return_date}.")
    except AttributeError:
        continue