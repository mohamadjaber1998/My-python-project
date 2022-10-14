import smtplib
import pandas as pd
import random
import datetime as dt
import glob

my_email = "your email"
password = "your pass"


def sendmail(mail, msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=mail, msg=f"Subject:Happy Birthday\n\n{msg}")


now = dt.datetime.now()
now_month = now.month
now_day = now.day

df = pd.read_csv("birthdays.csv")
for index, row in df.iterrows():
    month = row["month"]
    day = row["day"]
    name = row["name"]
    email = row["email"]
    if month == now_month and day == now_day:
        filename = random.choice(glob.glob('./letter_templates/*.txt'))
        with open(filename, 'r') as f:
            letter_str = f.read()
            final = letter_str.replace("[NAME]", name)

        sendmail(email, final)


