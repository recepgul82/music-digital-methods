import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_spotify_client(client_id, client_secret):
    auth = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth)
