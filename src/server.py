
import requests

def Send_to_server(sensor_data, path):

    url = 'https://dev.jobenas.com' + path 

    try:
        r = requests.post(url, json=sensor_data)
        print 'RESPUESTA: ', r.json()
        return 'success'

    except requests.exceptions.ConnectionError:
        print 'Entre a connection error'
        return 'failure'


