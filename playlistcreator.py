import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = 'alexavndra'

token = SpotifyOAuth(scope = scope, username = username)
spotifyObj = spotipy.Spotify(auth_manager = token)

playlist_name = input("Enter a playlist name:")
description = input("Enter a description:")

spotifyObj.user_playlist_create(user=username,name=playlist_name,public=True,description=description)

user_input = input("Enter the song: ")
list_of_songs = []

while user_input != "quit":
    song_result = spotifyObj.search(q=user_input)

    # finds the data for song uri
    list_of_songs.append(song_result['tracks']['items'][0]['uri'])

    # print(json.dumps(song_result,sort_keys=4,indent=4))
    user_input = input("Enter a song: ")

# finds playlist
playlistcreator = spotifyObj.user_playlists(user=username)

# accessing playlist
playlist = playlistcreator['items'][0]['id']

# adds songs to playlist
spotifyObj.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)
