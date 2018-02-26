from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pyaudio
import spl_lib as spl
engine 	= create_engine('sqlite:///bid_backup.sqlite')
Session = sessionmaker(bind=engine)


PEAK_DB = 0
CHUNKS  = [4096, 9600]       # Use what you need
CHUNK   = CHUNKS[1]
FORMAT  = pyaudio.paInt16    # 16 bit
CHANNEL = 1                 # 1 means mono. If stereo, put 2

RATES   = [44300, 48000]
RATE    = RATES[1]

NUMERATOR, DENOMINATOR = spl.A_weighting(RATE)

