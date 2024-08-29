
i = 0

# while, revisa una condicion y hasta que esta sea falsa se va a repetir la parte interna de codigo
while i < 5:
    i += 1
    if i == 3:
        # continue es para terminal el ciclo en que se encuentra y saltarse al siguiente
        continue
    #print(i)
    if i >2:
        # break es para cerrar el loop apenas llegue a este
        break

usuarios = ['chancito feliz', 'felipe', 'roberto', 'nicolas']

#for loop es un ciclo que funciona con un iterador interno, en este caso llamado usuario y va a tomar el valor de usuarios hasta que se terminen
for usuario in usuarios:
    print(usuario)

usuario1 = 'Chanchito feliz'

#for c in usuario1:
    #print(c)


for usuario in usuarios:
    if usuario == 'roberto':
        continue
    #print(usuario)

# unas propiedades de range es que si ponemos mas de un numero, el primero sera donde comience el rango y el segundo donde terminara, y si se pone uno tercero sera el aumento que tenga entre uno y otro

for x in range(3, 30, 3):
    print(x)
else: #en los for loop el else se realiza cuando se acaba el for loop
    print('hemos terminado')


edades = [24, 25, 26, 35]

for usuario in usuarios:
    for edad in edades:
        print(usuario,edad)
