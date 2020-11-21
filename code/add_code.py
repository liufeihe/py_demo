#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
from time import sleep
from requests.packages import urllib3

# _url = 'http://api.dev.lebai.ltd/admin'
_url = 'https://api.lebai.ltd/admin/test'
# _url = 'https://api.lebai.ltd/admin/prod'


def login(user, pwd):
    global _url
    data = {
        'account': user,
        'password': pwd
    }
    url = '{0}{1}'.format(_url, '/public/login')
    urllib3.disable_warnings()
    r = requests.post(url, json=data, headers={'Content-Type':'application/json'}, verify=False)
    r = json.loads(r.text)
    data = r.get('data', {})
    return data.get('session_id')

def add_code(data, session_id):
    global _url
    level = data.get('level')
    levelMap = {
        'INFO': 1,
        'WARNING': 2,
        'ERROR': 3,
    }
    level = levelMap.get(level, 1)
    data = {
        'code': data.get('code'),
        'level': level,
        'reason': data.get('reason'),
        'solution': data.get('solution'),
        'prd_category_id': 1,
        'status': 1,
        'weight': 30,
    }
    url = '{0}{1}'.format(_url, '/api/err_code')
    urllib3.disable_warnings()
    r = requests.post(url, json=data, headers={'Content-Type':'application/json', 'X-AUTH-SESSION': session_id}, verify=False)
    r = json.loads(r.text)
    return r.get('id')!=None
    # try:
    #     r = requests.post(url, json=data, headers={'Content-Type':'application/json', 'X-AUTH-SESSION': session_id})
    #     r = json.loads(r.text)
    #     print(r)
    #     return True
    # except:
    #     return False

def read_codes():
    lines = None
    with open('./code.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def main():
    lines = read_codes()
    code_list = []
    for line in lines:
        line = line.split('\t')
        line2 = []
        for l in line:
            if l!='':
                line2.append(l)
        # print(line2)
        code_list.append({
            'code': line2[0],
            'level': line2[1],
            'reason': line2[-2],
            'solution': line2[-1]
        })

    session_id = login('admin', '111111')
    # session_id = login('liufh', 'sTHdGB9mHKXJEdvP')
    if session_id is None:
        print('登录失败')
        return
    print(session_id)
    
    # code_list = [code_list[0]]
    ignore_codes = ['1000']
    for code_data in code_list:
        code = code_data.get('code')
        if code in ignore_codes:
            continue
        sleep(0.1)
        is_ok = add_code(code_data, session_id)
        if is_ok:
            print("添加ok，{0}".format(code_data))
        else:
            print("添加失败，{0}".format(code_data))
            break

if __name__ == "__main__":
    main()