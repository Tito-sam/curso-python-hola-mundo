import pymysql.cursors


midb =  pymysql.connect(
	host= 'localhost',
	user = 'portron',
	password = 'titoypapi2004',
	database = 'prueba'
	)

cursor = midb.cursor()


# listar datos

#cursor.execute('select * from Usuario')

#resultado = cursor.fetchall()

#print(resultado)

# ver definiciones de tablas
# cursor.execute('show create table Usuario')


# insertar datos

# sql = 'insert into Usuario(email, username, edad) values(%s, %s, %s)'
# values = ('micorreo@correo.com','usuario',45)

# cursor.execute(sql, values)

# midb.commit()

#print(cursor.rowcount)


# actualizar datos 

#sql = 'update Usuario set email = %s where id = %s'
#values = ('micorrero@gmail.com',5)

#cursor.execute(sql,values)

#midb.commit()


# Eliminar datos

#sql = 'delete from Usuario where id = %s'
#values = (6, )

#cursor.execute(sql,values)

#midb.commit()

#limitar datos

cursor.execute('select * from Usuario limit 1')

resultado = cursor.fetchall()

print(resultado)