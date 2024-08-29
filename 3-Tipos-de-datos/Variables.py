#cadenas de texto se definen con comillas simples o dobles
texto = 'hola mundo'
texto2 = "Texto con comillas dobles"

# para definir los numeros solo se le asigna el numero a la variable y ya
entero = 20
decimal = 20.2
complejo = 1j

# print(texto, texto2, entero, decimal, complejo)

#listas, en otros lenguajes son conocidos como arreglos, son listas de datos en conjunto 
lista = [1, 2, 3]

#print(lista)

#copy copia la lista a otra variable
lista2 = lista.copy()
#print(lista2)

# clear borra todos los elementos de la lista 
lista.clear()
#print(lista)

# append metodo que agrega un elemento al final
lista.append(4)
#print(lista)


#count es para decir la cantidad que se repite un dato en la lista
#print(lista.count(4))

#len da el tamaño de la lista 
#print(len(lista2))


#para localizar un dato en una lista cada posicion tiene un valor comenzando desde el 0
#print(lista[0])

#pop elimina el ultimo elemento de la lista
lista.pop()
#print(lista)


lista.append('Hola Amigos')
lista.append('Peguelo')


# remove elimina el elemento que le pasemos por parametro
lista.remove('Peguelo')
#print(lista)


lista.append(1)
lista.append('Que mas')
lista.append(2)
#print(lista)


#reverse es para cambiar el orden de la lista
lista.reverse()
#print(lista)

#sort es para ordenar la lista pero tiene que ser de un solo tipo de datos
lista.remove('Hola Amigos')
lista.remove('Que mas')
lista.append(3)
lista.append(0)
lista.append(4)
#print(lista)
lista.sort()
#print(lista)


#tupla es un conjunto de datos al igua que la lista pero la principal diferencia es que no se puede modificar
tupla = ('hola', 'mundo', 'somos', 'tupla')
#print(tupla,tupla.count('hola'))

#print(tupla.index('mundo'))

#con list podemos pasar la tupla a tipo lista para poder modificar
listaDeTupla = list(tupla)
#print(listaDeTupla)

rango = range(6)
#print(rango)

#un diccionario es un conjunto de datos de diferente tipo que tienen un identificador de posicion o dato para poder manejarlo
diccionario = {
    'Nombre': 'Chanchito feliz',
    'Raza': 'Persa',
    'Edad' : 5
}

print(diccionario)
print(diccionario['Raza'])
print(diccionario.get('Nombre'))

diccionario['Nombre'] = 'Fluffy'

print(diccionario)
print(len(diccionario))

diccionario['ronronea'] = 'Si'

#print(diccionario)

#para eliminar un elemento del diccionario se utiliza pop para decir el elemento, popoitem para eliminar el ultimo y del para lo mismo que pop
 
#diccionario.pop('ronronea')
#diccionario.popitem()

#para copiar el diccionario a otra variable  se utiliza el metodo copy o tambien el metodo dict
copiaGatito = diccionario.copy()
del diccionario['ronronea']

#para limpiar un diccionario se utiliza clear
diccionario.clear()
#print(diccionario, copiaGatito)

#Diccionarios anidados

floffy = {
    'nombre': 'Floffy',
    'edad': 5
}

mamba = {
    'nombre': 'Black Mamba',
    'edad': 12
}
gatitos = {
    'Floffy': floffy ,
    'Mamba': mamba 
}

print(gatitos)

#construir un diccionario con el constructor dict

perritos = dict(nombre = 'Chanchito Feliz', edad = 6)
print(perritos)

verdadero = True
falso = False