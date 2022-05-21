import openpyxl


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
            self.ws.cell(row + 1, col + 1, data).hyperlink = hyperlink  # type: ignore

    def write(self, row: int, col: int, data: str):
        if self.ws:
            self.ws.cell(row + 1, col + 1, data)

    def save(self, path: str):
        if self.wb:
            self.wb.save(path)

    def get_max_row(self) -> int:
        if self.ws:
            return self.ws.max_row
        return 0
