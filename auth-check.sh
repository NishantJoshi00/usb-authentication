#/bin/sh



if [[ $(python3 /root/USBAuth/checkScript.py $DEVPATH) -eq 0 ]]; then
	# echo This is executed 1>/dev/pts/2 ## DEBUG SIGNALS
	exit
fi

# echo This is exe 1>/dev/pts/2 ## DEBUG SIGNALS


if [[ $(echo $DEVPATH | su - {} -c 'read e;export DISPLAY=:0.0;zenity --question --text "Do you wish to connect $(cat /sys$e/product)?" --width 500;echo $?') -eq 0 ]]; then
	if [[ $(cat /root/USBAuth/password) == $(su - nishant -c "export DISPLAY=:0.0;zenity --password") ]]; then
		echo 1 > /sys$DEVPATH/authorized
		# su - nishant -c "export DISPLAY=:0.0;zenity --warning" ## DEBUG SIGNALS
	fi
fi
