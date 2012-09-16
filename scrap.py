from deptoscraper import deptoscraper
import sys

#search_url = "http://www.argenprop.com/Alquiler-Departamentos-Barrio-Norte-Con-precio/af_800Kaf_817KpiQKpsQ2900KmQ1KpQ1KrbQ1KvQKaf_1013Kb_5Kb_20Ksb_3Ksb_5"
#search_url = "http://propiedades.zonaprop.com.ar/alquiler-departamentos-capital-federal-belgrano-las-canitas-palermo-recoleta-1-2-amb/ncZ1_opZtipo-operacion-alquiler_lnZ3648+3652+3675+3694_prZars-0-2900_caZcantidad-ambientes-1+cantidad-ambientes-2_miZ50"
#search_url = "http://www.buscainmueble.com/Propiedades/Buscar?sp.RegionBusqueda=1&sp.Pais=1&sp.af_800=800&sp.af_817=817&sp.Barrios_5=5&sp.Barrios_20=20&sp.SubBarrios_3=3&sp.SubBarrios_5=5&ViewNameResult=VistaGrilla&totalCount=1234&totalPages=62&precio_desde=1400&precio_hasta=3360&sp.Moneda=1&sp.PrecioInferior=1400&sp.PrecioSuperior=3360"
search_url = sys.argv[1]
deptoscraper.scrap(search_url)