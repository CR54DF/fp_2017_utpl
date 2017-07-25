def parcial():
	""" hola """
	cont = 1
	mayor = 0
	sueldo_semanal = 0
	sueldo_semanal2 = 0
	sueldo_semanal3 = 0
	sueldo_semanal4 = 0
	sueldo_semanal5 = 0
	semanal = [0, 0, 0, 0, 0]
	salario1 = [0, 0, 0, 0, 0, 0]
	salario2 = [0, 0, 0, 0, 0, 0]
	salario3 = [0, 0, 0, 0, 0, 0]
	salario4 = [0, 0, 0, 0, 0, 0]
	salario5 = [0, 0, 0, 0, 0, 0]
	dia = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

	while(cont <= 5):
		vendedor = int(input("Ingrese el vendedor del que desea realizar el calculo: 1-2-3-4-5:  "))
		if(vendedor == 1):
			print("Trabajador 1\n")
			for i in range(0, 6):
				print("Dia %s\n" %dia[i])
				cantidad = int(input("Ingrese la cantidad vendida en el dia: "))
				if (cantidad <= 100):
					salario1[i] = 30 + (cantidad * 0.15)
				if (cantidad > 100 and cantidad < 999):
					salario1[i] = 50 + (cantidad * 0.15)
				if (cantidad >= 100):
					salario1[i] = 80 + (cantidad * 0.15)
				sueldo_semanal = sueldo_semanal + salario1[i]
				k = 0
				semanal[k] = sueldo_semanal
				print("%s:\t%.2f\n" %(dia[i], salario1[i]))

		if(vendedor == 2):
			print("Trabajador 2\n")
			for i in range(0, 6):
				print("Dia %s\n" %dia[i])
				cantidad = int(input("Ingrese la cantidad vendida en el dia: "))
				if (cantidad <= 100):
					salario2[i] = 30 + (cantidad * 0.15)
				if (cantidad > 100 and cantidad < 999):
					salario2[i] = 50 + (cantidad * 0.15)
				if (cantidad >= 100):
					salario2[i] = 80 + (cantidad * 0.15)
				sueldo_semanal2 = sueldo_semanal2 + salario2[i]
				k = 1
				semanal[k] = sueldo_semanal2
				print("%s:\t%.2f\n" %(dia[i], salario2[i]))

		if(vendedor == 3):
			print("Trabajador 3\n")
			for i in range(0, 6):
				print("Dia %s\n" %dia[i])
				cantidad = int(input("Ingrese la cantidad vendida en el dia: "))
				if (cantidad <= 100):
					salario3[i] = 30 + (cantidad * 0.15)
				if (cantidad > 100 and cantidad < 999):
					salario3[i] = 50 + (cantidad * 0.15)
				if (cantidad >= 100):
					salario3[i] = 80 + (cantidad * 0.15)
				sueldo_semanal3 = sueldo_semanal3 + salario3[i]
				k = 2
				semanal[k] = sueldo_semanal3
				print("%s:\t%.2f\n" %(dia[i], salario3[i]))

		if(vendedor == 4):
			print("Trabajador 4\n")
			for i in range(0, 6):
				print("Dia %s\n" %dia[i])
				cantidad = int(input("Ingrese la cantidad vendida en el dia: "))
				if (cantidad <= 100):
					salario4[i] = 30 + (cantidad * 0.15)
				if (cantidad > 100 and cantidad < 999):
					salario4[i] = 50 + (cantidad * 0.15)
				if (cantidad >= 100):
					salario4[i] = 80 + (cantidad * 0.15)
				sueldo_semanal4 = sueldo_semanal4 + salario4[i]
				k = 3
				semanal[k] = sueldo_semanal4
				print("%s:\t%.2f\n" %(dia[i], salario4[i]))

		if(vendedor == 5):
			print("Trabajador 5\n")
			for i in range(0, 6):
				print("Dia %s\n" %dia[i])
				cantidad = int(input("Ingrese la cantidad vendida en el dia: "))
				if (cantidad <= 100):
					salario5[i] = 30 + (cantidad * 0.15)
				if (cantidad > 100 and cantidad < 999):
					salario5[i] = 50 + (cantidad * 0.15)
				if (cantidad >= 100):
					salario5[i] = 80 + (cantidad * 0.15)
				sueldo_semanal5 = sueldo_semanal5 + salario5[i]
				k = 4
				semanal[k] = sueldo_semanal5
				print("%s:\t%.2f\n" %(dia[i], salario5[i]))
		cont = cont + 1
	for i in range(0, len(semanal)):
		if(semana[i] > mayor):
			mayor = semanal[i]

	print("El mejor sueldo es el del trabajador %d" %i)


