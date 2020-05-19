#Tuplas
miTupla = ("Juan", 23, 12, 1992)
print(miTupla[:])
miLista = list (miTupla) #Convertir Tupla en lista
print(miLista[:])
miTupla2 = tuple(miLista) #Convertir lista en tupla
print(miTupla2[:])

print("Juan" in miTupla) #Elemento presente en Tupla?
print(miTupla.count(5)) #Cuantas veces aparece un elemento
print(len(miTupla)) #Cuantos elementos hay
name, day, month, year = miTupla #Desempaquetado de Tuplas
print(name)
print(day)
print(month)
print(year)