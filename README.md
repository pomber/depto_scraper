This was my first python script. It takes a search url from web sites with apartments for rent and upload the new apartments (compared with a previous run) to a google spreadsheet.

I'm from Argentina so it only works with argentinian sites: www.argenprop.com and zonaprop.com.ar.

The idea was to get a working script quickly without caring about readability or maintainability so the code may be a bit messy and with some spanish words ("depto" means apartement). But, since I posted about this in a reddit post, and some people asked me to see the code, I've uploaded it to github.

It uses the following libraries:  
bs4  
mechanize  
gspread  

Usage example (first you need to set your google account information on deptodatasource.py):  
deptoscraper.py http://propiedades.zonaprop.com.ar/alquiler-departamentos-4-amb/ncZ1_tdZtipo-departamento-otro_opZtipo-operacion-alquiler_caZcantidad-ambientes-4_agZ1+3_formatZlist_soZempdesc 