from modulos import saludo 
from camelcase import CamelCase

saludo('Tito')

c = CamelCase()

s = 'esta oracion necesita camelcase'

print(c.hump(s))

