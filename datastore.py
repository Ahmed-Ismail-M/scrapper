from models.bookModel import Book
from services.ExcelService import ExcelService


class DataStore:
    def __init__(self) -> None:
        self.excelserver = ExcelService(path='test.xlsx')
    def add(self, book: Book):
        for index, value in enumerate(book.__dict__):
            self.excelserver.write_to_excel(self.excelserver.get_max_row(), index, value)
    def get_last_id(self)-> int:
        return self.excelserver.get_max_row() 