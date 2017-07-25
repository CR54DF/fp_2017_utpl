def parcial2():
	""" ejercicio numero 2 de la prueba parcial"""
	estudiantes, mayor, promedio, tot = 0, 0, 0, 0
	calif = []
	estudiantes = int(input("Cantidad de estudiantes: "))
	for i in range(0, estudiantes + 1):
		calif[i] = input("Ingrese la nota del estudiante" + i)
	for i in range(0, estudiante + 1):
		if(calif[i] > mayor):
			mayor = calif[i]
		tot = tot + calif[i]
	print("La mayor nota es: %d" % mayor)
	promedio = tot / estudiantes
	print("El promedio es: %.2f " % promedio)
	if(promedio >= 90):
		print("El estudiante tiene sobresaliente")
	if(promedio >= 70 and promedio < 90):
		print("El estudiante tiene un resultado muy bueno")
	if(promedio >= 45 and promedio < 70):
		print("El estudiante es bueno")
	if(promedio <= 45):
		print("El estudiante tiene un resultado regular")






