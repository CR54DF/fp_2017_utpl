# declaro variables
arreglo =[[7,7,8],[8,9,10],[10,10,3]]
estudiantes=[["maria","loja"],["luis","quito"],["jse",'cuenca']]
promedios=[0,0,0]
# for para recorrer la matriz calcular la suma y el promedio
for x in xrange(0,len(arreglo)):
	suma=0.0
	for y in xrange(x,len(arreglo)):
		suma= suma+arreglo[x][y]
	promedio= suma/len(arreglo[x])
	promedios[x]=promedio
print "--------Reporte----------"
# for para presentar el reporte
for x in xrange(0,len(estudiantes)):
	print "Nombre:%s\n Ciudad:%s\n Promedio:%.2f\t\n"%(estudiantes[x][0], estudiantes[x][1], promedios[x])