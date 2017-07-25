#  variables
suma =0
promedio=0
dias=["lunes","martes","miercles","jueves","viernes","sabado","domingo"]
respuestas =[]

for x in xrange(0,len(dias)):
	entrada =input("Numero de partidos jugados el dia %s\n"%(dias[x]))
	respuestas.append(entrada)

print "---------------------"
 
for x in xrange(0,len(dias)):
	print "Partidos jugados el dia %s fue %s\n"% (dias[x], respuestas[x])


for x in xrange(0,len(respuestas)):
	suma=suma+respuestas[x]

promedio = suma / len(respuestas)

print "El promedio de partidos jugados es %.2f\n"% promedio
