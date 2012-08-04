from zonapropscraper import ZonaPropScraper
from argenpropscraper import ArgenPropScraper
from deptodatasource import DeptoDataSource
import sys

search_url = sys.argv[1]
if "argenprop" in search_url:
	scraper = ArgenPropScraper()
elif "zonaprop" in search_url:
	scraper = ZonaPropScraper()
else:
	raise Exception("Unrecognized search URL")
	
repository = DeptoDataSource()

def scrap_all():
	headers = scraper.get_list(search_url)
	index = 1
	total = len(headers)
	for header in headers:
		if header["id"] in repository.ids:
			pass #print "{0}/{1} - Ignoring {2}".format(index, total, header["id"])
		else:
			print "{0}/{1} - Adding {2}".format(index, total, header["id"])
			depto = scraper.get_depto(header["id"], header["link"])
			repository.add(depto)
		index += 1
		
def scrap_by_page():
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

scrap_by_page()
