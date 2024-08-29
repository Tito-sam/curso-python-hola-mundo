# multiplicar un numero sin el signo de multiplicacion
"""
multiplo = int(input('Digite el primer numero.\n:'))
multiplicador = int(input('Digite el segundo numero.\n:'))
multiplicacion = 0
for x in range(multiplicador):
	multiplicacion += multiplo

print('El producto es:',multiplicacion)


# ingresar un nombre y apellido e imprimirlo al reves

nombre = input('Digite su nombre: ')
apellido = input('Digite su apellido: ')

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])


# escribir una funcion que encuentre el numero menor de una lista

lista = [4,4,5,7,2,356,6786,34,3.9,1,-34,42,0.43,44,-65,0.1,5654]
num_menor = lista[0]

for x in lista:
	if num_menor > x:
		num_menor = x

print(num_menor)

"""


# hacer una funcion que devuelva el volumen de una esfera a traves de su radio

#r = float(input('Digite el radio de la esfera: '))

def volumenEsfera(r: float) -> float:
	volumen = (4 / 3) * 3.1416 * r**3
	return volumen
#print(volumenEsfera(r))


#escribir una funcion preguntando si una persona es mayor de edad

#edad = int(input('Digite su edad: '))

def mayorEdad(edad: int):
	if edad > 17:
		print('Eres mayor de edad.')
	else:
		print('Eres menor de edad.')

#mayorEdad(edad)


# escriba una funcion que diga si un numero es par o impar

#numero = int(input('Digite un numero: '))

def parOImpar(num):
	if num % 2 == 0:
		print('El numero', num, ' es par.')
	else:
		print('El numero', num, ' es impar.')

#parOImpar(numero)


# Escribir una funcion que indique cuantas vocales hay en una palabra

#palabra = input('Digite una palabra: ')

def vocales(p):
	vocal = 0
	for l in p:
		if l == 'a' or l == 'A' or l == 'á' or l == 'Á':
			vocal += 1
		elif l == 'e' or l == 'E' or l == 'é' or l == 'É':
			vocal += 1
		elif l == 'i' or l == 'I' or l == 'í' or l == 'Í':
			vocal += 1
		elif l == 'o' or l == 'O' or l == 'ó' or l == 'Ó':
			vocal += 1
		elif l == 'u' or l == 'U' or l == 'ú' or l == 'Ú':
			vocal += 1
	print(vocal)

#vocales(palabra)


# escribir una aplicacion que reciba numeros infinitos hasta que
#se escriba basta, luego se sumen todos los numeros ingresados

"""
numero = 0
suma = 0
basta = False
while basta == False:
	numero = input('Digite numeros hasta poner basta: ')
	if numero == 'basta' or numero == 'Basta':
		basta = True
	else:
		try:
			num = int(numero)
			suma += num
		except:
			print('El dato no es un numero, si quiere salir escriba basta.')

print('La suma de los numeros es:',suma)
"""


#escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo

def escribirNombres():
	archivo = open('nombres.txt','a')
	detener = False
	
	while detener == False:
		nombre = input('Digite el nombre: ')
		apellido = input('Digite el apellido: ')
		detenido = input('Quiere detenerse, si o no: ')
		archivo.write(nombre + ' '+ apellido + '\n')
		if detenido == 'si':
			detener = True

escribirNombres()
archivo2 = open('nombres.txt')
print(archivo2.read())

