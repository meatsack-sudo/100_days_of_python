from bs4 import BeautifulSoup


with open('C:/Users/Meatsack/Desktop/python training/100_days_of_python/bs4-start/website.html') as my_file:
    contents = (my_file.read())
    

soup = BeautifulSoup(contents, 'html.parser')
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)

#print(soup.a)
#print(soup.li)
#print(soup.p)

#print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

#for tag in all_anchor_tags:
    #print(tag.getText())
    #print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)