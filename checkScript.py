import sys
import os
path = "/sys{}".format(sys.argv[1])
# os.system("echo {} 1>/dev/pts/2".format(path)) ## DEBUG SIGNALS
if "authorized" in os.listdir(path):
	# os.system("echo gone into if 1>/dev/pts/2") ## DEBUG SIGNALS
	with open("{}/authorized".format(path)) as f:
		d = int(f.read())
	if d == 0:
		# os.system("echo gone into ifif 1>/dev/pts/2") ## DEBUG SIGNALS
		print(1)
		exit()
	else:
		# os.system("echo gone into ifelse 1>/dev/pts/2") ## DEBUG SIGNALS
		print(0)
		exit()
else:
	# os.system("echo gone into else 1>/dev/pts/2") ## DEBUG SIGNALS
	print(0)
	exit()
