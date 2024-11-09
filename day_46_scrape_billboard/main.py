import requests
from bs4 import BeautifulSoup

year = input("What year would you like to travel to? Use this format YYYY-MM-DD: ")

url = (f"https://www.billboard.com/charts/hot-100/{year}/#")

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Target the list items that contain each song entry
all_songs = soup.find_all("li", class_="o-chart-results-list__item")

list_of_songs = []
for song in all_songs:
    # Within each list item, find the h3 tag containing the song title
    song_name = song.find("h3", id="title-of-a-story")
    if song_name:
        list_of_songs.append(song_name.get_text(strip=True))

print(list_of_songs)