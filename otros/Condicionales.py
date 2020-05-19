#Condicionales 
print("Programa de evaluación de notas de alumnos")

nota_alumno = input("Introduzca la nota del alumno")

def evaluacion (nota):
	valoracion = "Aprobado"
	if nota < 5:
		valoracion = "Reprobado"
	return valoracion

print(evaluacion(int(nota_alumno)))
