import logging

from spotipy import SpotifyException
from src.utils.logger import show_logging
from src.spotify_auth.authenticator import Authenticator


class Services:
    """
    Class to handle various Spotify operations such as retrieving saved tracks,
    creating albums, and creating playlists.
    """

    def __init__(self, authenticator):
        """
        Initializes Services with an authenticator instance.

        Args:
            authenticator (Authenticator): An instance of SpotifyAuthenticator.
        """
        self.authenticator = authenticator
        self.sp = authenticator.authenticate()

    def get_saved_tracks(self):
        """ Gets a list of the tracks saved in the current authorized user's
            "Your Music" library

            Parameters:
                - limit - the number of tracks to return
                - offset - the index of the first track to return
                - market - an ISO 3166-1 alpha-2 country code

        """
        results = self.sp.current_user_saved_tracks()
        for (idx, item) in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])

    def create_play_list(self, name: str, description=""):
        """ Creates a playlist for a user

            Parameters:
                - user - the id of the user
                - name - the name of the playlist
                - description - the description of the playlist
        """
        show_logging(f"Creating Playlist: {name}", logging.INFO)
        self.sp.user_playlist_create(
            user=self.sp.current_user()["id"],
            name=name,
            description=description,
        )

    def get_play_list_id(self, playlist_name: str) -> str:
        """ Gets playlists of a user
            Args:
                playlist_name (str): Playlist name.
            Returns:
                str: The Spotify playlist ID if found, None otherwise.
        """
        user_id = self.sp.current_user()["id"]
        playlists = self.sp.user_playlists(user_id)

        try:
            for (idx, playlist) in enumerate(playlists["items"]):
                if playlist_name.title() in playlist["name"]:
                    show_logging("Match found!", logging.INFO)
                    return playlist["id"]
                show_logging("No match found.", logging.WARNING)
        except KeyError as error:
            show_logging(f"KeyError: {error}", logging.ERROR)
        except Exception as error:
            show_logging(f"An unexpected error occurred: {error}", logging.ERROR)

    def get_track_id(self, song_title: str, artist_name: str) -> str:
        """
        Search for a track on Spotify by song title and artist name.

        Args:
            song_title (str): Title of the song.
            artist_name (str): Name of the artist.

        Returns:
            str: The Spotify track ID if found, None otherwise.
        """
        try:
            query = f"track:{song_title} artist:{artist_name}"
            result = self.sp.search(query, type='track', limit=1)
            tracks = result.get('tracks', {}).get('items', [])
            if tracks:
                return tracks[0]['id']
        except SpotifyException as e:
            show_logging(f"Spotify API error: {e}", logging.ERROR)
        except IndexError:
            show_logging(f"{song_title} doesn't exist in Spotify. Skipped.", logging.ERROR)

    def add_track_to_playlist(self, playlist_id: str, track_list: str, song: str, author: str) -> dict:
        """
        Add a track to a Spotify playlist.

        Args:
            playlist_id (str): The Spotify playlist ID.
            track_list (str): The Spotify track ID.
            song (str): The song's name.
            author (str): The Author's name.
        Returns:
            dict: The response from the Spotify API.
        """
        try:
            response = self.sp.playlist_add_items(playlist_id, [track_list])
            show_logging(f"Adding {song} by Author: {author}", logging.INFO)
            return response
        except SpotifyException as e:
            show_logging(f"Spotify API error: {e}", logging.ERROR)
        except Exception as e:
            show_logging(f"An unexpected error occurred while adding the track: {song}, by the Author: {author} to "
                         f"the playlist: {e}", logging.ERROR)
