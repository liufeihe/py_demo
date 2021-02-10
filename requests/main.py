import requests
import json

_debug = True
_debug_url = 'http://192.168.3.227'

def get_io_device(device_id):
    if _debug:
        url = _debug_url
    print("get device: {0}".format(device_id))
    res_data = None
    try:
        res = requests.get(url+'/api/device?id={0}'.format(device_id))
        res = json.loads(res.text)
        res_data = res.get('data', {})
    except Exception as e:
        print( "get io device failed, {0}".format(e))
    
    return res_data

def update_io_device(data):
    if _debug:
        url = _debug_url
    print("update device: {0}".format(data))
    is_ok = False
    try:
        json_data = json.dumps(data)
        res = requests.put(url+'/api/device', data=json_data, headers={'Content-Type':'application/json'})
        res = json.loads(res.text)
        print(res)
        is_ok = res.get('code')==0
    except Exception as e:
        print( "update io device failed, {0}".format(e))
    
    return is_ok

def main():
    device_id = 10020
    data = get_io_device(device_id)
    device = data.get('device')
    enable = True
    device['status'] = 2 if enable else 3
    service = data.get('service')
    is_ok = update_io_device({
        'device': device,
        'service': service,
    })
    print(is_ok)


if __name__ == "__main__":
    main()