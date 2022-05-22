import gspread
from services.SheetInterface import SheetService

class GSheetService(SheetService):
    def __init__(self, path=None) -> None:
        self.s_acc = gspread.service_account('credentials.json')
        self.sh = self.s_acc.open(path)
        self.ws = self.sh.worksheet('Sheet1')
    def update(self):
        self.ws.update_cell(1,1, '42')
    def read(self):
        return super().read()
    
    def write(self, row: int, col: int, data, hyperlink: str):
        if hyperlink == None:
            self.ws.update_cell(row, col, data)
            return
        self.ws.update_cell(row, col, f'=HYPERLINK("{hyperlink}","{data}")')

    def save(self):
        return super().save()