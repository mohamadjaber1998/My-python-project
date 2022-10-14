import smtplib
import random

my_email = "your email"
password = "your pass"

with open("quotes.txt", encoding="utf-8") as file:
    lines = file.readlines()
line = random.choice(lines).encode("ascii", "ignore").strip()
print(line)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="hektor.net.83@gmail.com",
                        msg=f"Subject:Motivation\n\n{line}"
                        )
