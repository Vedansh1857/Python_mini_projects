# step 0 : Get the requirements
import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com"

# Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlcontent)

# Step 2 : Parse the htmlcontent

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# step 3: HTML tree traveler
#
# 1. print(type(title.string)) # Navigable String
# 2. print(type(title)) # Tag
# 3. print(type(soup)) # BeautifulSoup

# 4. markup = "<p><!--this is a comment--></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string)) # bs4.element.comment

# To get the title of the html page
title = soup.title

# To get all the paragraphs frm the page
paras = soup.find_all('p')
# print(paras)

# To get the first element of the html page
print(soup.find('p'))

# To get classes of any element of the html page
print(soup.find('p')['class'])

# To find all the elements with class lead of the html page
print(soup.find_all('p', class_='lead'))

# Get the text frm the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# To get all the anchor tags frm the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page
for link in anchors:
    if link != '#':
        link = "https://stackoverflow.com" + link.get('href')
        all_links.add(link)
        print(link)

navbarSupportedContent = soup.find(id= "navbarSupportedContent")
for elem in navbarSupportedContent.children:
    print(elem)
