class Persona():
	def __init__(self,nombre,apellido,edad):
		self.nombre=nombre
		self.apellido=apellido
		self.edad=edad
	#
	def imprimir(self):
		print ("nombre: "+self.nombre)
		print ("apellido: "+self.apellido)
		print ("edad: "+str(self.edad))
	#
	def control_edad(self):
		if self.edad < 18:
			print ("la persona tiene menos de 18")
		else:
			print ("la persona tiene 18 o mas")
#
class Estudiante(Persona):
	def __init__(self,nombre,apellido,edad,escuela,media_nota):
		super().__init__(nombre,apellido,edad)
		self.escuela=escuela
		self.media_nota=media_nota
	#
	def imprimir_estudiante(self):
		super().imprimir()
		print ("escuela: "+self.escuela)
		print ("media nota:"+str(self.media_nota))
#
# Main
#
# Parte 1
#persona1=Persona("Juan","Martinez",15)
#print (persona1.nombre)
#print (persona1.apellido)
#print (persona1.edad)
#
# Parte 2
#persona1=Persona("Juan","Martinez",25)
#persona1.imprimir()
#persona1.control_edad()
#
# Parte 3
#estudiante1=Estudiante("Juan","Martinez",25,"madrid",30)
#estudiante1.imprimir_estudiante()
#estudiante1.control_edad()
#
# Parte 4
lista_estudiantes=[]
numero_estudiantes=int(input("Ingresa el numero de estudiantes: "))
for i in range(numero_estudiantes):
	nombre=input("nombre: ")
	apellido=input("apellido: ")
	edad=int(input("edad: "))
	escuela=input("escuela: ")
	media_nota=int(input("media nota: "))
	estudiante=Estudiante(nombre,apellido,edad,escuela,media_nota)
	lista_estudiantes.append(estudiante)
for estudiante in lista_estudiantes:
	if (estudiante.edad > 18) and (estudiante.media_nota > 28):
		print ("-------")
		estudiante.imprimir_estudiante()
