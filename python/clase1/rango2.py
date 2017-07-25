#  variables

rango =["menores 18",">=18 y <=25",'>25']
valores =[0,0,0]
salir=True


while (salir):
	entrada=input("ingrese la edad d una persona : \n ")
	
	if (entrada<=18):
		valores[0]=valores[0]+1
	else:
		if (entrada>=18 and entrada<=25):
			valores[1]=valores[1]+1
		else:
			valores[2]=valores[2]+1
	valor= input("desea ingresar otra edad: 1 si y 2 no  :  ") 
	
	if (valor==2):
		salir=False


print "el numero de estudiastes en el rango:%s es \n%s\n "% (rango[0], valores[0])
print ""
print "el numero de estudiastes en el rango:%s es \n%s\n "% (rango[1], valores[1])
print ""
print "el numero de estudiastes en el rango:%s es \n%s\n "% (rango[2], valores[2])