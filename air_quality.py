#!/usr/bin/env python
import bme680 # air quality sensor 
import time # current time 
from influxdb import InfluxDBClient  # influx client 
import datetime

print("""Display Temperature, Pressure, Humidity and Gas
Press Ctrl+C to exit
""")

# connect to influxdb, create home db if not already created
# and select database to use 
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client.create_database('home')
client.switch_database('home')

# create a instance of the sensor
try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These calibration data can safely be commented
# out, if desired.

print('Calibration data:')
for name in dir(sensor.calibration_data):

    if not name.startswith('_'):
        value = getattr(sensor.calibration_data, name)

        if isinstance(value, int):
            print('{}: {}'.format(name, value))

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

print('\n\nInitial reading:')
for name in dir(sensor.data):
    value = getattr(sensor.data, name)

    if not name.startswith('_'):
        print('{}: {}'.format(name, value))

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

# Up to 10 heater profiles can be configured, each
# with their own temperature and duration.
# sensor.set_gas_heater_profile(200, 150, nb_profile=1)
# sensor.select_gas_heater_profile(1)

print('\n\nPolling:')
try:
    while True:
        if sensor.get_sensor_data():
            output = '{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH'.format(
                sensor.data.temperature,
                sensor.data.pressure,
                sensor.data.humidity)


            if sensor.data.heat_stable:
                print('{0},{1} Ohms'.format(
                    output,
                    sensor.data.gas_resistance))
                gas = sensor.data.gas_resistance
            else:
                gas = "no data"
            if gas = "no data":  
                data = [{"measurement": "bme680_sensor",
                    "tags": {
                    "Location":"living_room",
                    "Floor": "1st_Floor"
                    },
                    "time": str(datetime.datetime.now()),
                    "fields": {
                    "temperture" : sensor.data.temperature,
                    "pressure" : sensor.data.pressure,
                    "humidity" : sensor.data.humidity
                    #"gas_resistance" : gas
                    }
                
                }
                ]
            else:
                data = [{"measurement": "bme680_sensor",
                    "tags": {
                    "Location":"living_room",
                    "Floor": "1st_Floor"
                    },
                    "time": str(datetime.datetime.now()),
                    "fields": {
                    "temperture" : sensor.data.temperature,
                    "pressure" : sensor.data.pressure,
                    "humidity" : sensor.data.humidity,
                    "gas_resistance" : gas
                    }
                
                }
                ]
    
            client.write_points(data)

            

        time.sleep(1)

except KeyboardInterrupt:
    pass