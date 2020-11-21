import requests
import json
import time

# 关节空间运动
def movej(ip, pose, acc, ver, blr = 1):
    url = 'http://'+ip+'/public/robot/action'
    ss = '{\
    "cmd": "movej",\
    "data": {\
    "pose_to": [' + ','.join(str(x) for x in pose) + '],\
    "is_joint_angle": true,\
    "acceleration":' + str(acc) + ',\
    "velocity":' + str(ver) + ',\
    "time": 0,\
    "blend_radius": ' + str(blr) + '}}'
    r = requests.post(url, data=ss)
    r = json.loads(r.text)
    return r

# 查询机器人状态
def robot_data(ip):
    url = 'http://'+ip+'/public/robot/action'
    ss = '{"cmd":"robot_data"}'
    r = requests.post(url, data=ss)
    r = json.loads(r.text)
    return r['data']['robot_mode']

# 启动机器人
def start_sys(ip, wait=30):
    url = 'http://'+ip+'/public/robot/action'
    ss = '{"cmd":"start_sys"}'
    r = requests.post(url, data=ss)
    r = json.loads(r.text)
    if(r['code'] != 0): # 没有post成功
        return False
    if(wait):
        k = wait_robot(ip, [5], wait) # 等待机器人进入空闲状态，等待时间为wt
        return k
    return True

# 停止机器人
def stop_sys(ip, wait=30):
    url = 'http://'+ip+'/public/robot/action'
    ss = '{"cmd":"stop_sys"}'
    r = requests.post(url, data=ss)
    r = json.loads(r.text)
    if(r['code'] != 0): # 没有post成功
        return False
    if(wait):
        k = wait_robot(ip, 12, wait) # 等待机器人进入空闲状态，等待时间为wt
        return k
    return True

# 等待机器人状态
def wait_robot(ip, status, wait=30):
    t = time.time()
    while(True):
        if((time.time()-t) > wait):
            return False
        time.sleep(0.5)
        if(robot_data(ip) in status):
            return True


# 启动场景
def start_scene(ip, id, status=[1,3], wait=30, exect=1, clear=1):
    url = 'http://' + ip + '/public/task'
    ss = '{"scene_id": ' + str(id) + ', "execute_count": ' + str(exect) + ', "clear":' + str(clear) + '}'
    r = requests.post(url, data = ss)
    r = json.loads(r.text)
    if(r['code'] != 0):
        return False
    if(wait):
        return wait_scene(ip, r['data']['id'], status, wait)
    return (r['data']['id'])

# 等待场景运行或完成
def wait_scene(ip, sid, status=[1,3], wait=30):
    url = 'http://' + ip + '/public/task' + '?id=' + str(sid)
    t = time.time()
    while(True):
        if((time.time()-t) > wait):
            return False
        time.sleep(0.5)
        k = requests.get(url)
        k = json.loads(k.text)
        if(k['data']['status'] > 3):
            return False
        if(k['data']['status'] in status):
            break
    return sid