#!/bin/sh
# copy service file to service location 
# Found this instruction to setup systemd script and permisions here : https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/ 

#Air particles  
cp -v -f air_particles.service /lib/systemd/system/
chmod +x  /home/pi/air_quality/particles.py
sudo chmod 644 /lib/systemd/system/particles.service
systemctl enable air_particles.service

# Air quality (GAS)
cp -v -f air_quality.service /lib/systemd/system/
chmod +x  /home/pi/air_quality/air_quality.py
sudo chmod 644 /lib/systemd/system/air_quality.service
systemctl enable air_quality.service