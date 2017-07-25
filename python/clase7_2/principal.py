# importa clase y modulo estudiate
from estudiante import Estudiante
import operaciones
suma=0
promedio =0.0

if __name__ == '__main__':
	 #Instancia la clase
	
	e1=Estudiante("",0)
	e2=Estudiante("",0)
#  datos
e1.agregar_nombre("luis")
e1.agregrar_promedio(10)
e2.agregar_nombre("santiago")
e2.agregrar_promedio(7.5)

lista=[0,0]
lista[0]=e1.obtener_promedio
lista[1]=e2.obtener_promedio
# enviar lista y calcular promedio con metodo
operaciones.agregar_lista(lista)


