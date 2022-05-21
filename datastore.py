from models.bookModel import Book
from services.ExcelService import ExcelService

PATH = 'test.xlsx'
class DataStore:
    def __init__(self) -> None:
        try:
            self.excelserver = ExcelService(path=PATH)
        except FileNotFoundError:
            self.create_database()
    def add(self, book: Book):
        for index, value in enumerate(book.__dict__.values()):
            self.excelserver.write(book.id, index+1, value)
            self.excelserver.save(PATH)
    def get_last_id(self)-> int:
        max_id = self.excelserver.get_max_row()
        return max_id+1
    def get_all_books(self):
        
        return self.excelserver.read()
    
    def delete_book(self, index:int):
        self.excelserver.delete(index)
        self.excelserver.save(PATH)
        return 'deleted'
    def create_database(self):
        self.excelserver = ExcelService()
        self.excelserver.save(PATH)