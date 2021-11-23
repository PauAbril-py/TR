import platform
import os
import shutil

import json

from datetime import datetime

def local():
	print('Local Machine:----------')

	total, used, free = shutil.disk_usage("/")

	print('Time:      ' + str(datetime.now()))
	print('Node:      ' + platform.node())
	print('Processor: ' + platform.processor().replace(',', ''))
	print('Machine:   ' + platform.machine())
	print('Os:        ' + platform.system() +' '+ platform.release() +' '+ platform.version())
	
	print('\nDisk:')
	print('Total: ' + str(total // (2**30)) + ' GiB')
	print('Used:  ' + str(used // (2**30)) + ' GiB')
	print('Free:  ' + str(free // (2**30)) + ' GiB')

	print('------------------------')


if __name__ == '__main__':
	print('\033[93mThis is a function, please use admin.py\033[0m')


import mysql.connector as mysql
import sqlite3

###############
import random## 
###############

total, used, free = shutil.disk_usage("/")

data = {
	'Time' : str(datetime.now()),
	'Node' : platform.node(),
	'Processor' : platform.processor().replace(',', ''),
	'Machine' : platform.machine(),
	'Os' : platform.system() +' '+ platform.release() +' '+ platform.version(),

	'Total' : str(total // (2**30)) + ' GiB',
	'Used' : str(used // (2**30)) + ' GiB',
	'Free' : str(free // (2**30)) + ' GiB',
}


class data_db:
	def __init__(self) -> None:
		print('Choose a database to use')

	def GoogleSheets():
		pass

	def MySQL(host, user, password, database):
		def connect():
			mydb = None
			try:
				mydb = mysql.connect(
					host = host,
					user = user,
					password = password,
					# database = "TR" # TODO : create the database and table on the admin side if it does not exist.
				)
				print(f'\033[92mConnection to MySQL DB at "{host}" successful\033[0m')
			except Exception as e:
				print(f'\033[91mThe error "{e}" ocurred\033[0m')
			return mydb
		try:
			connection = connect()
			cursor = connection.cursor()
		except Exception as e:
			return e

	  ###############################################################################################################
		def create_database():
			cursor.execute(f"CREATE DATABASE {database}")
		try:
			create_database()
		except:
			pass


		mydb = mysql.connect(host = host, user = user, password = password, database = database)
		connection = mydb
		cursor = mydb.cursor()
	  ###############################################################################################################
		def create_table():
			cursor.execute("CREATE TABLE Computers(id integer PRIMARY KEY, time text, node text, processor text, machine text, os text, Total text, Used text, Free text)")

		try:
			create_table()
		except:
			pass
	  ###############################################################################################################

		def insert_table():
			cursor.execute(
				f"""
				INSERT INTO Computers VALUES(
					{random.randint(2,102)},
					"{data["Time"]}",
					"{data["Node"]}",
					"{data["Processor"]}",
					"{data["Machine"]}",
					"{data["Os"]}",
					"{data["Total"]}",
					"{data["Used"]}",
					"{data["Free"]}"
				)
				"""
			)
			connection.commit()
		try:
			insert_table()
		except Exception as e:
			print(e)

	def SQLite(path): # NOTE: SQLite wont work properly for remote and multiple access
		def connect():
			# print(path)
			connection = None
			try:
				connection = sqlite3.connect(path)
				print(f'\033[92mConnection to SQLite DB at "{path}" successful\033[0m')
			except sqlite3.Error as e:
				print(f'\033[91mThe error "{e}" ocurred\033[0m')
			return connection
		
		connection = connect()
		cursor = connection.cursor()

		def create_table():
			cursor.execute("CREATE TABLE Computers(id integer PRIMARY KEY, time text, node text, processor text, machine text, os text, Total text, Used text, Free text)")
			connection.commit()

		try:
			create_table()
		except:
			pass

		def insert_table():
			cursor.execute( # TODO : ID from settings.cfg, not random number
				f'''
				INSERT INTO Computers VALUES(
					{random.randint(2,102)},
					'{data['Time']}',
					'{data['Node']}',
					'{data['Processor']}',
					'{data['Machine']}',
					'{data['Os']}',
					'{data['Total']}',
					'{data['Used']}',
					'{data['Free']}'
				)
				'''
			)
			connection.commit()
		try:
			insert_table()
		except Exception as e:
			print(e)
