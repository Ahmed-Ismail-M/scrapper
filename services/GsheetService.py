import gspread
from services.SheetInterface import SheetService

class ExcelService(SheetService):
    def __init__(self, path=None) -> None:
        self.s_acc = gspread.service_account('credentials.json')
        self.sh = self.s_acc.open(path)
        self.ws = self.sh.worksheet('Sheet1')
    def update(self):
        self.ws.update_cell(1,1, '42')
    def read(self, row):
        return super().read()
    
    def write(self, row: int, col: int, value, hyperlink: str):
        self.ws.update_cell(row, col, f"=HYPERLINK({hyperlink})")
        self.ws.update_cell(row, col, value)
