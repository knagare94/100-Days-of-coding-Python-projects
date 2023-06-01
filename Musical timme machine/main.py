import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "23dd72c7f30645838fcdd31e287aee65"
CLIENT_SECRET = "eeb7484a43914c6195f70623f87b9d41"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
billboard_web = response.text

soup = BeautifulSoup(billboard_web, "html.parser")
songs = soup.find_all("h3", class_="a-no-trucate")
song_names = [song.getText().strip() for song in songs]
print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["23dd72c7f30645838fcdd31e287aee65"]
