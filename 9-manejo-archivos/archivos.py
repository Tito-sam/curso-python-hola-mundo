"""c = open('chanchito.txt','w')

c.write('\nagregaremos una nueva linea a nuestro archivo')

c.close()

x = open('chanchito.txt')

print(x.read())"""

import os 

if os.path.exists('chanchito.txt'):
	os.remove('chanchito.txt')
else:
	print('El archivo no existe.')

os.rmdir('mi-carpeta')