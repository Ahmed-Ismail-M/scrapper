from models.bookModel import Book
from services.ExcelService import ExcelService


class DataStore:
    def __init__(self) -> None:
        self.excelserver = ExcelService(path='test.xlsx')
    def add(self, book: Book=None):
        self.excelserver.read()
