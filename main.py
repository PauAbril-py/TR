import platform
import os
import shutil

import json

from datetime import datetime

# Import Local Files
# from format_output import *
from format_output_test import *
from dirs import *

# dir_path = os.path.dirname(os.path.realpath(__file__))
# out_path = dir_path + '/out/'
# out_file_path = out_path + '/output.csv'
# err_file_path = out_path + '/error.txt'

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
