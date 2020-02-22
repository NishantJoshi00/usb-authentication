#!/bin/bash
if [[ $(id -u) != 0 ]]; then
	echo "run as sudo"
	exit	
fi
export USER
echo $SUDO_USER
read psk
echo $psk > password
psk=$SUDO_USER
python3 rulesMaker.py $SUDO_USER
chown root:root password
chmod 400 password
chown root:root checkScript.py
chmod 500 checkScript.py
chown root:root auth-check.sh
chmod 500 auth-check.sh
mv ./01-usblockdown.rules /etc/udev/rules.d/
mkdir /root/USBAuth
mv ./password /root/USBAuth
mv ./checkScript.py /root/USBAuth
mv ./auth-check.sh /root/USBAuth
chattr -R +i /root/USBAuth
rm rulesMaker.py
rm establish.sh
