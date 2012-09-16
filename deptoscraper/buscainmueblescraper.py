# encoding=latin1
from deptositescraper import DeptoSiteScraper
from deptositescraper import clear

class BuscaInmuebleScraper(DeptoSiteScraper):

	def get_next_page_url(self, soup):
		pager = soup.select(".paginado")[0]
		if pager is None:
			return None
		pager_links = pager('a')
		for link in pager_links:
			if "Siguiente" in link.text:
				return "http://www.buscainmueble.com" + link.get("href")
		return None
	
	def get_headers(self, soup):
		listing = soup.select("ul.Items")[0]
		list_items = listing.select("li.Desc")
		headers = [self.get_header(list_item) for list_item in list_items]
		return [header for header in headers if header is not None]

	def get_header(self, item):
		link = item.select("a.detailsLink")
		if len(link) is 0:
			return None		
		link = link[0]

		link_name = link.get("name")
		link_href = "http://www.buscainmueble.com" + link.get("href")
		item_id = "bi-" + link_name[12:]
		return {"id": item_id, "link": link_href}
	
	def get_address(self, soup):
		data = soup.select(".Fl.FilaDatos")[0]
		text = data.select(".Detalle")[3].text[18:]
		return clear(text)
	
	def get_surface(self, soup):
		text = self.get_feature(soup, "Superficie Cubierta")
		return clear(text)
	
	def get_price(self, soup):
		data = soup.select(".Fl.FilaDatos")[0]
		text = data.select(".Detalle")[0].text
		return clear(text)
	
	def get_photo_count(self, soup):
		return len(soup.select("#thumbnails li"))
	
	def get_expenses(self, soup):
		text = self.get_feature(soup, "Expensas")
		return clear(text)
	
	def get_room_count(self, soup):
		text = self.get_feature(soup, "Cantidad de ambientes")
		return clear(text)
	
	def get_feature(self, soup, feature):
		features = soup.select(".Lista.Final")[0].select("span")
		label = [f for f in features if feature in f.text][0]
		text = label.next_sibling.next_sibling.text
		return text
