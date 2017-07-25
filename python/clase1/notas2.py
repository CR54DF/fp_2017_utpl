#  variables
notas=[]
total=0
parametros=["asistencia","prueba","leccion","participacion"]

for x in xrange(0,len(parametros)):
	entrada= input("ingrese la nota de : %s\n"% parametros[x])
	notas.append(entrada)
print "\t--------resultado----------\n","        \tlas notas son"

for x in xrange(0,len(parametros)):
	total=total+notas[x]

for x in xrange(0,len(parametros)):
	print "la nota de %s es %s\n"% (parametros[x], notas[x])

resultado=total/len(parametros)

if (resultado>7 & resultado<=10):
	print  "\naprobado con %s"% resultado
else :
	print "\nreprobado con %s"% resultado