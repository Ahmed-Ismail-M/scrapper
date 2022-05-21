import openpyxl
from models.bookModel import Book

class ExcelService:
    def __init__(self, path=None) -> None:
        if path:
            self.wb = openpyxl.load_workbook(path)
            self.ws = self.wb.active
        else:
            self.wb = openpyxl.Workbook()  # new workboopk
            self.ws = self.wb.active  # new sheet
    def write(self, row: int, col: int, data: str, hyperlink=None):
        if self.ws:
            self.ws.cell(row, col, data).hyperlink = hyperlink

    def save(self, path: str):
        if self.wb:
            self.wb.save(path)

    def get_max_row(self) -> int:
        if self.ws:
            return self.ws.max_row
        return 0

    def delete(self, row: int):
        if self.ws:
            for index in range(self.ws.max_column):
                self.ws.cell(row, index+1).value = None
    def read(self) -> dict:
        books = {}
        print(self.ws.max_row)
        for r in range(self.ws.max_row):
            print(self.ws.cell(r+1,1).value)
            # if self.ws.cell(r+1,1).value:
            books[str(self.ws.cell(r + 1, 1).value)] = Book(
                id=self.ws.cell(r + 1, 1).value,
                title=self.ws.cell(r + 1, 2).value,
                author=self.ws.cell(r + 1, 3).value,
                country=self.ws.cell(r + 1, 4).value,
            ).__dict__
            
        return books
