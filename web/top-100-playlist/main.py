import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotipyClientCredentials

URL = "https://www.billboard.com/charts/hot-100/"

with open("pass1.txt", "r") as f:
    SPOTIFY_CLIENT_ID = f.read()

with open("pass2.txt", "r") as f:
    SPOTIFY_CLIENT_SECRET = f.read()

# # URL += input("What date would you like? (YYYY-MM-DD) ")
# URL += "1997-06-02"
#
# html = requests.get(URL).text
# soup = BeautifulSoup(html, "html.parser")
# songs = []
# song_artist = []
#
# divs = soup.find_all(class_="o-chart-results-list-row-container")
# for div in divs:
#     rank = int(div.select("li span")[0].getText().strip("\n"))
#     title_div = div.find(name="h3", id="title-of-a-story")
#     title = title_div.getText().strip()
#     songs.append(title)
#     artist = title_div.find_next_sibling("span").getText().strip()
#     song_artist.append((rank, title, artist))
#
# print(song_artist)

# user_playlist_create(user, name, public=True, collaborative=False, description='')


