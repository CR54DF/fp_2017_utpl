
from random import randint

class Dado():

        def generarNumAleatorio(self):
            numAleatorio = randint(1,6)
            return numAleatorio

        def sumarDado(self,dado):
            resultado = []
            can = len(dado)
            cont = 0
            valor1 = 0
            valor2 = 0
            while cont < can:
                if cont <=3:
                    valor1 = valor1 + dado[cont]
                if cont >= 4:
                    valor2 = valor2 + dado[cont]
                cont = cont + 1
            resultado.append(valor1)
            resultado.append(valor2)
            return resultado
        def ganador(self, ganador):
            if ganador[0] > ganador[1]:
                print ' Felicidades, primer lugar Persona 1 con ',ganador[0]
                print ' Genial, segundo  lugar Persona 2 con ',ganador[1]
            if ganador[0] < ganador[1]:
                print ' Felicidades, primer lugar Persona 2 con ',ganador[1]
                print ' Genial, segundo  lugar Persona 1 con ',ganador[0]
            if ganador[0] == ganador[1]:
                print ' Felicidades, Han empatado Persona 1 y Persona 2 con ',ganador[0]


dado = Dado()
numA = 0
dadoDate = []
contPer = 1
contIntentos = 1
while contPer <= 2:
    print '============================================'
    while contIntentos <= 4:
        print 'Persona (',contPer,')'
        print 'lanzar dado Nro (',contIntentos,')'
        numA = dado.generarNumAleatorio()
        dadoDate.append(numA)
        print 'Dado =',numA
        print '----------------------'
        contIntentos = contIntentos + 1
    contIntentos = 1
    contPer = contPer + 1
resultado = dado.sumarDado(dadoDate)
dado.ganador(resultado)
