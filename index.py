import requests
from bs4 import BeautifulSoup
import pandas as pd
from services.ExcelService import ExcelService
from services.GsheetService import GSheetService
from services.SheetInterface import SheetService

URL = "https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9"
PATH = 'test.xlsx'
def write_to_sheet(url:str, sheet_service: SheetService):
    res = requests.get(url=url).text
    soup = BeautifulSoup(res, "html.parser")
    result = soup.find("table", class_="wikitable").find_all("tr")[1::1]  # type: ignore
    for row, items in enumerate(result):
        data = items.find_all(["th", "td"])
        for col in range(len(data)):
            try:
                if data[col].find('a'):
                    hyperlink = "https://ar.wikipedia.org/" + data[col].find('a').get('href')  # type: ignore
                else:
                    hyperlink=None
                value = str(data[col].text)
                sheet_service.write(row=row+1, col=col+1, data=value, hyperlink=hyperlink)
            except IndexError:
                pass
    sheet_service.save()

def scrap(url:str)-> list:
    res = requests.get(url=url).text
    soup = BeautifulSoup(res, "html.parser")
    result = soup.find("table", class_="wikitable").find_all("tr")[1::1]  # type: ignore
    rows = []
    for items in result:
        data = items.find_all(["th", "td"])
        row = []
        for col in range(len(data)):
            try:
                if data[col].find('a'):
                    hyperlink = "https://ar.wikipedia.org/" + data[col].find('a').get('href')  # type: ignore
                    value = f"=HYPERLINK(\"{hyperlink}\",\"{str(data[col].text)}\")"
                else:
                    value=value = str(data[col].text)
            
                row.append(value)
            except IndexError:
                pass
        rows.append(row)
    return rows
# write_to_sheet(url=URL,  sheet_service=GSheetService(path='books'))
# write_to_sheet(url=URL,  sheet_service=ExcelService(path=PATH))
print(scrap(url=URL))
df = pd.DataFrame(scrap(url=URL))
# df.apply(lambda s:s.str.replace("''", ""))
GSheetService(path='books').write_multiple(df)
print(df)