import pyodbc

# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.

class DbManage():

	server = '172.24.1.39'
	database = 'FACTURA'
	username = 'Data_Editor'
	password = 'jr03124300'

	def connect(self):
		cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';ENCRYPT=no;UID='+self.username+';PWD='+self.password)
		cursor = cnxn.cursor()
		return cursor

	def desconnect(self, cursor):
		cursor.close()

	# Tabla 'VFacturacion'
	def connect1(self, building):
		cursor = self.connect()
		cursor.execute("SELECT * FROM Vpfacturacion WHERE BLDGID = '%s'" % building)
		row = cursor.fetchall()
		self.desconnect(cursor)
		return row

	# Tabla 'VINCH'
	def connect2(self):
		cursor = self.connect()
		cursor.execute("SELECT * FROM VINCH")
		row = cursor.fetchall()
		self.desconnect(cursor)
		return row

