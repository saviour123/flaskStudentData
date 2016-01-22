from flask import Flask, render_template, request
import sqlite3
import sqlite3 as sql

app = Flask(__name__)


#db configurations
conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# conn.close()

@app.route('/')
def home():
	return render_template('home.html')



@app.route('/addnew')
def addnew():
	return render_template('addnew.html')



@app.route('/addrec', methods=['POST','GET'])
def addrec():
	if request.method == 'POST':
		try:
			name = request.form['nm']
			addr = request.form['add']
			city = request.form['city']
			pin = request.form['pin']

			with sql.connect('database.db') as con:
				cur = con.cursor().execute('INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)',(name,addr,city,pin) )
				con.commit()
		except:
			con.rollback()
			msg = "error in insert operation"

		# finally:
		# 	return render_template('result.html', msg = msg)
		con.close()
	return render_template('result.html')



@app.route('/list')
def list():
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from students")

	rows = cur.fetchall()
	return render_template('list.html',rows=rows)

if __name__=='__main__':
	app.run(debug=True)