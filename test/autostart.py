import requests
import json
import time

# 启动场景
def start_scene(ip, id, status=[1,3], wait=30, exect=1, clear=1):
    url = 'http://' + ip + '/public/task'
    ss = '{"scene_id": ' + str(id) + ', "execute_count": ' + str(exect) + ', "clear":' + str(clear) + '}'
    r = requests.post(url, data = ss)
    r = json.loads(r.text)
    if(r['code'] != 0):
        return False
    # if(wait):
    #     return wait_scene(ip, r['data']['id'], status, wait)
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
        k = wait_robot(ip, 5, wait) # 等待机器人进入空闲状态，等待时间为wt
        return k
    return True

# 等待机器人状态
def wait_robot(ip, status, wait=30):
    t = time.time()
    while(True):
        if((time.time()-t) > wait):
            return False
        time.sleep(0.5)
        if(robot_data(ip) == status):
            return True

def auto_start():
    t = time.time() # 获取当前时间
    url = '127.0.0.1' # 本机IP
    sceneid = 10022 # 场景ID
    overtime = 300 # 超时时间
    print('场景ID：', sceneid)
    print('启动时间：', time.asctime(time.localtime(t)))

    while(True):
        if((time.time()-t) > overtime):
            print('开机超时')
            break
        time.sleep(3)
        try:
            r = robot_data(url)
        except:
            pass
        else:
            if(r in [4,5,1,12]):
                print('开机没问题 mode:', r)
                break

    while(True):
        if((time.time()-t) > overtime):
            print('启动机器人超时')
            break
        time.sleep(3)
        try:
            r = start_sys(url)
        except:
            pass
        else:
            if(r):
                print('启动机器人没问题')
                break

    time.sleep(3)

    while(True):
        if((time.time()-t) > overtime):
            print('启动场景超时')
            break
        time.sleep(3)
        try:
            r = start_scene(url, sceneid)
        except:
            pass
        else:
            if(r):
                print('启动场景没问题，场景任务ID：', r)
                break
    
if __name__ == "__main__":
    start_scene()