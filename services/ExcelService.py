
import openpyxl

class ExcelService:
    def __init__(self) -> None:
        self.wb = None
        self.ws = None
    def creat_wb(self):
        self.wb = openpyxl.Workbook()  # open workboopk
        self.ws = self.wb.active  # open sheet
    def write_to_excel_with_hyperlink(self, row:int, col:int, data:str, hyperlink:str):
        if self.ws:
            self.ws.cell(row + 1, col + 1, data).hyperlink = hyperlink # type: ignore
    def write_to_excel(self, row:int, col:int, data:str):
        if self.ws:
            self.ws.cell(row + 1, col + 1, data)
    def save(self, path: str):
        if self.wb:
            self.wb.save(path)
