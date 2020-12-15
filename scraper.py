import requests

# server was blocking python headers so use User-Agent:XY to get around it

url = 'https://www.hookedondestin.com/deepseafishingboats.html'
r = requests.get(url, headers={"User-Agent": "XY"})
print(r.status_code)
print(r.headers)

#  display HTML content

r.content

# import beautifulsoup

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,'html.parser')

# prettify results to find name and phone numbers

print(soup.prettify())

soup.select("div br")




from BeautifulSoup import BeautifulSoup, NavigableString, Tag



input = '''<br />
Important Text 1
<br />
<br />
Not Important Text
<br />
Important Text 2
<br />
Important Text 3
<br />
<br />
Non Important Text
<br />
Important Text 4
<br />'''

soup = BeautifulSoup(input)

for br in soup.findAll('br'):
    next_s = br.nextSibling
    if not (next_s and isinstance(next_s,NavigableString)):
        continue
    next2_s = next_s.nextSibling
    if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
        text = str(next_s).strip()
        if text:
            print ("Found:", next_s)
