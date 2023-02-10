"""create spotify playlist based on prefs"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = 'user-id' # replace later !

token = SpotifyOAuth(scope=scope, username=username)
spotify = spotipy.Spotify(auth_manager=token)

playlist_name = input("Enter a name for your playlist: ")
playlist_description = username + "'s playlist by astrologify"

spotify.user_playlist_create(user = username, name = playlist_name, public = True, description = playlist_description)

user_genre_input = ""
user_sun_sign_input = ""
list_of_songs = []

user_genre_input = input("Enter your favorite genre: ")
user_sun_sign_input = input("Enter your sun sign: ")



