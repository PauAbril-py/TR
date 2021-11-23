# -*- coding: utf-8 -*-
import PySimpleGUIQt as sg

import sys

import json

import dirs
from lib import LocalGuest

# ─── CONFIG ─────────────────────────────────────────────────────────────────────

config = json.load(open(dirs.config_path))

icon = b'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAQAAAD9CzEMAAAAaklEQVRYw+2X4QlAIQgGv/Haf4QaxAaIeCoZ9Ljrr3GYVigBnKVpyDZrqIXjFvp2m8nUw3EL9rGicQgQ/FlQftHST0U6dS8IjgnKi5xuU+/G9FF6U6fbHhaUF7m8TfkyESC4MICUj1AAGSZrLe0urAS6dAAAAABJRU5ErkJggg=='

# ─── MySQL
host, user, password, database = config['MySQL_Credentials']['host'], config['MySQL_Credentials']['user'], config['MySQL_Credentials']['password'], config['MySQL_Credentials']['database']

# sg.theme('systemdefault1')
# sg.theme('darkpurple5')
# sg.theme('LightBrown9')
# sg.theme('Topanga')

# ─── SETTINGS ───────────────────────────────────────────────────────────────────

def save_settings():
	for i in config['Modules']:
		config['Modules'][i] = values[i]
	json.dump(config, open(dirs.config_path, 'w'), indent='\t', sort_keys=True)
	print('Settings saved')

def revert_settings():
	for i in config['Modules']:
		window[i].update(value=config['Modules'][i])
	print('Settings reverted')

def OutputSettings():
	window.Disable()
	window.DisableClose = True
	Odatabases = [
		[sg.Checkbox('Google Sheets')],
		[sg.Checkbox('SQLite')],
		[sg.Checkbox('MySQL')],
	]
	Olayout = [
		[sg.Text(size=(35,0))],
		[sg.Checkbox('Print')],
		[sg.Checkbox('Csv')],
		[sg.Checkbox('DataBase')],
		[sg.VerticalSeparator(), sg.Column(Odatabases), sg.Stretch()],
		[
			sg.Stretch(),
			sg.Button(' Revert settings ', tooltip='Reverts settings to saved position', key='OUTPUT_REVERT_SETTINGS'), 
			sg.Button(' Save ', tooltip='Saves the settings', key='OUTPUT_SAVE_SETTINGS'),
			# sg.Button(' Exit ', key='OUTPUT_EXIT'),
		],
	]

	Owindow = sg.Window('Output Settings', layout=Olayout, icon=icon, resizable=False)

	while True:
		Oevent, Ovalues = Owindow.read()

		if Oevent == sg.WIN_CLOSED:
			break
		
	window.Enable()
	window.DisableClose = False
	Owindow.close()

