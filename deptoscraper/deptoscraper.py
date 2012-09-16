from zonapropscraper import ZonaPropScraper
from argenpropscraper import ArgenPropScraper
from deptodatasource import DeptoDataSource
from config import config
import sys	
		
def scrap(search_url):
	scraper = choose_scraper(search_url)
	repository = DeptoDataSource(config)

	url = search_url
	page = 1
	while url is not None:
		headers, url = scraper.scrap_results(url)
		index = 1
		total = len(headers)
		print "--- Scraping page {0} ---".format(page)
		for header in headers:
			if header["id"] in repository.ids:
				pass #print "{0}/{1} - Ignoring {2}".format(index, total, header["id"])
			else:
				print "{0}/{1} - Adding {2}".format(index, total, header["id"])
				depto = scraper.get_depto(header["id"], header["link"])
				repository.add(depto)
			index += 1
		page += 1

def choose_scraper(url):	
	if "argenprop" in url:
		return ArgenPropScraper()
	elif "zonaprop" in url:
		return ZonaPropScraper()
	else:
		raise Exception("Unrecognized search URL")