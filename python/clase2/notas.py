# variables
lista =[[7,7,8],[8,9,10],[10,10,3]]

for x in xrange(0,len(lista)):
	suma =0.0
	
	for y in xrange(0,len(lista)):
		print "%d\t"%(lista[x][y])
		suma =suma+lista[x][y]
		
	promedio = suma/len(lista[x])
	print "Promedio %.2f" %(promedio)
	print ""