def MySQL_CredentialsInput():
	global host, user, password, database # FIXME : not saved unless you open the settings and hit save
	cfg = config['MySQL_Credentials']

	window.Disable()
	window.DisableClose = True
	MySQLCI_layout = [
		[sg.Text('host', size=(8,1)), sg.InputText(key='host', default_text=cfg['host'])],
		[sg.Text('user', size=(8,1)), sg.InputText(key='user', default_text=cfg['user'])],
		[sg.Text('password', size=(8,1)), sg.InputText(key='password', default_text=cfg['password'], password_char='*')],
		[sg.Text('database', size=(8,1)), sg.InputText(key='database', default_text=cfg['database'])],
		[
			sg.Checkbox('Save localy', key='MySQLCI_SAVE_LOCAL', default=cfg['savelocaly']),
			sg.Stretch(),
			sg.Button(' Clear settings ', tooltip='Clears settings', key='MySQLCI_CLEAR_SETTINGS'), 
			sg.Button(' Save ', tooltip='Saves the settings and exits the window', key='MySQLCI_SAVE_SETTINGS'),
			# sg.Button(' Exit ', key='OUTPUT_EXIT'),
		],
	]

	MySQLCI_window = sg.Window('MySQL Credentials Input', layout=MySQLCI_layout, icon=icon, resizable=False)


	while True:
		MySQLCI_event, MySQLCI_values = MySQLCI_window.read()

		if MySQLCI_event == sg.WIN_CLOSED:
			break

		if MySQLCI_event == 'MySQLCI_SAVE_SETTINGS':
			# print(MySQLCI_values)
			host = MySQLCI_values['host']
			user = MySQLCI_values['user']
			password = MySQLCI_values['password']
			database = MySQLCI_values['database']

			if MySQLCI_values['MySQLCI_SAVE_LOCAL'] == True:
				cfg['host'] = host
				cfg['user'] = user
				cfg['password'] = password
				cfg['database'] = database
				cfg['savelocaly'] = True
				json.dump(config, open(dirs.config_path, 'w'), indent='\t', sort_keys=True)
			elif MySQLCI_values['MySQLCI_SAVE_LOCAL'] == False:
				cfg['host'] = ''
				cfg['user'] = ''
				cfg['password'] = ''
				cfg['database'] = ''
				cfg['savelocaly'] = False
				json.dump(config, open(dirs.config_path, 'w'), indent='\t', sort_keys=True)
			break
		
		elif MySQLCI_event == 'MySQLCI_CLEAR_SETTINGS':
			cfg['host'] = host = MySQLCI_values['host'] = ''
			cfg['user'] = user = MySQLCI_values['user'] = ''
			cfg['password'] = password = MySQLCI_values['password'] = ''
			cfg['database'] = database = MySQLCI_values['database'] = ''
			cfg['savelocaly'] = False
			for i in ['host', 'user', 'password', 'database']:
				MySQLCI_window.FindElement(i).Update('')

			MySQLCI_window['MySQLCI_SAVE_LOCAL'].Update(value=False)
			
			json.dump(config, open(dirs.config_path, 'w'), indent='\t', sort_keys=True)

	window.Enable()
	window.DisableClose = False
	MySQLCI_window.close()

# ─── MAIN ───────────────────────────────────────────────────────────────────────

def start():
	print('# TODO : send signal to guest PCs to execute the program and return the results')
	pass# TODO : send signal to guest PCs to execute the program and return the results

# ─── GUI ────────────────────────────────────────────────────────────────────────

def gui():
  # ─── LAYOUTS ────────────────────────────────────────────────────────────────────

	col1 = [
		[sg.Button('Start')],
		[
			sg.Button('Local', tooltip='Executes the program on the local machine'),
			sg.Button('Output', tooltip='Opens the output settings')
		],
		[sg.Button('MySQL Credentials')],
		[sg.Text(size=(20,0))],
	]

	col2 = [
		[sg.Checkbox('time', default=config['Modules']['time'], key='time')],
		[sg.Checkbox('node', default=config['Modules']['node'], key='node')],
		[sg.Checkbox('processor', default=config['Modules']['processor'], key='processor')],
		[sg.Checkbox('machine', default=config['Modules']['machine'], key='machine')],
		[sg.Checkbox('os', default=config['Modules']['os'], key='os')],
		[sg.Text('Disk:')], # ---- DISK ----------------------------------------
		[
			sg.Checkbox('Total', default=config['Modules']['Total'], key='Total'),
			sg.Checkbox('Used', default=config['Modules']['Used'], key='Used'),
			sg.Checkbox('Free', default=config['Modules']['Free'], key='Free')
		],
		# TODO : choose output methods [csv, db, print]
		# [sg.HorizontalSeparator()],
		# [
		# 	sg.Checkbox('Print'),
		# 	sg.Checkbox('Csv'),
		# 	sg.Combo(['No database', 'Google Drive', 'MySQL']),
		# ],
		[
			sg.Stretch(), 
			sg.Button(' Revert settings ', tooltip='Reverts settings to saved position', key='REVERT_SETTINGS'), 
			sg.Button(' Save ', tooltip='Saves the settings', key='SAVE_SETTINGS')
		],
	]

	col2_1 = [
		[sg.Column(col1)],
		[sg.HorizontalSeparator()],
		[sg.Column(col2, element_justification='')]
	]

	col3 = [
		[sg.Output(size=(65,18), font=('Consolas', 11), key='OUTPUT')],
		[sg.Button('Clear',tooltip='Clears the output' , key='CLEAR_OUTPUT')]
	]

	layout_main = [
		[sg.Text('Admin Tools')],
		[sg.Column(col2_1), sg.Column(col3, key='OUTPUT_COL')]
	]

  # ─── OPEN WINDOW ────────────────────────────────────────────────────────────────

	global window
	window = sg.Window('TR Admin', layout_main, icon=icon, resizable=False, disable_close=False)

	while True:
		global values
		event, values = window.read(timeout=500)

		if event == sg.WIN_CLOSED or event == 'Exit':
			break
		
		if event == 'SAVE_SETTINGS':
			save_settings()
		elif event == 'REVERT_SETTINGS':
			revert_settings()

		elif event == 'CLEAR_OUTPUT':
			window.FindElement('OUTPUT').Update('')
		
		elif event == 'Start':
			start()
		elif event == 'Local':
			LocalGuest.local()
			LocalGuest.data_db.MySQL(host, user, password, database)
				
		elif event == 'Output':
			OutputSettings()
		elif event == 'MySQL Credentials':
			MySQL_CredentialsInput()



	window.close()


