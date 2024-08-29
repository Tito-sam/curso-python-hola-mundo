# if es un condicional
if 2 < 5:
    print('2 es menor que 5')

# a == b para revisar si es igual uno de otro
# a < b para mirar si a es menor que b
# a > b para revsar si a es mayor que b
# a != b para revisar si a es diferente de b
# <= b menor o igual
# >= b mayor o igual


#if 2 == 2:
#    print('2 es igual a 2')

#if 2 == 3:
#    print('2 es igual a 3')

#if 2 > 5:
#    print('2 es mayor que 5')

#if 5 > 2:
#    print('5 es mayor a 2')

#if 2 != 2:
#    print('2 es distinto a 2')

#if 3 != 2:
#    print('3 es diferente de 2')

#if 3 >= 2:
#    print('3 es mayor o igual a 2')

#if 3 <= 3:
#    print('3 es menor o igual a 3')

#siempre tenemos que identar para que funcione el codigo dentro del if

if 2 > 5:
    # la indentacion es ese espacio que hay entre el borde de la pagina y el codigo
    print('2 es mayor a 5 en if')
    #elif es para utilizar otro codigo con un comparador en el caso de que no se cumpla el primer if
elif 5 < 2:
    print('2 es menor a 5 en elif')
else:
    #else es una parte del codigo que solo funciona si todos los anteriores condicionales no funcionan y dan en false
    print('yo me imprimo en else solo si los anteriores condicionales son falsos')


#if de una sola linea

if 2 < 5: print('2 es menor a 5')

#if ternario
print('cuando devuelve true') if 5 > 2 else print('cuando devuelve false')

# and y or son comparadores que comparan dos condiciones y funcionan en el caso de and si ambos son verdaderos, y en el caso de or si alguno de las dos condiciones es true

if 2 < 5 and 3 > 2:
    print('ambas devuelven true')

if 2 > 5 and 3 > 2:
    print('hay una falsa y esto no se mostrara') 

if 2 > 5 or 3 > 2:
    print('hay una falsa pero tambien una verdadera entonces esto se muestra')

if 2 > 5 or 1 > 2:
    print('ambas son falsas y por esto no se mostrara')

