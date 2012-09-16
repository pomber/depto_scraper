from deptoscraper import deptoscraper

#search_url = "http://www.argenprop.com/Alquiler-Departamentos-Barrio-Norte-Con-precio/af_800Kaf_817KpiQKpsQ2900KmQ1KpQ1KrbQ1KvQKaf_1013Kb_5Kb_20Ksb_3Ksb_5"
search_url = sys.argv[1]
deptoscraper.scrap(search_url)