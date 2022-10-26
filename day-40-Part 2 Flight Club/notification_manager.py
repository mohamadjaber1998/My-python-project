import requests
from smtplib import SMTP

URL = "https://api.sheety.co/bfd2410085fa74be48f93a2ed6f8ea5d/usersClub/users"
user_name = ""
password = ""


class NotificationManager:
    def __init__(self):
        self.users_emails = []
        self.import_users()


    def import_users(self):
        response = requests.get(url=URL)
        users = response.json()['users']
        for user_dict in users:
            self.users_emails.append(user_dict['email'])


    def send_message(self, message: list):
        with SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=user_name, password=password)

            if len(message) == 0:
                message1 = "Unfortunately, We didn't find any deal yet."
                for user in self.users_emails:
                    connection.sendmail(from_addr=user_name, to_addrs=user, msg=f"Subject:Travel deal\n\n{message1}")

            else:
                message1 = ""
                for city in message:
                    from_city = city['from city']
                    from_airport = city['from airport']
                    to_city = city['to city']
                    to_airport = city['to airport']
                    price = city['price']
                    out_date = city['out date']

                    message1 += f"Hurry up! We've found a deal in {out_date}.\n" \
                               f"Travel from {from_city}({from_airport})\n" \
                               f"to {to_city}({to_airport}).\n\n\n"

                print(message1)
                for user in self.users_emails:
                    connection.sendmail(from_addr=user_name, to_addrs=user, msg=f"Subject:Travel deal\n\n{message1}")


