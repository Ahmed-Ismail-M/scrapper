import requests
from bs4 import BeautifulSoup
def scrap_data(url: str)-> list:
    res = requests.get(url=url).text
    soup = BeautifulSoup(res, "html.parser")
    result = soup.find("table", class_="wikitable").find_all("tr")[1::1]  # type: ignore
    rows = []
    for items in result:
        data = items.find_all(["th", "td"])
        row = []
        for col in range(len(data)):
            try:
                if data[col].find("a"):
                    hyperlink = "https://ar.wikipedia.org/" + data[col].find("a").get("href")  # type: ignore
                else:
                    hyperlink = None
                value = value = str(data[col].text)
                row.append((value, hyperlink))
            except IndexError:
                pass
        rows.append(row)
    return rows
