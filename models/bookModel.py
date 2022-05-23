from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    country: str
    def __post_init__(self):
        self.id = int(self.id)