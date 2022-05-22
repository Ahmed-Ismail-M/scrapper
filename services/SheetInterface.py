from abc import ABC, abstractmethod


class SheetService(ABC):
    @abstractmethod
    def read(self):
        pass
    def write(self, row: int, col:int, data, hyperlink:str):
        pass
    def save(self, path:str=''):
        pass