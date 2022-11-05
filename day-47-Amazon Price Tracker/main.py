import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

my_email = ''
my_password = ''
receiver_email = ''

amazon_url = 'https://www.amazon.com/dp/B09MS2FGJP/ref=sbl_dpx_kitchen-electric-cookware_B0BK9H6XCT_0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'
}

response = requests.get(url=amazon_url, headers=headers)
response.raise_for_status()
page = response.text

soup = BeautifulSoup(page, 'html.parser')
span = soup.find_all(name='span', class_='a-offscreen')
price = float(span[0].getText().replace('$', ''))
print(price)

if price < 120:
    with SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.loging(my_email, my_password)
        connection.sendmail(my_email, my_email, msg=f'Subject::Amazon price tracker\n\nHurry up!\nThe price is {price}')