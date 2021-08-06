# Json test 1

# import os

import json

from dirs import *

a = open(config_path)
config = json.load(a)


def format_output():
	output = open(out_path + '/output.csv', 'w')

	for i, j in config['Modules'].items():
		if j == True:
			output.write(i + ', ')
	#		print('a')
		elif j == False:
			output.write(', ')
	#		print('s')

	output.write('\n')

	output.close()
