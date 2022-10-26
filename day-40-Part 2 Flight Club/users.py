
# Use this for sign new users only.

import requests

print("Welcome to Mohamad's flight club.")
print("We find the best flight deals and email you.")

first_name = input("What is your first name ? ")
last_name = input("What is your last name ? ")
it_is_same = False

while not it_is_same:
    email = input("What is your email ? ")
    email_again = input("Type your email again ? ")

    if email == email_again:
        it_is_same = True
    else:
        print("Retype your email please. ")


params = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}

response = requests.post(url="https://api.sheety.co/bfd2410085fa74be48f93a2ed6f8ea5d/usersClub/users", json=params)
response.raise_for_status()
print("You are in the club.")
