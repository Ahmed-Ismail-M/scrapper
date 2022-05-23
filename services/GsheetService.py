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
        df= df.apply(self.tuple_to_value)
        print(df)
        # self.ws.update(df.values.tolist(), value_input_option='USER_ENTERED')

    def tuple_to_value(self, t: tuple):
        hyperlink = "https://ar.wikipedia.org/" + t[1]  # type: ignore
        value = f'=HYPERLINK("{hyperlink}","{t[0]}")'
        return value
    def save(self):
        return super().save()