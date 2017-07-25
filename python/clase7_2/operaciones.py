# variables
promedio=0.0
#  calcular el promedio
def agregar_lista(lista):
	suma=0
	for x in xrange(0,len(lista)):
		suma=lista[x]+suma
	promedio=suma/len(lista)
	print " promedio  :" , promedio



