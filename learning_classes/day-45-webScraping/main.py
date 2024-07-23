from bs4 import BeautifulSoup
import requests


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")

article_texts = [article.getText() for article in soup.find_all(name="a", class_="storylink")]
article_links = [link.get("href") for link in soup.find_all(name="a", class_="storylink")]
article_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_index = article_votes.index(max(article_votes))

print(article_texts[highest_index])
print(article_links[highest_index])
print(article_votes[highest_index])

# with open("website.html") as website:
#     contents = website.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# a = soup.find_all(name="p")
# print(a[0])
#
# heading = soup.find(name="h1", id="name")
