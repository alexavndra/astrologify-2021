import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public'
username = '31tnz6f4fdyyuw444ryw5f6anvbq'

token = SpotifyOAuth(scope = scope, username = username)
spotifyObj = spotipy.Spotify(auth_manager = token)

print("welcome to astrologify! made for UCSD SPIS 2021 by alex h and leah k!")
print("\n")

user_name = input("Enter your name: ")
sun_sign = input("Enter your sun sign: ")
playlist_name = user_name + " " + sun_sign + "'s playlist"
description = user_name + "'s " + sun_sign + " playlist made with astrologify"

# creates the user's playlist
spotifyObj.user_playlist_create(user=username,name=playlist_name,public=True,description=description)

# user_tops = spotifyObj.current_user_top_tracks(limit=20,offset=0,time_range='long_term')
# print(json.dumps(user_tops,sort_keys=4,indent=4))

# gets three songs to put in user playlist
user_top_tracks = []
user_own_rec = input("Enter a favorite song (will be included): ")

for i in range(3):
    user_song = spotifyObj.search(q=user_own_rec)

    #finds song and puts it into list
    user_top_tracks.append(user_song['tracks']['items'][0]['uri'])

    # asks again
    user_own_rec = input("Enter a favorite song (will be included): ")
 

# will ask for genre
spotifyObj.recommendation_genre_seeds()
favorite_genre = input("Enter favorite genre: ")

astro_rec = []
song_rec = []

# takes the genre from the sun signs too here
if sun_sign == "aries":
    for song in ["don't stop believin'","whole lotta love","livin' on a prayer","dream on","kashmir"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "taurus":
    for song in ["let's stay together","lean on me","a change is gonna come","i say a little prayer","baby love"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "leo":
    for song in ["into you","levitating","...baby one more time","levitating","stay"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "pisces":
    for song in ["stargazing","passion","take me where your heart is","addicted","godspeed"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "virgo":
    for song in ["filma solo","fracture","losar","robin's cello","somnia"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "cancer":
    for song in ["i walk the line","jolene","live like you were dying","before he cheats","concrete angel"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "sagittarius":
    for song in ["chunky","uptown funk","this is what you came for","get lucky","starboy"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "gemini":
    for song in ["harder, better, faster, stronger","i feel it coming","wolves","get lucky","the nights"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "aquarius":
    for song in ["one more time","get lucky","digital love","break free","technologic"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "libra":
    for song in ["20 something","butterflies","dark red","self control","pink+white"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "scorpio":
    for song in ["dior","hurricane","violent crimes","butterfly effect","chun li"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])
elif sun_sign == "capricorn":
    for song in ["tell me a bedtime story","april in paris","if you could see me now","blue world","close your eyes"]:
        song_result = spotifyObj.search(q=song)
        astro_rec.append(song_result['tracks']['items'][0]['uri'])

# incorporates some of the user's fave genre tracks
if favorite_genre == "pop":
    for song in ["24k magic","driver's license","what makes you beautiful","lights up","fergalicious"]:
        genre_result = spotifyObj.search(q=song)
        song_rec.append(genre_result['tracks']['items'][0]['uri'])
elif favorite_genre == "rock":
    for song in ["kiwi","end up here","creep","smells like teen spirit","californication"]:
        genre_result = spotifyObj.search(q=song)
        song_rec.append(genre_result['tracks']['items'][0]['uri'])
elif favorite_genre == "hip-hop":
    for song in ["passionfruit","yikes","HUMBLE.","thot shit","tell em"]:
        genre_result = spotifyObj.search(q=song)
        song_rec.append(genre_result['tracks']['items'][0]['uri'])
elif favorite_genre == "r&b":
    for song in ["normal girl","pyramids","open (passionate)","best part","hit my phone"]:
        genre_result = spotifyObj.search(q=song)
        song_rec.append(genre_result['tracks']['items'][0]['uri'])
elif favorite_genre == "indie":
    for song in ["basement jack","easy","solar power","hate cd","sofia"]:
        genre_result = spotifyObj.search(q=song)
        song_rec.append(genre_result['tracks']['items'][0]['uri'])
elif favorite_genre == "country":
    for song in ["cruise","beautiful crazy","marry me","new truck","crash and burn"]:
        genre_result = spotifyObj.search(q=song)
        song_rec.append(genre_result['tracks']['items'][0]['uri']) 
elif favorite_genre == "jazz":
    for song in ["put your head on my shoulder","innerstellar love","habits","la vie en rose","feeling good"]:
        genre_result = spotifyObj.search(q=song)
        song_rec.append(genre_result['tracks']['items'][0]['uri'])    
else:
    print("please choose another favorite genre!")                  

# lists will contain some of the user's received fave genre tracks and astrologify tracks

# print(json.dumps(astro_rec,sort_keys=4,indent=4))
# print(json.dumps(song_rec,sort_keys=4,indent=4))


# finds playlist
playlistcreator = spotifyObj.user_playlists(user=username)

# accessing playlist
playlist = playlistcreator['items'][0]['id']


# adds songs to playlist
for track_type in [user_top_tracks, astro_rec, song_rec]:
    spotifyObj.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=track_type) 

print("done, thank you for using! check out your spotify for the playlist :)")