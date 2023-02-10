"""uses api to access spotify client id"""

import json

import requests

# separate py classes in the app
from spotify_playlist import spotifyplaylist
from spotify_track import spotifytrack

class SpotifyClient:

    def __init__(self, auth_token, user) -> None:
        
        self._auth_token = auth_token
        self._user = user

    def get_last_played_tracks(self, limit = 10):
        
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"    
        response = self.get_api_request(url) # function 
        response_json = response.json()
        # tracks = [spotifytrack(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for
                #   track in response_json["items"]]
        return response_json

    def get_track_recommendations(self, seed_tracks, seed_artists, limit = 50):

        seed_tracks_url = "" # empty string
        seed_artists_url = "" # empty string

        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_track_url = seed_tracks_url[:-1]        
        
        for seed_artist in seed_artists:
            seed_artists_url += seed_artist.id + ","
        seed_artists_url = seed_artists_url[:-1]   

        url = f"https://api.spotify.com/v1/recommendations?limit={limit}&market=US&seed_artists={seed_artists_url}&seed_tracks={seed_tracks_url}"

        response = self.get_api_request(url) # function
        response_json = response.json()
        tracks = [spotifytrack(track["name"], track["id"], track["artists"][0]["name"]) for
                  track in response_json["tracks"]]
        return 
        
    def create_spotify_playlist(self, playlistname):
        data = json.dumps({
            "name": playlistname,
            "description": "Recommended songs",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self._user_id}/playlists"
        response = self.place_post_api_request(url, data)
        response_json = response.json()

        # create playlist
        playlist_id = response_json["id"]
        playlist = spotifyplaylist(playlistname, playlist_id)
        return playlist  

    def populate(self, playlistname, tracks): 

        track_uris = [spotifytrack.create_uri() for track in tracks]
        data = json.dumps(track_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlistname.id}/tracks"
        response = self.place_post_api_request(url, data)
        response_json = response.json()
        return response_json

    def get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._auth_token}"
            }
        )
        return response    

    def place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self._auth_token}"
            }
        )
        return response    