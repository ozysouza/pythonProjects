from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titles = [movies_titles.getText() for movies_titles in soup.find_all(name="h3", class_="title")]

with open("movies.txt", mode="w") as file:
    for title in list(reversed(titles)):
        file.write(f"{title}\n")

