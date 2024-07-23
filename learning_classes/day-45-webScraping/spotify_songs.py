from bs4 import BeautifulSoup

import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
songs_list = [song.getText().strip() for song in soup.select("li ul li h3")]
print(songs_list)