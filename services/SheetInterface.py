from abc import ABC, abstractmethod


class SheetService(ABC):
    def __init__(self, path) -> None:
        self.path = path
        super().__init__()

    @abstractmethod
    def read(self):
        pass

    def write(self, row: int, col: int, data, hyperlink: str):
        pass

    def save(self):
        pass

    def write_multiple(self, data_list: list):
        pass
