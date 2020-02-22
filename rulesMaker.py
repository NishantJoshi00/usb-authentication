import os

import sys
with open("auth-check.sh") as f:
	a = f.read().format(sys.argv[1])
with open("auth-check.sh", "w") as f:
	f.write(a)


with os.popen("lsusb | awk '{ print $6 }'") as f:
	data = f.readlines()

# Default Authorization
line1 = "ACTION==\"add\", SUBSYSTEMS==\"usb\", RUN+=\"/bin/sh -c 'for h in /sys/bus/usb/devices/usb*; do echo 0 > $h/authorized_default; done'\"\n"
line2 = "ACTION==\"add\", ATTR{bDeviceClass}==\"09\", RUN+=\"/bin/sh -c 'echo 1 > /sys$DEVPATH/authorized'\"\n"

multi = "ACTION==\"add\" ATTR{idVendor}==\"%s\", ATTR{idProduct}==\"%s\" RUN+=\"/bin/sh -c 'echo 1 > /sys$DEVPATH/authorized'\"\n"

authline = "ACTION==\"add\", SUBSYSTEMS==\"usb\", RUN+=\"/bin/sh -c 'bash /root/USBAuth/auth-check.sh'\"\n"

print(line1)
print(line2)
for i in data:
	print(multi % tuple(i.split(":")))
print(authline)

with open("01-usblockdown.rules", "w") as f:
	f.write(line1)
	f.write(line2)
	for i in data:
		f.write(multi % (i.split(":")[0].strip(), i.split(":")[1].strip()))
	f.write(authline)
	
