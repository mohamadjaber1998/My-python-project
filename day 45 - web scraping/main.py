from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
yc = response.text

soup = BeautifulSoup(yc, 'html.parser')

article = soup.find_all(name='a', attrs={'target': '_self'})

movies_not_classified = [item.getText() for item in article]

movies = []
for item in movies_not_classified:
    if "Read Empire's" in item:
        movies.append(item[24:-1])
print(len(movies))
