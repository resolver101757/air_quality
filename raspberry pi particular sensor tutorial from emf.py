#useful website from #https://cayenne.mydevices.com/
# http://wiki.dragino.com/index.php?title=Lora_Shield

from plantower import Plantower # plantower the sensor  
from dragino import Dragino # the board 
from simplecayennelpp import CayenneLPP # a way to store the data (a standard)

#d = Dragino("/home/pi/dragino.ini")

sensor = Plantower ("/dev/ttyUSB1")

sensor.read() # read the data 

data=sensor.read() # store teh data 

print(data) # lots of data 

data.gr03um  # particules over 2.5 i think 

# store 10 samples in a list 
datalist= []

for i in range (10):
    data = sensor.read()
    datalist.append(data.gr03um)

average = sum(datalist) / len(datalist)  # average teh list 

d.send_bytes([2])  # createsa 2 byte variables ithink 

my_location = d.get_gps() # get teh gps location 
print (my_location)


lpp=CayenneLPP() # gps loaction 
lpp.addGPS(1,my_location.latitude,my_location.longitude,my_location.altitude) # get my location 

lpp.addAnalogInput(2,average/10) # 

d.send_bytes(list(lpp.getBuffer()))


# login for kn 
#mydevices.com
#u : emf@computernodes.net
#p : backpackmemorytooth