
def generar_recibo(nombre, apellido, cedula, edad, sueldo_neto):
	nombre_mayuscula= obtener_mayuscula(nombre)
	descuento = obtener_descuento(sueldo_neto, edad)
	seguro = obtener_seguro(sueldo_neto)
	sueldo_final = sueldo_neto + seguro - descuento
	print "\t-------------Recibo---------------\nNombre:%s\tApellido:%s\tcedula:%s\nSueldo final es:%.2f\n\t----------------------------------"% (nombre_mayuscula, apellido, cedula, sueldo_final)


def obtener_descuento( valor,  edad):
	d=0.0
	if (edad>=50):
		d=valor*0.05
	else:
		d =valor*0.01
	return d	

def  obtener_seguro( v2):
	s= v2*0.05
	return s

def obtener_mayuscula( valor):
	 valor = valor.upper()
	 return valor