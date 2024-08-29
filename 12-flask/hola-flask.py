from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector

app = Flask(__name__)

midb = mysql.connector.connect(
	host = 'localhost',
	user = 'portron',
	password = 'titoypapi2004',
	database = 'prueba'
	)


cursor = midb.cursor(dictionary= True)

@app.route('/')
def index():
	return 'hola mundo'


# GET = llamar o listar, POST = Crear , PUT = actualizar, PATCH = actualizar , DELETE = Borrar
@app.route('/post/<post_id>', methods = ['GET', 'POST'])
def lala(post_id):
	if request.method == 'GET':
		return 'El id del post es: ' + post_id
	else:
		return 'Este es otro metodo y no get'	

@app.route('/lele', methods = ['POST','GET'])
def lele():
	cursor.execute('select * from Usuario')
	usuarios = cursor.fetchall()
	print(usuarios)
	#abort(401)
	#return redirect(url_for('lala', post_id = 2))
	#print(request.form)
	#print(request.form['llave1'])
	return render_template('lele.html', usuarios = usuarios)



@app.route('/home', methods = ['GET'])
def home():
	return render_template('home.html',mensaje = 'Hola mundo')



@app.route('/crear', methods = ['GET','POST'])
def crear():
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		edad = int(request.form['edad'])
		sql = 'insert into Usuario(email,username,edad) values( %s, %s, %s) '
		values = (email, username, edad)
		cursor.execute(sql, values)
		midb.commit()
		return redirect(url_for('lele'))
	return render_template('crear.html')