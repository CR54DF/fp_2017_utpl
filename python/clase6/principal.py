# se importa el modulo y la clase 
from estudiante import Estudiante

suma_edades=0
promedio = 0.0
if __name__ == '__main__':
	 # clase iniciada
	e1 =Estudiante("juan",5)
	e2 =Estudiante("maria",15)
    
    

# calcular 
suma_edades=e1.edad+e2.edad
promedio= suma_edades/2
# imprime el valor 
print promedio