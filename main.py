#webscraping
import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"

#get the html
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)

#parse the html
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

#HTML Tree tarversal
# get the title of html page
title=soup.title
#print(title)

#types of objects
print(type(title))#1. Tag
print(type(title.string))#2. Navigable String
print(type(soup))#3. BeautifulSoup

#4. Comment
# markup="<p><!--this is a comment--></p>"
# soup2=BeautifulSoup(markup)
# print(soup2)
# print(type(soup2))
# print(type(soup2.p))
# print(type(soup2.p.string))
# exit()

# get all the paragraphs from the page
paras=soup.find_all('p')
# print(paras)

# get all the anchors from the page
anchors=soup.find_all('a')
all_links=set()
#get all the links on the page
for link in anchors:
    if link.get("href") !='#':
        linkText="https://codewithharry.com"+link.get("href")
        all_links.add(linkText)
        print(linkText)

# print(anchors)

#get first elements in the HTML page
print(soup.find('p'))

#Get the classes of any element in HTML page
print(soup.find('p')['class'])

#find all the elements with class lead
print(soup.find_all("p",class_="lead"))

#get the text from the soup/tags
print(soup.find('p').get_text())
print(soup.get_text())








