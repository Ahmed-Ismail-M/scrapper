import openpyxl
import requests
from bs4 import BeautifulSoup

from services.ExcelService import ExcelService

URL = "https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9"
PATH = 'test.xlsx'
def write_to_excel(url:str, path:str):
    res = requests.get(url=url).text
    soup = BeautifulSoup(res, "html.parser")
    excel_service = ExcelService()
    result = soup.find("table", class_="wikitable").find_all("tr")[1::1]  # type: ignore
    for row, items in enumerate(result):
        data = items.find_all(["th", "td"])
        links = items.find_all("a", href=True)
        for col in range(len(data)):
            try:
                
                value = str(data[col].text)
                if col <= len(links):
                    hyperlink = "https://ar.wikipedia.org/" + links[col-1]['href']  # type: ignore
                    excel_service.write_to_excel_with_hyperlink(row=row+1, col=col+1, data=value, hyperlink=hyperlink )
                else:
                    excel_service.write_to_excel(row=row+1, col=col+1, data=value)
            except IndexError:
                pass

    excel_service.save(path=path)
write_to_excel(url=URL, path=PATH)

