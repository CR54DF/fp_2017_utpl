from cuadrado import Cuadrado
import cuadrado
for x in xrange(0,4):
	c=input("Ingrese el valor del lado : ")
	if __name__ == '__main__':
	 
		lado=Cuadrado("")
		lado.agregar_lado(c)
	

	lad=lado.obtener_lado
	area=cuadrado.calcular_area(c)
	perimetro=cuadrado.calcular_perimetro(c)
	print perimetro
	print "Cuadrado con lado%d\n\tArea=%d\n\tPreimetro=%d\n"%(c, area, perimetro)