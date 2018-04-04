import datetime
from pytz import timezone


def Parse_serial_data(rx_buf, sensor_data, noise):
    parsed_data_list = []
    parsed_data_list = rx_buf.split(',')
    now_utc = datetime.datetime.now(timezone('UTC'))

    sensor_data['username'] = "richard"
    sensor_data['pwd'] = "passw0rd"
    sensor_data['sensor_id'] = "2"
    sensor_data['timestamp'] = now_utc.astimezone(timezone('America/Lima')).strftime("%Y-%m-%d %H:%M:%S")
    sensor_data['co'] = parsed_data_list[0]
    sensor_data['o3'] = parsed_data_list[1]
    sensor_data['no2'] = parsed_data_list[2]
    sensor_data['so2'] = parsed_data_list[3]
    sensor_data['co2'] = parsed_data_list[6]
    sensor_data['temp'] = parsed_data_list[10]
    sensor_data['hum'] = parsed_data_list[11]
    sensor_data['uv'] = parsed_data_list[5]
    sensor_data['lum'] = parsed_data_list[4]
    sensor_data['pm1'] = parsed_data_list[7]
    sensor_data['pm25'] = parsed_data_list[8]
    sensor_data['pm10'] = parsed_data_list[9]
    sensor_data['sonido'] = str(noise)
    

def Check_if_midnight():
    now_utc = datetime.datetime.now(timezone('UTC'))
    now_peru = now_utc.astimezone(timezone('America/Lima')).strftime("%H:%M")
    if((now_peru == '00:00') or (now_peru == '00:01')):
        ser.write('z')

def Has_passed_15_minutes(counter):
    if(counter == 15):
        return True
    else:
        return False


def Reset_counter_minute():
    return 0


def Increase_counter_minute(counter):
    counter =  counter + 1
    return counter

def Get_average_reading(readings_list):
    average_reading = dict()
    now_utc = datetime.datetime.now(timezone('UTC'))

    average_reading['username']  = "richard"
    average_reading['pwd']       = "passw0rd"
    average_reading['sensor_id'] = "2"
    average_reading['timestamp'] = now_utc.astimezone(timezone('America/Lima')).strftime("%Y-%m-%d %H:%M:%S")

    for idx in range(0, len(readings_list)):
        average_reading['co']       += readings_list[idx]
        average_reading['o3']       += readings_list[idx]
        average_reading['no2']      += readings_list[idx]
        average_reading['so2']      += readings_list[idx]
        average_reading['co2']      += readings_list[idx]
        average_reading['temp']     += readings_list[idx]
        average_reading['hum']      += readings_list[idx]
        average_reading['uv']       += readings_list[idx]
        average_reading['lum']      += readings_list[idx]
        average_reading['pm1']      += readings_list[idx]
        average_reading['pm25']     += readings_list[idx]
        average_reading['pm10']     += readings_list[idx]
        average_reading['sonido']   += readings_list[idx]


    average_reading['co']       /= len(readings_list)
    average_reading['o3']       /= len(readings_list)
    average_reading['no2']      /= len(readings_list)
    average_reading['so2']      /= len(readings_list)
    average_reading['co2']      /= len(readings_list)
    average_reading['temp']     /= len(readings_list)
    average_reading['hum']      /= len(readings_list)
    average_reading['uv']       /= len(readings_list)
    average_reading['lum']      /= len(readings_list)
    average_reading['pm1']      /= len(readings_list)
    average_reading['pm25']     /= len(readings_list)
    average_reading['pm10']     /= len(readings_list)
    average_reading['sonido']   /= len(readings_list)

    return average_reading