if __name__ == '__main__':
	gui()

# use commandline arguments to run the program on the local machine


# for python >= v3.10

if sys.version_info >= (3, 10):'''
	match len(sys.argv):
		case 1: # one argument
			if sys.argv[1] in ('-l', '--local'):
				LocalGuest.local()
				LocalGuest.data_db.MySQL(host, user, password, database)
		case _:
			gui()
	'''
else:
	# for python < v3.10
	if len(sys.argv) > 1:
		if '-g' in sys.argv or '--gui' in sys.argv:
			gui()

		elif '-r' in sys.argv or '--run' in sys.argv:
			start()

		elif '-l' in sys.argv or '--local' in sys.argv:
			LocalGuest.local()
			LocalGuest.data_db.MySQL(host, user, password, database)
		
		elif '-c' in sys.argv or '--config' in sys.argv: # FIXME
			setting = sys.argv[sys.argv.index('-c') + 1]

			try:
				if setting.lower() == 'host':
					host = sys.argv[sys.argv.index('host') + 1]
					config['MySQL_Credentials']['host'] = host
				if setting.lower() == 'user':
					user = sys.argv[sys.argv.index('user') + 1]
					config['MySQL_Credentials']['user'] = user
				if setting.lower() == 'password':
					password = sys.argv[sys.argv.index('password') + 1]
					config['MySQL_Credentials']['password'] = password
				if setting.lower() == 'database':
					database = sys.argv[sys.argv.index('database') + 1]
					config['MySQL_Credentials']['database'] = database
			except Exception as e:
				print(f'Invalid setting "{e}"')
			
			json.dump(config, open(dirs.config_path, 'w'), indent='\t', sort_keys=True)


		elif '-h' in sys.argv or '--help' in sys.argv:
			print('Usage: python3 admin.py [OPTION]')
			print('')
			print('Options:')
			print('	-g, --gui				Opens the GUI for the program')
			print('	-r, --run				Runs the program')
			print('	-l, --local				runs the program on the local machine')
			print('	-s <setting> <value>, --settings <setting> <value>			')
			print('		--host				')
			print('		--user				')
			print('		--password			')
			print('		--database			')
			print('	-h, --help				Display this help message')


			print('')
			print('Example:')
			print('	python3 admin.py -g')
			print('	python3 admin.py --gui')
			print('	python3 admin.py -r')
			print('	python3 admin.py --run')
			print('	python3 admin.py -l')
			print('	python3 admin.py --local')
			print('	python3 admin.py -s --host=localhost --user=root --password=password --database=database')
			print('	python3 admin.py --settings --host=localhost --user=root --password=password --database=database')
			print('')
			print('	python3 admin.py -h')
			print('	python3 admin.py --help')
			print('')
			print('	python3 admin.py -s --host=localhost --user=root --password=password --database=database')



			print('-h or --help : prints this help menu')
			print('-r or --run : runs the program')
			print('-l or --local : runs the program on the local machine')
			print('-s or --settings : sets a new setting for the program')
			print('-s <setting> or --settings <setting> : sets a new setting for the program')
			print('-s <setting> <value> or --settings <setting> <value> : sets a new setting for the program')
			print('-g or --gui : opens the gui')
			print('Usage: python3 admin.py [OPTION]\n\nOptions:\n\t-l, --local\t\t\t\tRun the program on the local machine\n\t-h, --help\t\t\t\tDisplay this help message')
		else:
			# args = ' '.join(sys.argv[1:])
			args = sys.argv[1:]
			print(f'\033[91mThe arguments "{args}" are erroneous\033[0m')
			
	else:
		gui()
