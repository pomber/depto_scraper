import gspread

class DeptoDataSource:
	
	def __init__(self):
		gc = gspread.login("your_google_username", "your_google_password")
		self.sheet = gc.open("your_google_spreadsheet_name").sheet1
		self.new_row = int(self.sheet.cell(1,1).value) + 2
		self.ids = self.sheet.col_values(2)
		
	def add(self, depto):		
		new_cells = self.sheet.range('B{0}:I{0}'.format(self.new_row))
		new_cells[0].value = depto.id
		new_cells[1].value = depto.price
		new_cells[2].value = depto.expenses
		new_cells[3].value = depto.surface
		new_cells[4].value = depto.room_count
		new_cells[5].value = depto.photo_count
		new_cells[6].value = depto.address
		new_cells[7].value = "=hyperlink(\"{0}\",\"link\")".format(depto.url)
		self.new_row += 1
		self.ids.append(depto.id)
		self.sheet.update_cells(new_cells)
