from models.bookModel import Book
from services.ExcelService import ExcelService

PATH = 'test.xlsx'
class DataStore:
    def __init__(self) -> None:
        try:
            self.excel_service = ExcelService(path=PATH)
        except FileNotFoundError:
            self.create_database()
    def add(self, book: Book):
        for index, value in enumerate(book.__dict__.values()):
            self.excel_service.write(book.id, index+1, value)
            self.excel_service.save(PATH)
    def get_last_id(self)-> int:
        max_id = self.excel_service.get_max_row()
        return max_id+1
    def get_all_books(self):
        
        return self.excel_service.read()
    
    def delete_book(self, index:int):
        self.excel_service.delete(index)
        self.excel_service.save(PATH)
        return 'deleted'
    def create_database(self):
        self.excel_service = ExcelService()
        self.excel_service.save(PATH)