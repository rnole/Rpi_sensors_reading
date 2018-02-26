from globals import Session
from models import Sensors_data
import datetime
import server


def save_sensor_data(sensor_data):
    session = Session()
    
    new_data = Sensors_data(
                sensor_id   = int(sensor_data['sensor_id']),
                timestamp   = sensor_data['timestamp'],
                co          = float(sensor_data['co']),
                o3          = float(sensor_data['o3']),
                no2         = float(sensor_data['no2']),
                so2         = float(sensor_data['so2']),
                co2         = float(sensor_data['co2']),
                temperature = float(sensor_data['temp']),
                humidity    = float(sensor_data['hum']),
                uv          = float(sensor_data['uv']),
                luminosity  = float(sensor_data['lum']),
                pm1         = float(sensor_data['pm1']),
                pm25        = float(sensor_data['pm25']),
                pm10        = float(sensor_data['pm10']),
                noise       = float(sensor_data['sonido']))

    session.add(new_data)
    session.commit()
    session.close()


def send_saved_data():
    session = Session()
    saved_data_entries = session.query(Sensors_data).all()

    response = 'success'

    for eachRow in saved_data_entries:
        sensor_data = dict() 
        sensor_data['username']     = "richard"
        sensor_data['pwd']          = "passw0rd"
        sensor_data['sensor_id']    = eachRow.sensor_id
        sensor_data['timestamp']    = eachRow.timestamp
        sensor_data['co']           = eachRow.co
        sensor_data['o3']           = eachRow.o3
        sensor_data['no2']          = eachRow.no2
        sensor_data['so2']          = eachRow.so2
        sensor_data['co2']          = eachRow.co2
        sensor_data['temp']         = eachRow.temp
        sensor_data['hum']          = eachRow.hum
        sensor_data['uv']           = eachRow.uv
        sensor_data['lum']          = eachRow.lum
        sensor_data['pm1']          = eachRow.pm1
        sensor_data['pm25']         = eachRow.pm25
        sensor_data['pm10']         = eachRow.pm10
        sensor_data['sonido']       = eachRow.sonido

        current_response = server.Send_to_server(sensor_data)

        if(current_response == 'success'):
            session.delete(eachRow)

        else:
            break

    session.commit()
    session.close()


