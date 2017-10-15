import time
import RPi.GPIO as io # Motion Sensor
io.setmode(io.BCM)

pir_pin = 18 # Set up motion sensor pin


io.setup(pir_pin, io.IN)         # activate input
#io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

while True:
    time.sleep(0.5)
    if io.input(pir_pin):
	print ('Motion Detected')
    else:
	print ('No Motion')
