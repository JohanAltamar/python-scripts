#Excepciones
def divide():
	try:
		op1 = float(input("Introduce el primer numero: "))
		op2 = float(input("Introduce el segundo numero: "))
		print("La división es: " + str(Op1/op2))
	
	except ValueError:
		print("El valor introducido es erroneo")
	except ZeroDivisionError:
		print("No se puede dividir entre 0!")
	except: #Encierra cualquier tipo de error
		print("Ha ocurrido un error")

	finally: #SIEMPRE SE EJECUTA LO QUE ESTA DENTRO
		print("Calculo finalizado")

divide()