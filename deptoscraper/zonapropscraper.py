# encoding=latin1
from deptositescraper import DeptoSiteScraper

class ZonaPropScraper(DeptoSiteScraper):
			
	def get_next_page_url(self, soup):
		pager = soup.find(id="paginacion")
		if pager is None:
			return None
		pager_links = pager('a')
		for link in pager_links:
			if link.text == "Siguiente":
				return link.get("href")
		return None
	
	def get_headers(self, soup):
		listing = soup.find(id="listado")
		list_items = listing("div", "aviso")
		headers = [self.get_header(list_item) for list_item in list_items]
		return [header for header in headers if header is not None]
	
	def get_header(self, list_item):
		item_id = "zp-" + list_item.get("id")
		link = list_item.h2.a
		if link is not None:
			return {'id': item_id, 'link': link.get("href")}
		return None
	
	def get_address(self, soup):
		text = soup.find("div","meta").dl.find_all("dd")[1].li.text
		return clear(text)
	
	def get_surface(self, soup):
		text = soup.find("div","meta").find_all("dl")[2].dd.text
		return clear(text)
	
	def get_price(self, soup):
		text = soup.find("div","grid_7").p.text.replace("$","")
		return clear(text)
	
	def get_photo_count(self, soup):
		thumbs = soup.select(".miniaturas .items")
		if len(thumbs) is 0:
			return "0"
		count = len(thumbs[0].select("img"))
		return str(count)
	
	def get_expenses(self, soup):
		return self.get_feature(soup, "Expensas ($):")	
	
	def get_room_count(self, soup):
		return self.get_feature(soup, "Ambientes:")	
	
	def get_feature(self, soup, feature):
		label = soup.select(".caracteristicas")[0].find("dt",text=feature)
		text = label.next_sibling.next_sibling.text
		return text
		
def clear(text):
	return text.replace("\r", "").replace("\n","").replace("\t","").strip().encode("ascii", "replace")
