#!/usr/bin/env python
import os, errno
import pyaudio
import spl_lib as spl
from scipy.signal import lfilter
import numpy

"""
The following is similar to a basic CD quality
   When CHUNK size is 4096 it routinely throws an IOError.
   When it is set to 8192 it doesn't.
   IOError happens due to the small CHUNK size

   What is CHUNK? Let's say CHUNK = 4096
   math.pow(2, 12) => RATE / CHUNK = 100ms = 0.1 sec
"""
"""
Different mics have different rates.
For example, Logitech HD 720p has rate 48000Hz
"""
CHUNKS  = [4096, 9600]       # Use what you need
CHUNK   = CHUNKS[1]
FORMAT  = pyaudio.paInt16    # 16 bit
CHANNEL = 1                 # 1 means mono. If stereo, put 2

RATES   = [44300, 48000]
RATE    = RATES[1]

PEAK_DB = 0
NUMERATOR, DENOMINATOR = spl.A_weighting(RATE)

#Listen to mic
pa = pyaudio.PyAudio()

stream = pa.open(format = FORMAT,
                channels = CHANNEL,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)


def spl_is_meaningful(old, new):
    return abs(old - new) > 3



def listen(old=0, error_coint=0, min_decibel=100, max_decibel=0):
    print("Listening")
    while True:
        try:
            block = stream.read(CHUNK)
        except IOError, e:
            error_count += 1
            print(" (%d) Error recording: %s" % (error_count, e))
        else:
            ## Int16 is a numpy data type which is Integer (-32768 to 32767)
            ## If you put Int8 or Int32, the result numbers will be ridiculous
            decoded_block = numpy.fromstring(block, 'Int16')
            ## This is where you apply A-weighted filter
            y = lfilter(NUMERATOR, DENOMINATOR, decoded_block)
            new_decibel = 20*numpy.log10(spl.rms_flat(y))
            #print 'new decibels: ', new_decibel
            #return new_decibel
            
            if spl_is_meaningful(old, new_decibel):
                old = new_decibel
                print('A-weighted: {:+.2f} dB'.format(new_decibel))
        

    stream.stop_stream()
    stream.close()
    pa.terminate()


if __name__ == '__main__':
    print 'Hello there!'
    listen()
    
