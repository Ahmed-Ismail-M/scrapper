import requests
from bs4 import BeautifulSoup

URL = "https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9"
res = requests.get(url=URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
    data = items.find_all(['th','td'])
    try:
        country = data[0].a.text
        title = data[1].a.text
        name = data[1].a.find_next_sibling().text
    except IndexError:pass
    print("{}|{}|{}".format(country,title,name))