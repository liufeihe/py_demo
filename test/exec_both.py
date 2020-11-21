#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
import time
from sys import argv

# 启动场景
def start_scene(ip, id, status=[1,3], wait=30, exect=1, clear=1):
  url = 'http://' + ip + '/public/task'
  ss = '{"scene_id": ' + str(id) + ', "execute_count": ' + str(exect) + ', "clear":' + str(clear) + '}'
  r = requests.post(url, data = ss)
  r = json.loads(r.text)
  if(r['code'] == 0):
    print(ip+'start scene ok')
    return False
  else:
    print(ip+'start scene failed')
    return True

def stop_scene(ip):
  url = 'http://' + ip + '/public/robot/action'
  ss = '{"cmd": "stop_task"}'
  r = requests.post(url, data = ss)
  r = json.loads(r.text)
  if(r['code'] == 0):
    print(ip+'stop scene ok')
    return False
  else:
    print(ip+'stop scene failed')
    return True

def get_task_status(ip):
  url = 'http://' + ip + '/public/robot/action'
  ss = '{"cmd": "get_task_status"}'
  r = requests.post(url, data = ss)
  r = json.loads(r.text)
  if(r['code'] == 0):
    print(r['data'])
    print(ip+'get task status:'+str(r['data']['task_status']))
    return False
  else:
    print(ip+'get task status failed')
    return True

def start_both():
  start_scene('192.168.3.143', 10038, exect=0)
  start_scene('192.168.3.144', 10038, exect=0)

def stop_both():
  stop_scene('192.168.3.143')
  stop_scene('192.168.3.144')

if __name__ == "__main__":
  if argv[1] == 'start':
    # print('start')
    start_both()
  elif argv[1] == 'stop':
    # print('stop')
    stop_both()
  else:
    get_task_status('192.168.3.141')
    print('no action')