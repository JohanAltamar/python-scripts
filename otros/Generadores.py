#Generadores

def generaPares(limite):
	num = 1
	while num < limite:
		yield num*2
		num += 1
	
numerosPares = generaPares(10)

print(next(numerosPares))
print("Aqui puede ir mas codigo")

print(next(numerosPares))
print("Aqui puede ir mas codigo")

print(next(numerosPares))
print("Aqui puede ir mas codigo")
