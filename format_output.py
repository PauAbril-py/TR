import os

import json

from dirs import *


def format_output():

	output = open(out_path + '/output.csv', 'w')
	output.write('time, ')
	output.write('node, processor, machine, os, Total, Used, Free')
	output.write('\n')

	output.close()