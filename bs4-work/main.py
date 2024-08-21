from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_content = response.text

soup = BeautifulSoup(yc_content, "html.parser")
#print(soup.title)

first_title_span = soup.find(class_="titleline")

first_article_line = first_title_span.get_text()
print(first_article_line)
# for link in title_lines:
#     print(link.getText())
first_article_link = first_title_span.find("a")
print(first_article_link.get("href"))

first_article_score = soup.find(class_="score")
print(first_article_score.get_text())

