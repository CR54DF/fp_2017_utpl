#  variables

lista =[[7,7,8],[8,9,10],[10,10,3]]

opcion = input("1.ingrese 1 para diagonal \n2.ingrese 2 para infrerior diagonal \n3.ingrese 3 para superior diagonal  ")


for x in xrange(0,len(arreglo)):
	for y in xrange(0,len(arreglo)):
		if (opcion ==1) :
			if (x==y):
				print "%d\t"% (lista[x][y])
		else:
			if (opcion==2):
				if (y>x):
					print "%d\t"%(lista[y][x])
			else:
				if (opcion==3):
					if (y<x):
						print "%d\t"%(lista[y][x])