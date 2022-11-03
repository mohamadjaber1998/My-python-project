import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# client_id = '4a028a465efa4f27ad7fcd1b10440607'
# client_secret = '57f52e735047445fab2408de9013bd5f'
Access_Token = 'BQD_WrzrOG1WCMf4kZTrgOikiUKqot9QQqrKjd48MDhrKgq_VARwb7QR6QBL5E68aJf1uE_5X8Xsx5yO-eDUM4NKkqQo9FBrLHtfj2xmb1swEWhypsEHu2A8sbJJuQzp-VYSjJtMS0YYuVlPQtu-guFoxFvYnIcw7RS9eCXqWr1NWf01Ivj6OVtdi5JjzmErtIvV3CHNIjeI9w0QO2-1O1-eh_PLXxSRc3Pk-ryORTYnlsvoEHer4Of_YXh7'
spotify_endpoint = 'https://api.spotify.com/v1/users/0yubuyrhpqo7jicmfdbzp8nkz/playlists'

# ------------------ Scraping songs ----------------------

date = input("Which year do you want to travel to ? (type the date in this format: YYYY-MM-DD): ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=URL)
website = response.text
soup = BeautifulSoup(website, 'html.parser')

content = soup.find_all(name='li', attrs={'class': 'o-chart-results-list__item'})

final = []
for name in content:
    final.append(name.getText().strip())

songs_list = []

for ind in final:
    if len(ind) > 1:
        try:
            int(ind)
        except:
            songs_list.append(ind.replace('\n', '').replace('\t', ' '))

final_songs_list = [song.split('   ')[0] for song in songs_list ]

print(final_songs_list)
print(f' I have found {len(final_songs_list)} songs on Billboard.')

# --------------- Search fo songs and add the song's id to a list --------------

headers = {
    'Authorization': f'Bearer {Access_Token}'
}

spotify_search_endpoint = 'https://api.spotify.com/v1/search'
uris_list = []
for song in final_songs_list[0:100]:
    try:
        search_params = {
            'q': song,
            'type': 'track'
        }

        response = requests.get(url=spotify_search_endpoint, params=search_params, headers=headers)
        response.raise_for_status()
        uris_list.append(response.json()['tracks']['items'][0]['uri'])
    except:
        pass

print(uris_list)
print(f'I have found {len(uris_list)} songs on spotify.')

# ------------------------- Create new playlist ------------------

param = {
    'name': f'100 Billboard {date} playlist'
}

response = requests.post(url=spotify_endpoint, json=param, headers=headers)
response.raise_for_status()
playlist_id = response.json()['id']
print(f"The Playlist id: {playlist_id}")

# ----------------- Add to playlist --------------------

spotify_items_endpoint = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
headers_for_add_items = {
    'Authorization': f'Bearer {Access_Token}'
}

track_params = {
    'uris': uris_list
}

response1 = requests.post(url=spotify_items_endpoint, json=track_params, headers=headers_for_add_items)
response1.raise_for_status()
print(response1.json())

