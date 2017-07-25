#  variables
lista =[[7,7,8],[8,9,10],[10,10,3]]
suma=0

for x in xrange(0,len(lista)):
	for y in xrange(0,len(lista)):
		if (x==y):
			print "%d\t"%lista[x][y]
			suma= suma +lista[x][y]

print  suma