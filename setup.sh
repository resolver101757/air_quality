#!/bin/sh
# copy service file to service location 
# Found this instruction to setup systemd script and permisions here : https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/ 

cp -v -f air_particles.service /lib/systemd/system/
chmod +x  /home/pi/ak_air_quality_sensor/read_pressure.py
sudo chmod 644 /lib/systemd/system/air_particles.service
systemctl enable air_particles.service

