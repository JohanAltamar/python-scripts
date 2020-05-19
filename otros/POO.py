#POO
class Coche():
	#Propiedades comunes de objetos que pertenezcan a la clase
	#largoChasis = 250
	#anchoChasis = 120
	#ruedas = 4
	#enMarcha = False
	def __init__(self): #Constructor, especifica estado inicial de los objetos pertenecientes a la clase
		self.__largoChasis = 250
		self.__anchoChasis = 120
		self.__ruedas = 4 #Encapsulamiento de la propiedad. No se permite la modificacion desde fuera
		self.__enMarcha = False

	#Comportamientos de objetos pertenecientes a la clase
	#Métodos: funcion especial que pertenece a la clase
	def arrancar(self, arrancamos):
		self.__enMarcha = arrancamos

		if(self.__enMarcha):
			chequeo = self.__chequeo_interno()

		if (self.__enMarcha and chequeo):
			return "El coche está en marcha"
		elif (self.__enMarcha and chequeo == False):
			return "Algo ha ido mal en el chequeo, no podemos arrancar"
		else:
			return "El coche está parado"

	
	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Tiene un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
	
	def __chequeo_interno(self):#Encapsular metodo
		print("Realizando chequeo interno.")
		self.gasolina = "Ok"
		self.aceite = "Ok"
		self.puertas = "Cerradas"
		if(self.gasolina == "Ok" and self.aceite == "Ok" and self.puertas == "Cerradas"):
			return True
		else: 
			return False


miCoche = Coche() #Instanciar una clase. Crear objeto
print(miCoche.arrancar(True)) #miCoche.enMarcha = True
miCoche.estado()
print(miCoche.chequeo_interno())

print("--------------A continuacion creamos el segundo objeto")
miCoche2 = Coche()
print(miCoche2.arrancar(False))
#miCoche2.__ruedas = 3
miCoche2.estado()