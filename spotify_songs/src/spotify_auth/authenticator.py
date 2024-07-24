import logging

import spotipy
import os

from spotipy.oauth2 import SpotifyOAuth
from src.utils.logger import show_logging


class Authenticator:
    """
    Class to handle Spotify authentication.
    """
    def __init__(self):
        """
        Initializes the SpotifyAuthenticator with the provided credentials.

        Args:
            client_id (str): The client ID for the Spotify app.
            client_secret (str): The client secret for the Spotify app.
            redirect_uri (str): The redirect URI for the Spotify app.
        """
        self.client_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.client_uri = os.getenv("SPOTIPY_REDIRECT_URI")
        self.sp = self.authenticate()

    def authenticate(self):
        """
        Authenticates the user with Spotify and retrieves an access token.

        Returns:
             The authenticated user.
        """
        try:
            show_logging("Authenticating with Spotify.", logging.INFO)
            sp_oauth = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                redirect_uri=self.client_uri,
                scope="user-library-read playlist-modify-public playlist-read-private"))
            show_logging("Authenticating successful.", logging.INFO)
            return sp_oauth
        except Exception as e:
            show_logging(f"Authentication failed: {e}", logging.ERROR)
            raise
