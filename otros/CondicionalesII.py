#Condicionales II
print("Control de ingresos para mayores de edad")

edad_persona = int(input("Ingrese edad del usuario: "))

if edad_persona < 18:
	print("No puede pasar")
elif edad_persona > 100:
	print("Edad incorrecta")
else: 
	print("Puede pasar")

print("El programa ha finalizado.")