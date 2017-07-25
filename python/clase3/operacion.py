#  imprimir  segun la opcion que se elija
def imprimir(val1,val2,op):
	if(op==1):
		presenta_suma(val1,val2)
	else:
		if (op==2):
			presenta_resta(val1,val2)
		else:
			if (op==3):
				presenta_mult(val1,val2)
			else:
				if (op==4):
					presenta_div(val1,val2)
				else:
					print "no existe"


def presenta_suma(valor1,valor2):
	suma= val1+val2
	print "la suma%f mas %f\nes igual a \n\t%f"%(val1, val2, suma)

def presenta_resta(val1,val2):
	resta= val1+val2
	print "la resta%f menos %f\nes igual a \n\t%f"%(val1, val2, resta)

def presenta_mult(val1,val2):
	mul= val1*val2
	print "la multiplicacion%f por %f\nes igual a \n\t%f"%(val1, val2, mul)

def presenta_div(val1,val2):
	div= val1/val2
	print "la division%f para %f\nes igual a \n\t%f"%(val1, val2, div)		
	