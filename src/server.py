
import requests

def Send_to_server(sensor_data):

    url = 'https://dev.jobenas.com/limaio/api/v1.0/registerReading'

    try:
        r = requests.post(url, json=sensor_data)
        print 'RESPUESTA: ', r.json()
        return 'success'

    except requests.exceptions.ConnectionError:
        print 'Entre a connection error'
        return 'failure'


