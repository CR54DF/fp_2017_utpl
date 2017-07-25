# importar modulo
import presenta

nombre = input("Ingrese su nombre : ")
reporte = input("Tipo de reporte  1.   2.")


if (reporte==1):
 	presenta.presentar_mayusculas(nombre)
else:
	if (reporte==2):
 	 	presenta.presentar_minusculas(nombre)
 	else:
 		print "no hay reporte" 
