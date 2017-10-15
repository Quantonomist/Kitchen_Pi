print ('Test')

import time
import RPi.GPIO as io # Motion Sensor
io.setmode(io.BCM)
import sys
from Hologram.HologramCloud import HologramCloud
import Adafruit_DHT  # Temp/Humidity Sensor 
from Adafruit_AMG88xx import Adafruit_AMG88xx # Predator Camera 
#from time import sleep


# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
dht_sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 23

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
#if humidity is not None and temperature is not None:
#    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
#else:
#    print('Failed to get reading. Try again!')




pir_pin = 18 # Set up motion sensor pin
#door_pin = 23

io.setup(pir_pin, io.IN)         # activate input
#io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp


#device_key = raw_input("What is your device key? ")
#device_key = str(144465)
device_key = 144465

credentials = {'devicekey': device_key}

hologram = HologramCloud(credentials, network='cellular')
#hologram = HologramCloud(credentials, authentication_type='csrpsk')


result = hologram.network.connect()
if result == False:
    print 'Failed to connect to cell network'

print 'Cloud type: ' + str(hologram)

print 'Network type: ' + str(hologram.network_type)

#recv = hologram.sendMessage("one two three!",
#                                topics = ["TOPIC 1","TOPIC 2"],
#                                timeout = 3)

#recv = hologram.sendMessage('Intruder Alert')

#print 'RESPONSE MESSAGE: ' + hologram.getResultString(recv)

#print 'LOCAL IP ADDRESS: ' + str(hologram.network.localIPAddress)
#print 'REMOTE IP ADDRESS: ' + str(hologram.network.remoteIPAddress)

hologram.network.disconnect()




'''
destination_number = raw_input("What is your destination number? ")
print 'destination numer is',destination_number
#destination_number = 8123402307

print ''
recv = hologram.sendSMS(destination_number, "Motion Detected!") # Send SMS to destination number
print "RESPONSE CODE RECEIVED: " + str(recv)

print ''
print 'Testing complete.'
print ''
'''



#### Predator Camera ###
sensor = Adafruit_AMG88xx()
count = 0
while count <= 10:
    count+=1
    time.sleep(0.5)
    print (sensor.readPixels())

#######################


while True:
    if io.input(pir_pin):
        print("PIR ALARM!")
	#send message here
	result = hologram.network.connect()
	if result == False:
            print 'Failed to connect to cell network'
	humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, pin) # Read in the temp and humidity
	print ('Motion Alert...Temp is: %s  Humidity is: %s:'%(temperature,humidity))
	recv = hologram.sendMessage('Intruder Alert...Temp is: %s  Humidity is: %s:' %(temperature,humidity))
	hologram.network.disconnect()
	time.sleep(120)
    else:
	print ('No Alarm')
    time.sleep(5)
    
    
