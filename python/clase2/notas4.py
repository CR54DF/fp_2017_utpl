#  variables
arreglo =[[7,7,8],[8,9,10],[10,10,3]]
suma=0

for x in xrange(0,len(arreglo)):
	for y in xrange(0,len(arreglo)):
		if (x>y):
			print "%d\t"%arreglo[x][y]
			suma= suma +arreglo[x][y]

print ""
print  suma