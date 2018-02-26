import serial


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=0)
ser.write('Z')
ser.close()

