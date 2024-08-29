# para definir una funcion se pone def el nombre de la funcion, unos parentesis y dos puntos 
def miFuncion():
    # todo lo que se escriba sobre la funcion tiene que ir identado(con el espacio que aparece al inicio) 
    print('Mi primera funcion')

#para llamar una funcion se pone el nombre de la funcion y unos parentesis 
miFuncion()

# en este caso dentro de los parentesis hay algo llamado argumentos, estos son variables que la funcion esta esperando que le den al momento de ser llamado y con las cuales podra poner a funcionar el codigo de adentro
def imprimeDato(nombre, apellido ):

    print('El nombre completo es: ', nombre, apellido)

# en este caso se le esta pasando un parametro al momento de llamarla , se le llama asi al dato que se le esta dando al llamarla.
imprimeDato('Chanchito','feliz')


#al ponerle un asterisco antes de los argumentos se quiere decir que va a recibir todos los parametros que le inglesen en una lista
def imprimedato2(*nombres) :
    for nombre in nombres:
        print('El nombre del usuario es: ' , nombre)


imprimedato2('chanchito', 'feliz', 'lala', 'lele')


def nombreCompleto(apellido, nombre) :
    print(nombre,apellido)

#si se pasa el parametro con el nombre exacto como si se asignara no importa el orden del ingreso de datos ya que se le asigna directamente.
nombreCompleto(nombre = 'chanchito', apellido = 'feliz')


#poner dos asteriscos hace que el argumento se vuelva un diccionario
def nombre(**kwargs) :
    print(kwargs['nombre'], kwargs['apellido'])

#para poder pasarle datos tenemos que ponerle el nombre de la llave y el valor
nombre(nombre='Chanchito',apellido='Feliz')


#para darle un valor por defecto a un argumento se le asigna un valor y en caso de que no le pases ese parametro que dara con ese valor
def mifuncion2(argumento = 'Chachito'):
    print(argumento)

mifuncion2()

mifuncion2('batman')

def mifuncionlista(lista):
    for elemento in lista:
        print(elemento)

#a las fucniones se les pueden pasar casi todo tipos de datos
mifuncionlista(['chanchito','feliz'])


def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

saludo = concatenaNombres(['Tito', 'Mendez'])

print(saludo)


#recursividad, es usar una funcion en ella misma

def recursion(i):
    if (i < 1):
        return i
    else:
        print(i)
        recursion(i - 1)

recursion(6)