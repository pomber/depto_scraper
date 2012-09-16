from os import path
import datetime
import gspread
import pickle

class DeptoDataSource:
	
	def __init__(self, config):
		print "Initializing repository..."

		username = config["google.username"]
		password = config["google.password"]
		sheetname = config["google.sheetname"]
		self._use_cache = config["ids-cache.on"]

		gc = gspread.login(username, password)
		self.sheet = gc.open(sheetname).sheet1
		self.new_row = int(self.sheet.cell(1,1).value) + 2

		self.ids = self._get_ids()
		
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
		self.sheet.update_cells(new_cells)

		self.ids.add(depto.id)
		if self._use_cache:
			filename = get_today_cache_filename()
			self._save_ids_to_file(self.ids, filename)

	def _get_ids(self):
		if not self._use_cache:
			return self._get_ids_from_sheet()

		cache_filename = get_today_cache_filename()
		if path.exists(cache_filename):			
			return self._get_ids_from_file(cache_filename)
		else:
			ids = self._get_ids_from_sheet()
			self._save_ids_to_file(ids, cache_filename)
			return ids

	def _get_ids_from_sheet(self):
		print "Getting ids from spreadsheet..."	
		return set(self.sheet.col_values(2))

	def _get_ids_from_file(self, filename):
		print "Getting ids from local cache..."	
		with open(filename, "rb") as cache_file:
			return pickle.load(cache_file)

	def _save_ids_to_file(self, ids, filename):
		with open(filename, "wb") as cache_file:
			pickle.dump(ids, cache_file)

def get_today_cache_filename():
	today = datetime.date.today()
	return today.strftime("%Y%m%d.cache")

