"""tracks for playlist"""

class spotifytrack:

    def __init__(self, songname, id, artist):
        
        self.songname = songname
        self.id = id
        self.artist = artist

    def create_uri(self):
        return f"Spotify:track:{self.id}"

    def __str__(self):
        return self.songname + ": " + self.artist        