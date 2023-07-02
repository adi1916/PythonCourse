import requests
import bs4

base_url = "https://quotes.toscrape.com/page/{}/"
res = requests.get(base_url.format('1'))
soup = bs4.BeautifulSoup(res.text, "lxml")

print(soup)
#print(soup.select('.author'))
#1
for item in soup.select('.author'):
    print(item.text)

#2
for item in soup.select('.text'):
    print(item.text)

#3
for item in soup.select('.tag-item .tag'):
    print(item.text)

#4
lastPage = False
i = 1
base_url = "https://quotes.toscrape.com/page/{}/"
authors = set()
while not lastPage:
    res = requests.get(base_url.format(str(i)))
    if "No quotes found!" in res.text:
        break
    soup = bs4.BeautifulSoup(res.text, "lxml")
    for item in soup.select('.author'):
        authors.add(item.text)
    i += 1

#print(list(authors).sorted())
print(sorted(authors))