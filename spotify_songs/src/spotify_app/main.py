import requests

from bs4 import BeautifulSoup
from src.spotify_app.services import Services
from src.spotify_auth.authenticator import Authenticator
from src.utils.utils import *
from src.utils.logger import *


def main():
    authenticator = Authenticator()
    spotify_serv = Services(authenticator)
    setup_logging()  # Initialize logging with default file name 'app.log'

    while True:
        user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        if validate_date(user_date):
            url = f"https://www.billboard.com/charts/hot-100/{user_date}"

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # Extracting songs and authors
            songs_list = [song.getText().strip() for song in soup.select("li ul li h3")]
            author_list = [author.getText().strip() for author in soup.select("li ul li span.a-no-trucate")]

            # Cleaning Author name for better match on spotify
            for idx, author in enumerate(author_list):
                cleaned_name = clean_author_name(author)
                author_list[idx] = cleaned_name

            # Combining into a dictionary
            songs_authors_dict = {result: {"song": song, "author": author} for result, (song, author) in
                                  enumerate(zip(songs_list, author_list))}

            # Create play list
            spotify_serv.create_play_list("Billboard 100")

            # Get the track ID
            play_list_id = spotify_serv.get_play_list_id("Billboard 100")

            # Adding tracks into playlist
            for index, entry in songs_authors_dict.items():
                track_id = spotify_serv.get_track_id(entry['song'], entry['author'])
                spotify_serv.add_track_to_playlist(play_list_id, track_id)
            return False
        else:
            show_logging("Incorrect data format, should be YYYY-MM-DD", logging.WARNING)


if __name__ == "__main__":
    main()
