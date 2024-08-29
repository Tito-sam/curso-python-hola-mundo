#dato = input('Ingrese dato: ')


#lista = ['hola mundo', 'chanchito feliz', 'dragones']

#if lista.count(dato) > 0:
#    print('El dato existe: ', dato)
#else:
#    print('El dato no existe: ', dato)


primero = input('Ingese el primer numero: ')

try:
    primero =int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('el primer dato no es un numero, por favor ingresa un numero.')
    exit()


segundo = input('Ingrese el segundo numero: ')

try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'


if segundo == 'chanchito feliz':
    print('ingresaste mal el segundo dato, prueba solo con numeros')
    exit()

print('suma = +\nresta = -\nmultiplicacion = *\ndivision = /')
simbolo = input('ingrese la operacion en signo: ')

if simbolo == '+' or simbolo == 'suma':
    c = primero + segundo
    print('La suma de los numeros es:',c)
elif simbolo == '-' or simbolo == 'resta':
    c = primero - segundo
    print('La resta de los numeros es:',c)
elif simbolo == '*' or simbolo == 'multiplicacion':
    c = primero * segundo
    print('La multiplicacion de los numeros es:',c)
elif simbolo == '/' or simbolo == 'division':
    c = primero / segundo
    print('La division de los numeros es:',c)
else:
    print('no es un signo de operacion u nombre de operacion')