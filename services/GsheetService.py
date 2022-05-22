import gspread
class ExcelService:
    def __init__(self, path=None) -> None:
        self.s_acc = gspread.service_account('credentials.json')
        self.sh = self.s_acc.open(path)
        self.ws = self.sh.worksheet('Sheet1')
    def update(self):
        self.ws.update_cell(1,1, '42')