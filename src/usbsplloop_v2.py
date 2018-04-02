import sys
import serial
import time
import datetime
import backup
import os, errno
import pyaudio
import server
import spl_lib as spl
from pytz import timezone
from scipy.signal import lfilter
from globals import PEAK_DB, CHUNK, FORMAT, RATE, CHANNEL
from globals import NUMERATOR, DENOMINATOR
import numpy
import utils

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
received_data = ''


#Listen to mic
pa = pyaudio.PyAudio()


def Clean_globals():
        global received_data, PEAK_DB

        received_data = ''
        PEAK_DB = 0

def Check_if_midnight():
    now_utc = datetime.datetime.now(timezone('UTC'))
    now_peru = now_utc.astimezone(timezone('America/Lima')).strftime("%H:%M")
    if(now_peru == '00:00'):
        ser.write('z')



def get_decibels(stream, spl):
    print("Listening")
    try:
        block = stream.read(CHUNK)
    except IOError, e:
        print(" Error recording: %s" % (e))
    else:
        ## Int16 is a numpy data type which is Integer (-32768 to 32767)
        ## If you put Int8 or Int32, the result numbers will be ridiculous
        decoded_block = numpy.fromstring(block, 'Int16')
        ## This is where you apply A-weighted filter
        y = lfilter(NUMERATOR, DENOMINATOR, decoded_block)
        new_decibel = 20*numpy.log10(spl.rms_flat(y))

        return new_decibel

def main():

    global received_data, PEAK_DB
    current_response  = ''
    previous_response = ''

    ser.flushInput()
    last_time = int(time.time())

    while True:
        
        if( (int(time.time()) - last_time) >= 2):
            print 'Ya paso 2 secs'

            audio_stream = pa.open(format = FORMAT,
                                    channels = CHANNEL,
                                    rate = RATE,
                                    input = True,
                                    frames_per_buffer = CHUNK)

            last_time = int(time.time())
            dB = int(get_decibels(audio_stream, spl))
            print 'New decibel: ', dB

            audio_stream.stop_stream()
            audio_stream.close()

            if dB > PEAK_DB:
                PEAK_DB = dB
        
        
        received_data = ser.readline()

        if('\n' in received_data):
            ser.flushInput()
            sensor_data = {}
            received_data  = received_data[0: len(received_data)-1]
            
            Check_if_midnight()
            utils.Parse_serial_data(received_data, sensor_data, PEAK_DB)    
            print 'sensor data to be sent: ', sensor_data

            current_response = server.Send_to_server(sensor_data)          #Como hacer unit tests para esto?

            if(current_response == 'failure'):
                backup.save_sensor_data(sensor_data)


            elif((current_response == 'success') and (previous_response == 'failure')):
                backup.send_saved_data()
                ser.flushInput()


            previous_response = current_response
            Clean_globals()

        time.sleep(0.2)

    
    pa.terminate()

if __name__ == '__main__':
    main()
    #print 'Hello there!'





