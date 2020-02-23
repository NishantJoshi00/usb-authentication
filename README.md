# USB Protection System for Linux (Ubuntu)
This is a simple system tweak to disallow any usb device that is to be connected to the Linux Box

# Warning
- While installing the script please take the precautions the the script is configured correctly
- It ignored, there is a little chance that the rules misbehieve cutting the user off entirly from accessing the system
- It is farely safe to use on laptops, as the keyboard is not connected to the USB bus, improving the chances of fixing the problem
- Where the problems could occour
     - If facing difficulty connecting any devices after configuring the script, check the `/etc/udev/rules.d/01-usblockdown.rules` file, that the rule for accessing the `/root/USBAuth/auth-check.sh` is present
     - Python3 must be present in your linux box, for this system to work
     - If encountered problem even after entering the password, please check the `/root/USBAuth` folder and the password, file to get the password root privilages are required.

# How it works
It adds a rules to the udev rulebook to disallow allow the usb devices present, then only allow the once that are really required to by your Computer


# How to install
The installation procedure is very simple.
```bash
# Please do not run this script as root
# This script is required to be run as sudo
$ sudo bash establish.sh
```


# How to uninstall safely
The following commands must be executed as root
```bash
rm /etc/udev/rules.d/01-usblockdown.rules
chattr -i -R /root/USBAuth
rm -rf /root/USBAuth
```


# Contributions
- The only operating system that this script is tested on is **ubuntu:19.10**
- I don't have any idea about the compatibility of the script with other Linux based OS
- The parts of the scripts that are written in python could very well be implemented in bash, but I lack the necessary knowledge to do so.
- This project is very risky to implement on a linux PC, as most of the components are connected by USB, my goal is to make this project risk free and easy to install on all the Linux based platforms
- To improve the protection even more the scripts could be transcribed into ELF's which are written is a secure language to improve the security even move
- The method of storing password could be enhanced by implementing hashing algorithm