"""playlist for client"""

class spotifyplaylist:
    
    def __init__(self, playlistname, id):

        self.playlistname = playlistname
        self.id = id

    def __str__(self):
        return f"Playlist: {self.playlistname}"    