#Diccionario
miDiccionario = {"Clave":"Valor","Alemania":"Berlin", "Colombia": "Bogota", "Francia":"Paris","Reino Unido":"Londres"}
print(miDiccionario["Colombia"])
miDiccionario["Italia"] = "Lisboa"#Agregar elemento
print(miDiccionario)
miDiccionario["Italia"] = "Roma" #Modificar elemento
print(miDiccionario)
del miDiccionario["Reino Unido"]#Eliminar elemento
print(miDiccionario)
miTupla = ("España","Francia", "Reino Unido", "Alemania")
miDiccionario2 = {miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlin"}
print(miDiccionario2)
print(miDiccionario.keys()) #Imprimir claves
print(miDiccionario.values())#Imprimir valores
print(len(miDiccionario))