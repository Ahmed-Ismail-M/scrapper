import gspread

s_acc = gspread.service_account('credentials.json')
sh = s_acc.open('books')
ws = sh.worksheet('Sheet1')
print(ws.cell(1,1).value)