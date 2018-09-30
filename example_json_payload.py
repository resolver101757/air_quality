# -*- coding: utf-8 -*-
import datetime
gr03um_average = 1

data = [{"measurement": "AirParticles",
            "tags": {
            "Location":"BedRoom",
            "Floor": "FirstFloor"
        },
            "time": str(datetime.datetime.now()),
            "fields": {
            "03um" : gr03um_average
        }
        
        }
    ]

print(data)