# importar modulo y clase estudainte
from estudiante import Estudiante
# variables
suma=0.0
promedio=0.0

if __name__ == '__main__':
	 
	
	e1=Estudiante("",0)
	e2=Estudiante("",0)
# datos q se envia a la clase 
e1.agregar_nombre("martin")
e1.agregrar_promedio(10)
e2.agregar_nombre("luis")
e2.agregrar_promedio(7.5)
lista =[]

lista.append(e1.obtener_promedio)
lista.append(e2.obtener_promedio)

for x in xrange(0,len(lista)):
	suma=suma+lista[x]

promedio=suma/len(lista)

print " promedio  :", promedio