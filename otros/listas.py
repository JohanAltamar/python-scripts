mi_lista =["juan", "luz", "johan", "Francis"]
print(mi_lista[:])   #Para imprimir todos los elementos
print(mi_lista[3]) 	 #Para imprimir un elemento en 
                  	 #particular, siendo el primero 0
print(mi_lista[1:3]) #Para imprimir intervalos, omite
					 #el de la ultima posición
print(mi_lista[2:])  #Imprime desde el seleccionado
					 #hasta el final
mi_lista.append("Sandra") #Para agregar elemento al final
mi_lista.insert(2,"Sandra")#Para agregar en el indice 2
mi_lista.extend(["Jairo","Luis","Roy"])#Para agregar varios
print(mi_lista.index("luz"))#Para hallar indice del elemento
print("Axe" in mi_lista)#Para mostrar si el elemento pertenece a la lista
mi_lista.remove("luz")#Eliminar un elemento
mi_lista.pop()#Elimina ultimo elemento agregado
print(mi_lista[:])
#El operador + se usa para concatenar listas
#El operador * se usa como repetidor