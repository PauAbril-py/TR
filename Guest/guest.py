# TODO : link with admin.py

import platform
import os
import shutil

from datetime import datetime

import json

import dirs

# Database Imports
import mysql.connector as mysql
import sqlite3

###############
import random## 
###############

# Import Local Files
# from format_output import *
	
# from format_output_test import *
# from dirs import *

# dir_path = os.path.dirname(os.path.realpath(__file__))
# out_path = dir_path + '/out/'
# out_file_path = out_path + '/output.csv'
# err_file_path = out_path + '/error.txt'




# ─── MODULE DATA ────────────────────────────────────────────────────────────────

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

ordered_data = [
	data['Time'], 
	data['Node'], 
	data['Processor'], 
	data['Machine'], 
	data['Os'], 
	data['Total'], 
	data['Used'], 
	data['Free']
]

# ─── PRINT ──────────────────────────────────────────────────────────────────────

# TODO : turn into a function and return instead of print
def data_print():
	print('------------------------')

	print('Time:      ' + data['Time'])
	print('Node:      ' + data['Node'])
	print('Processor: ' + data['Processor'])
	print('Machine:   ' + data['Machine'])
	print('Os:        ' + data['Os'])
	
	print('\nDisk:')
	print('Total: ' + data['Total'])
	print('Used:  ' + data['Used'])
	print('Free:  ' + data['Free'])

	print('------------------------')

# for i in data:
# 	print(f"{i :<10} {data[i]}")

# ─── CSV ────────────────────────────────────────────────────────────────────────

def data_csv(): # TODO : csv function that returns the data in order to add it to admin's storage
	if os.path.isdir(dirs.out_path) != True:
		os.mkdir(dirs.out_path)
		pass
		
# '''
# 	if os.path.isfile(dirs.out_file_path) != True:
# 		print('a')
# 		try:
# 			format_output()
# 		except Exception as e:
# 			print(e)
# 			error = open(dirs.err_file_path, 'a')
# 			error.write('\n'+ str(datetime.now()) +' | '+ str(e))
# 	else:
# 		print('e')
# '''

	output = open(dirs.out_file_path, 'a')
	for i in data:
		output.write(f"{data[i]}, ")

	output.write('\n')


# ─── DB ─────────────────────────────────────────────────────────────────────────

# TODO : add google sheets database
class data_db:
	def __init__(self) -> None:
		print('Choose a database to use')

	def GoogleSheets():
		pass

	def MySQL(host, user, password, database):# TODO : verify credentials, and if it doesnt work, break and ask again
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
		
		connection = connect()
		cursor = connection.cursor()

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

	

data_db.MySQL('localhost', 'write_user', '0000', 'test1')
data_db.SQLite('C:\Code\TR\Guest\database.db')
data_csv()

# ────────────────────────────────────────────────────────────────────────────────


if __name__ == '__main__':
	pass
	
exit("\033[91mGuest program doesn't work yet\033[0m")
'''

if os.path.isdir(out_path) != True:
	os.mkdir(out_path)

if os.path.isfile(out_file_path) != True:
	print('a')
	try:
		format_output()
	except Exception as e:
		print(e)
		error = open(err_file_path, 'a')
		error.write('\n'+ str(datetime.now()) +' | '+ str(e))
else:
	print('e')

print(platform.system_alias(
	platform.system(),
	platform.release(),
	platform.version(),
))
print()
print(platform.uname())
print()
print(
	platform.node(),
	platform.processor(),
)

print(dir_path)

print(datetime.now())

total, used, free = shutil.disk_usage("/")

output = open(out_file_path, 'a')
output.write(str(datetime.now()) +', ')
output.write(platform.node() +', '+ platform.processor().replace(',', '') +', '+ platform.machine() +', '+ platform.system() +' '+ platform.release() +' '+ platform.version() +', ')
output.write(str(total // (2**30)) + ' GiB, '+ str(used // (2**30)) + ' GiB, '+ str(free // (2**30)) + ' GiB')
output.write('\n')


total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))
'''
