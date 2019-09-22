# MonoDAQ-U-X
This repository is made for MonoDAQ-U-X related codes and testing. Mainly for my hobby use, but everyone is welcome to share, use and participate :)

## How to use MonoDAQ-U-X with raspberry pi
MonoDAQ-U-X suits well for remote logging applications and Raspberry pi makes great companion for that.

For Raspberry Pi logging you have to install [Isotel DAQ and Metering (IDM)](https://www.isotel.eu/idm/rpi.html "Setting up Isotel IDM on Raspberry PI")

Here quick IDM installation guide without monitor.
1. Log to your Raspberry Pi with SSH
1. Update and upgrade your Raspberry Pi
```
sudo apt-get update
sudo apt-get -y dist-upgrade  
```
1. Install oracle java 1.8 for IDM
```
sudo apt-get install oracle-java8-jdk
```
1. Download IDM package
```
wget https://www.isotel.eu/download/idm-1.1b5.jar
```
1. Give access for default user to plug-and-play USB devices. Create `sudo nano /etc/udev/rules.d/99-myusb.rules` and add there
```
SUBSYSTEMS=="usb", ATTRS{idVendor}=="5726", ATTRS{idProduct}=="1500", GROUP="users", MODE="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="5726", ATTRS{idProduct}=="1502", GROUP="users", MODE="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="1ced", ATTRS{idProduct}=="8000", GROUP="users", MODE="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="1ced", ATTRS{idProduct}=="8001", GROUP="users", MODE="0666"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="1ced", ATTRS{idProduct}=="8002", GROUP="users", MODE="0666"
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666"
```
1. Go to `cd /etc/udev/rules.d/`
1. Run `sudo udevadm control --reload-rules`
1. And run `udevadm trigger`
1. Install python packages
```
pip3 install isotel-idm
```
There is also bluethooth modules available for IDM and you can check how to install them from [here](https://www.isotel.eu/idm/rpi.html "Setting up Isotel IDM on Raspberry PI")

1. Finally start IDM service ```java -jar idm-1.1b5.jar --daemon```
