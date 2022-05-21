
import openpyxl

class ExcelServer:
    def __init__(self) -> None:
        self.wb = openpyxl.Workbook()  # open workboopk
        self.ws = self.wb.active  # open sheet
    def write_to_excel_with_hyperlink(self, row:int, col:int, data:str, hyperlink:str):
        self.ws.cell(row + 1, col + 1, str(data)).hyperlink = hyperlink # type: ignore
    def write_to_excel(self, row:int, col:int, data:str):
        self.ws.cell(row + 1, col + 1, str(data))
