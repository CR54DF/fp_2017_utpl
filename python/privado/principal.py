# importar modulo estudiante y estudiante
from estudiante import Estudiante
# declaro variables
suma=0.0
promedio=0.0

if __name__ == '__main__':

	e1=Estudiante("",0)
	e2=Estudiante("",0)
#enviar datos a la clase 

e1.agregar_nombre("martin")
e1.agregrar_edad(14)
e2.agregar_nombre("juan")
e2.agregrar_edad(19)

# hacer las operaciones
suma =e1.obtener_edad + e2.obtener_edad
promedio = suma/2

print "el promedio es :", promedio