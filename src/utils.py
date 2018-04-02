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
    

