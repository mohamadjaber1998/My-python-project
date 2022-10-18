import requests

from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "your's"
auth_token = "your's"

api_key = "your's"

OWM_param = {
    "lat": 35.528227,
    "lon": 35.786146,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=OWM_param)
weather_data = response.json()

weather_status = weather_data["weather"][0]["description"]
temp = int(weather_data["main"]["temp"])-273

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=f"The weather status is {weather_status}, and the temperature is {temp}.",
                     from_='+00000000',
                     to='+00000'
                 )

print(message.status)
