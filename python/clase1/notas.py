#  variables
suma=0
promedio =0
notas=[]
materias=["programacion","base de datos","contabilidad","biologia"]
 

for x in xrange(0,len(materias)):
	entrada= input ("ingrese la nota %s\n"% materias[x])
	notas.append(entrada)
print "-------------------"

for x in xrange(0,len(materias)):
	print "las nota de %s fue %s\n"% (materias[x], notas[x])
	

for x in xrange(0,len(notas)):
	suma= suma + notas[x]

promedio = suma / len(materias)

print "El promedio es %.2f\n"%promedio

if (promedio>=80):
	print "sobresaliente :\t%s"% promedio
elif (promedio>=60):
	print "Buena :\t%s"% promedio
else :
	print "Regular:\t%s"% promedio