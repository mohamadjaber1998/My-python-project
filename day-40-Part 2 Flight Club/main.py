from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

notify = NotificationManager()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data() # get data from SHEETY as dict

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
            flight_dict = {
                "from city": flight.origin_city,
                "from airport": flight.origin_airport,
                "to city": flight.destination_city,
                "to airport": flight.destination_airport,
                "price": flight.price,
                "out date": flight.out_date
            }
            flights_list.append(flight_dict)
    except AttributeError:
        pass
notify.send_message(flights_list)

