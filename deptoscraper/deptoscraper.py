from zonapropscraper import ZonaPropScraper
from argenpropscraper import ArgenPropScraper
from deptodatasource import DeptoDataSource
from config import config
import sys	
		
def scrap(search_url):
	scraper = choose_scraper(search_url)
	repository = DeptoDataSource(config)

	page_url = search_url
	page_index = 1

	while page_url is not None:
		page_url = scrap_page(scraper, repository, page_url, page_index)		
		page_index += 1

def choose_scraper(url):	
	if "argenprop" in url:
		return ArgenPropScraper()
	elif "zonaprop" in url:
		return ZonaPropScraper()
	else:
		raise Exception("Unrecognized search URL")

def scrap_page(scraper, repository, url, page_index):
	print "--- Scraping page {0} ---".format(page_index)
	headers, next_url = scraper.scrap_results(url)
	for header in headers:
		if header["id"] not in repository.ids:
			scrap_depto(scraper, repository, header["id"], header["link"])
	return next_url

def scrap_depto(scraper, repository, depto_id, depto_url):
	depto = scraper.get_depto(depto_id, depto_url)	
	if should_save(depto):
		print "Adding {0}".format(depto_id)
		repository.add(depto)

def should_save(depto):
	return depto.photo_count > 1