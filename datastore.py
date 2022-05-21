from models.bookModel import Book
from services.ExcelService import ExcelService


class DataStore:
    def __init__(self) -> None:
        self.excelserver = ExcelService(path='test.xlsx')
    def add(self, book: Book):
        for index, value in enumerate(book.__dict__.values()):
            self.excelserver.write(book.id, index+1, value)
            self.excelserver.save('test.xlsx')
    def get_last_id(self)-> int:
        return self.excelserver.get_max_row()+1
    def get_all_books(self):
        
        return self.excelserver.read()
    
    def delete_book(self, index:int):
        self.excelserver.delete(index)
        return 'deleted'