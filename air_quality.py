#useful website from #https://cayenne.mydevices.com/
# http://wiki.dragino.com/index.php?title=Lora_Shield

from plantower import Plantower # plantower the sensor  
from dragino import Dragino # the board 
from simplecayennelpp import CayenneLPP # a way to store the data (a standard)
from influxdb import InfluxDBClient

#d = Dragino("/home/pi/dragino.ini")

sensor = Plantower ("/dev/ttyUSB0")
sensor.read() # read the data 
data=sensor.read() # store teh data 
print(data) # lots of data 
data.gr03um  # particules over 2.5 i think 

# store 10 samples in a list 
datalist= []

while True:

    for i in range (100):
        data = sensor.read()
        datalist.append(data.gr03um)

    gr03um_average = sum(datalist) / len(datalist)  # average teh list 
    #d.send_bytes([2])  # createsa 2 byte variables ithink 
    #my_location = d.get_gps() # get teh gps location 
    
    data = [{"measurement": "AirParticles",
                "tags": {
                "Location":"living_room",
                "Floor": "1st_Floor"
            },
                "time": str(datetime.datetime.now()),
                "fields": {
                "03um" : gr03um_average
            }
            
            }
    ]

# login for kn 
#mydevices.com
#u : emf@computernodes.net
#p : backpackmemorytooth