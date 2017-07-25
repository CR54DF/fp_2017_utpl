# clase cuadrado
class Cuadrado:
    global lado
    def __init__(self, lado):
        self.obtener_lado = lado 


    def agregar_lado(self,lado):
    	self.obtener_lado = lado
      	lado=lado
      	
def calcular_area(lado):
    area = 0;
    area = lado*lado;
    return area;

def calcular_perimetro(lado):
    perimetro = 0;
    perimetro = lado + lado + lado + lado;
    return perimetro;