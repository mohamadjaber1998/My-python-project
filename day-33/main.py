import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 35.483038
MY_LONG = 35.895038
my_email = "your email"
password = "your password"


def is_it_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)
    if 78.9789 <= iss_longitude <= 120.9789 and -46.7087 <= iss_latitude <= -0.7087:
        print("I am here")
        return True
    else:
        return False


def is_it_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if sunset <= time_now.hour <= sunrise:
        print("dark")
        return True
    else:
        return False


def look_up():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="hektor.net.83@gmail.com", msg="Subject:Look up\n\n look up.")
    print("Message has been sent.")


while True:
    print("I still work")
    time_now = datetime.now()

    if is_it_close() and is_it_dark():
        print("up")
        look_up()
    time.sleep(60)
