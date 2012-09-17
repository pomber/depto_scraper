# encoding=latin1
from deptositescraper import DeptoSiteScraper
from deptositescraper import clear
#import urllib

class IccawebScraper(DeptoSiteScraper):

	def get_next_page_url(self, soup):
		pager = soup.find(id="paginacion")
		if pager is None:
			return None
		pager_links = pager('a')
		for link in pager_links:
			if link.text == ">":
				#url = urllib.quote_plus(link.get("href").encode('utf-8'))
				return "http://www.iccaweb.com.ar" + link.get("href")
		return None
	
	def get_headers(self, soup):
		listing = soup.find(id="propiedades_registros")
		list_items = listing.select("div.propiedades_registro")
		headers = [self.get_header(list_item) for list_item in list_items]
		return [header for header in headers if header is not None]

	def get_header(self, item):
		if item.find(title="alquilado.png") is not None:
			return None
		if item.find(title="reservado.png") is not None:
			return None

		link = item.select("div.ver_detalles_propiedad")[0].find("a").get("href")
		link_href = "http://www.iccaweb.com.ar" + link
		item_id = "iw-" + link[24:-4]
		return {"id": item_id, "link": link_href}
	
	def get_address(self, soup):
		street = soup.select("#detalle_calle div")[0].text
		number = soup.select("#nro_numero")[0].text
		text = street + " " + number
		return clear(text)
	
	def get_surface(self, soup):
		return self.get_feature(soup, "#sup_total_numero")
	
	def get_price(self, soup):
		return self.get_feature(soup, "#precio_numero").replace(".","")
	
	def get_photo_count(self, soup):
		return len(soup.select("#galeria_img div.contenedor"))
	
	def get_expenses(self, soup):
		return self.get_feature(soup, "#detalle_valor_expensas div.texto")
	
	def get_room_count(self, soup):
		return self.get_feature(soup, "#detalle_id_ambientes div.texto")[0]

	def get_feature(self, soup, selector):
		label = soup.select(selector)
		if len(label) is 0:
			return "-"
		text = label[0].text
		return clear(text)
