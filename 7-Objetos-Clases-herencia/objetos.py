
#para crear una clase toca poner class y luego poner el nombre de la clase, siempre la primera letra tiene que ser en mayuscula
class Usuario:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    #aqui adentro van a estar los metodos y los atributos, un metodo es una funcion propia de un objeto 
    #y un atributo es un dato propio de un objeto, pero se crea la estructura en la clase y ser le puede 
    #brindar un valor por defecto a los atributos 
    def saludo(self):
    	#EL self se puede cambiar por cualquier nombre mientras que se le de el mismo uso
    	print('Hola, mi nombre es', self.nombre, self.apellido)

class Admin(Usuario):
	def superSaludo(self):
		print('Hola, me llamo', self.nombre, 'y soy administrador')

usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('Chanchito', 'Feliz')

print(usuario.nombre, usuario.apellido)
print(usuario2.nombre, usuario2.apellido)

usuario2.saludo()

usuario.nombre = 'Chanchosqui'

usuario.saludo()

#del usuario.nombre
#del usuario
#print(usuario)

admin = Admin('Super','Feliz')
admin.saludo()
admin.superSaludo()

class Animal:
	def __init__ (self, nombre, onomatopeya):
		self.nombre = nombre
		self.onomatopeya = onomatopeya
	def saludo(self):
		print('Hola, soy un', self.tipo ,' y mi sonido es el', self.onomatopeya)

class Gato(Animal):
	tipo = 'Gato'
	def __init__(self, nombre, onomatopeya):
		Animal.__init__(self, nombre, onomatopeya)

gato1 = Gato('Fluffy', 'maullido')
gato1.saludo()

class Perro(Animal):
	tipo = 'Perro'
	def __init__(self, nombre, onomatopeya):
		super().__init__(nombre, onomatopeya)

perro = Perro('firulais', 'Ladrido')
perro.saludo()