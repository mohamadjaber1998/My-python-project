import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os

# ------------ Create folders ------------
try:
    os.makedirs("Clubs")
    os.makedirs("Games")
    os.makedirs("Players")
except:
    pass
# --------------- Create csv file for clubs --------------

field_names = ['Club name', 'Manager', 'City', 'Foundation', 'Stadium', 'Website']
games_field_names = ['Home', 'Home goals', 'Away', 'Away goals']
players_field_name = ['name', 'number Player', 'AGE', 'club', 'mainposition', 'Overall', 'physical', 'mental', 'technical', 'attacking', 'defending']

with open('Clubs/clubs.csv', 'w') as file_csv:
    writer = csv.DictWriter(file_csv, fieldnames=field_names)
    writer.writeheader()

# --------------- start scraping -------------------

url = 'https://www.footballdatabase.eu/en/'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
anchor = soup.find_all('div', {'class': "topclubs"})

for pt in anchor:

    # ---------------------  Return all hrefs  for teams ----------
    teams_href_list = ['https://www.footballdatabase.eu' + link.get('href') for link in pt.find_all('a')]

    for a in teams_href_list:

        r = requests.get(a)
        soup = BeautifulSoup(r.content, "html.parser")
        try:

            # ------------------------ Return Manager --------------------------------

            Manager = soup.find('div', {'class': 'section-manager'}).find('p', {'class': 'manager'}).find('a').get_text()

            # -------------------------- Return Info ----------------------------

            car_det = soup.find('div', {'class': 'info'}).find_all('div')
            det_list = [div.get_text() for div in car_det]
            City = det_list[1][4:]
            Name = det_list[2][9:]
            Foundation = det_list[4][10:]
            Stadium = det_list[5][8:]
            website = det_list[6][16:]
            print(Name)

            # ---------------------------- Return info to csv ------------------------

            to_csv = {
                'Club name': Name,
                'Manager': Manager,
                'City': City,
                'Foundation': Foundation,
                'Stadium': Stadium,
                'Website': website
            }

            df = pd.DataFrame(data=to_csv, index=[0])
            df.to_csv(f'Clubs/clubs.csv', mode='a', index=False, header=False)

            # --------------- create games csv file ---------------------

            with open(f'Games/{Name}.csv', 'w') as file_csv:
                writer = csv.DictWriter(file_csv, fieldnames=games_field_names)
                writer.writeheader()

            club_gams = soup.find_all('tr', {'class': 'line'})
            for line in club_gams:
                home = line.find('span', {'class': 'first_score'})
                away = line.find('span', {'class': 'second_score'})
                td = line.find_all('td', {'class': 'club'})
                games = [a.find('a').get_text() for a in td]

                try:
                    if len(games) > 1:
                        game_dict = {
                            'Home': games[0],
                            'Home goals': home.get_text(),
                            'Away': games[1],
                            'Away goals': away.get_text()
                        }
                        df = pd.DataFrame(data=game_dict, index=[0])
                        df.to_csv(f'Games/{Name}.csv', mode='a', index=False, header=False)

                except:
                    pass
            # ------------------------ Return players -------------------------------
            with open(f'Players/{Name}.csv', 'w') as file_csv:
                writer = csv.DictWriter(file_csv, fieldnames=players_field_name)
                writer.writeheader()

            players = soup.find_all('div', {'class': "picture"})
            for py in players:
                for link in py.find_all('a'):
                    href = link.get('href')
                    a = 'https://www.footballdatabase.eu' + href
                    r = requests.get(a)
                    soup = BeautifulSoup(r.content, "html.parser")

                    # --------------- Return player name ---------------

                    if soup.find('li', {'class': 'subphoto mySlides'}) and soup.find('span', {'class': 'lastname'}):
                        try:
                            NAME = soup.find('span', {'class': 'lastname'}).get_text()
                            print(NAME)

                            # info = soup.find('div', {'class': 'infoPlayer'})

                        # ---------------- Return player number ------------

                            numberPlayer = soup.find('span', {'class': 'numberPlayer'}).get_text()

                        # ----------------- Return the age ------------------

                            AGE = soup.find('span', {'class': 'age'}).get_text().strip()

                        # ----------------- Return the club ------------------

                            club = soup.find('div', {'class': 'clublogo'}).find('a').get_text()

                        # ----------------- Return the image url ------------------

                            IMAGE = soup.find('li', {'class': 'subphoto mySlides'}).find('img').get('src')

                        # ------------------ Return the main position --------------

                            mainposition = soup.find('tr', {'class': 'mainposition'}).find('td').get_text()

                        # -------------------- Return Over all -----------------------

                            Overall = soup.find('div', {'class': 'skill general'}).find('div', {'class': 'result'}).get_text()

                        # -------------------- Return physical -----------------------

                            physical = soup.find('div', {'class': 'skill physical'}).find('div', {'class': 'result'}).get_text()

                        # -------------------- Return Mental ---------------------

                            mental = soup.find('div', {'class': 'skill mental'}).find('div', {'class': 'result'}).get_text()

                        # -------------------- Return technical ------------------

                            technical = soup.find('div', {'class': 'skill technical'}).find('div', {'class': 'result'}).get_text()

                        # -------------------- Return attacking ------------------

                            attacking = soup.find('div', {'class': 'skill attacking'}).find('div', {'class': 'result'}).get_text()

                        # -------------------- Return defending ------------------

                            defending = soup.find('div', {'class': 'skill defending'}).find('div', {'class': 'result'}).get_text()

                            player_data = {
                                'name': NAME,
                                'number Player': numberPlayer,
                                'AGE': AGE[1:3],
                                'club': club,
                                'mainposition': mainposition,
                                'Overall': Overall,
                                'physical': physical,
                                'mental': mental,
                                'technical': technical,
                                'attacking': attacking,
                                'defending': defending
                            }

                            df = pd.DataFrame(data=player_data, index=[0])
                            df.to_csv(f'Players/{Name}.csv', mode='a', index=False, header=False)

                        except:
                            pass

        except:
            pass
