import openpyxl
from models.bookModel import Book

class ExcelService:
    def __init__(self, path=None) -> None:
        if path:
            self.wb = openpyxl.load_workbook(path)
            self.ws = self.wb.active
        else:
            self.wb = openpyxl.Workbook()  # open workboopk
            self.ws = self.wb.active  # open sheet

    def write_with_hyperlink(self, row: int, col: int, data: str, hyperlink: str):
        if self.ws:
            self.ws.cell(row, col, data).hyperlink = hyperlink  # type: ignore

    def write(self, row: int, col: int, data: str):
        if self.ws:
            self.ws.cell(row, col, data)

    def save(self, path: str):
        if self.wb:
            self.wb.save(path)

    def get_max_row(self) -> int:
        if self.ws:
            return self.ws.max_row
        return 0

    def read(self) -> dict:
        books = {}
        for r in range(self.ws.max_row):
            books[r+1] = Book(
                id=self.ws.cell(r + 1, 1).value,
                title=self.ws.cell(r + 1, 2).value,
                author=self.ws.cell(r + 1, 3).value,
                country=self.ws.cell(r + 1, 4).value,
            ).__dict__
        return books
