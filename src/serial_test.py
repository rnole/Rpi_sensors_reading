import serial
import time



ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=0)

while True:

    sensor_data = ser.readline()
    if(sensor_data != ''):
        print 'Dentro del if'

    print 'Fuera del if'
    time.sleep(2)

