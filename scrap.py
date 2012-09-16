from deptoscraper import deptoscraper

#search_url = "http://www.argenprop.com/Alquiler-Departamentos-Barrio-Norte-Con-precio/af_800Kaf_817KpiQKpsQ2900KmQ1KpQ1KrbQ1KvQKaf_1013Kb_5Kb_20Ksb_3Ksb_5"
search_url = "http://propiedades.zonaprop.com.ar/alquiler-departamentos-capital-federal-belgrano-las-canitas-palermo-recoleta-1-2-amb/ncZ1_opZtipo-operacion-alquiler_lnZ3648+3652+3675+3694_prZars-0-2900_caZcantidad-ambientes-1+cantidad-ambientes-2_miZ50"
#search_url = sys.argv[1]
deptoscraper.scrap(search_url)