# encoding=latin1
from deptositescraper import DeptoSiteScraper

class ArgenPropScraper(DeptoSiteScraper):
			
	def get_next_page_url(self, soup):
		link = soup.find("a",title="Siguiente")
		return link.get("href") if link is not None else None
	
	def get_headers(self, soup):
		listing = soup.find(id="ul_listado_avisos")
		if listing is None:
			raise Exception(soup)
		list_items = listing("li", "ResuAviso")
		headers = [self.get_header(list_item) for list_item in list_items]
		return [header for header in headers if header is not None]
	
	def get_header(self, list_item):
		link = list_item.find("a", "detailsLink")
		if link is not None:
			link_name = link.get("name")
			link_id = link_name.replace("linkDetails_","ap-")
			prefix = "http://www.argenprop.com"
			return {'id': link_id, 'link': prefix + link.get("href")}
		return None
	
	def get_address(self, soup):
		text = soup.find(id="subti").contents[-1] 
		return clear(text)
	
	def get_surface(self, soup):
		li = soup.find_all("div", "ListaUno")[0].ul.li
		text = li.find_all("span")[-1].text
		return clear(text).replace(" m2", "")
	
	def get_price(self, soup):
		price_txt = soup.find_all("div", "datos")[1].find("span","txt")
		return price_txt.text.replace("$ ","").replace(".","")
	
	def get_photo_count(self, soup):
		count = len(soup.find("div", "contGal").find_all("div", "fotos"))
		return str(count)
	
	def get_expenses(self, soup):
		span = soup.find_all("div","ListaUno")[1].ul.li.find("span","res")
		return clear(span.text).replace("$", "")
	
	def get_room_count(self, soup):
		span = soup.find_all("div","ListaUno")[2].ul.find_all("li")[4].find("span","res")
		return clear(span.text)
		
def clear(text):
	return text.replace("\r", "").replace("\n","").replace("\t","").strip().encode("ascii", "replace")
