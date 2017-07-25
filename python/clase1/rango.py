#  variables
rango =["menores 18",">=18 y <=25",">25"]
valores=[0,0,0]

for x in xrange(0,len(rango)):
	entrada = input("ingrese la edad %s\n"% rango[x])
	
	if (entrada <=18):
		valores[0]=valores[0]+1
	else:
		if (entrada>=18 and entrada<=25):
			valores[1]=valores[1]+1
		else:
			valores[2]=valores[2]+1

for x in xrange(0,len(rango)):
	print "el numero de estudiastes en el rango:%s es %s\n "% (rango[x], valores[x])