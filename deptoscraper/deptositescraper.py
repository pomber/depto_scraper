# encoding=latin1
from bs4 import BeautifulSoup
from depto import Depto
import mechanize

class DeptoSiteScraper:
	def __init__(self):
		self.browser = mechanize.Browser()
		
	def get_list(self, search_url):
		deptos = []
		url = search_url
		while url is not None:
			page = self.browser.open(url).read()
			soup = BeautifulSoup(page)
			deptos += self.get_headers(soup)
			url = self.get_next_page_url(soup)
		return deptos
	
	def scrap_results(self, search_url):
		page = self.browser.open(search_url).read()
		soup = BeautifulSoup(page)
		return (self.get_headers(soup), self.get_next_page_url(soup))
	
	def get_depto(self, id, depto_url):
		page = self.browser.open(depto_url).read()
		soup = BeautifulSoup(page)
		dep = Depto()
		dep.id = id
		dep.url = depto_url
		dep.address = self.get_address(soup)
		dep.surface = self.get_surface(soup)
		dep.price = self.get_price(soup)
		dep.photo_count = self.get_photo_count(soup)
		dep.expenses = self.get_expenses(soup)
		dep.room_count = self.get_room_count(soup)
		return dep
		
def clear(text):
	return text.replace("\r", "").replace("\n","").replace("\t","").strip().encode("ascii", "replace")
