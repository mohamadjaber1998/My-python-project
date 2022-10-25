from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

notify = NotificationManager()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data() # get data from SHEETY as dict
print(sheet_data)
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

flights_list = []

for destination in sheet_data:
    try:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        if flight.price <= destination['lowestPrice']:
            notify.send_message()
    except AttributeError:
        pass





    #     flights_dict = {
    #         "to": flight.destination_city,
    #         "price": flight.price
    #     }
    #     flights_list.append(flights_dict)
    #
    # except AttributeError:
    #     pass

