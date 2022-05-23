import gspread
from services.SheetInterface import SheetService
from pandas.core.frame import DataFrame
import pandas as pd
class GSheetService(SheetService):
    def __init__(self, url=None) -> None:
        self.s_acc = gspread.service_account('credentials.json')
        self.sh = self.s_acc.open_by_url(url)
        self.ws = self.sh.worksheet('Sheet1')
    
    def read(self):
        return super().read()
    
    def write(self, row: int, col: int, data, hyperlink: str):
        if hyperlink == None:
            self.ws.update_cell(row, col, data)
            return
        self.ws.update_cell(row, col, f'=HYPERLINK("{hyperlink}","{data}")')

    def write_multiple(self, data_list: list):
        df = pd.DataFrame(data_list)
        df= df.applymap(self.check_hyperlink)
        self.ws.update(df.values.tolist(), value_input_option='USER_ENTERED')

    def check_hyperlink(self, t: tuple):
        if isinstance(t, tuple): # IF the value has hyperlink
            return f'=HYPERLINK("{t[1]}","{t[0]}")'
        return t[0]
    def save(self):
        return super().save()