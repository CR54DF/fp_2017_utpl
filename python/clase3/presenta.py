
def presentar_mayusculas(nombre):
	print nombre.upper()

def presentar_minusculas(nombre):
	print nombre.lower()


def presenta_impresion(opcion, valor):
	if (opcion==1):
		presentar_mayusculas(valor)
	else: 
		if (opcion==2):
			presentar_minusculas(valor)
		else:
			print "no hay reporte"