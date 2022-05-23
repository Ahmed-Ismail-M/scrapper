from services.ExcelService import ExcelService
from services.GsheetService import GSheetService
from services.SheetInterface import SheetService
from services.ScrapService import scrap_data
from services.QRService import create_multiple_qr
URL = f"https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9"
EXCEL_PATH = "books.xlsx"
GSHEET_PATH = "https://docs.google.com/spreadsheets/d/1pofeVaaad5ZeA7X2XchAebd8ct5jVKdDPuxP4Rb4TZA/edit?usp=sharing"


def main(sheet_service: SheetService):
    data = scrap_data(url=URL)
    sheet_service.write_multiple(data)
    sheet_service.save()
    print('Data extracted successfully to '+ sheet_service.path)

def generate_pdf():
    data = scrap_data(URL)
    create_multiple_qr(data=data)

# main(GSheetService(GSHEET_PATH))
main(ExcelService(EXCEL_PATH))
