from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    country: str
    def __post_init__(self):
        try:
            self.id = int(self.id)
            self.title = str(self.title)
            self.author = str(self.author)
            self.country = str(self.author)
        except Exception:
            raise ValueError('Invalid inputs')