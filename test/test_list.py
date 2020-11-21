#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading

class Job:
    def __init__(self, jid, priority=1):
        self.job_id = jid
        self.priority = priority
    def __str__(self):
        return "job_id:{0}, priority: {1}".format(self.job_id, self.priority)
    def set_priority(self, priority):
        self.priority = priority

def test():
    print(1)
    timer = threading.Timer(1, test)
    timer.start()

def reverseList():
    a = [40,30,20,10]
    for i in range(len(a)-1, -1, -1):
        if i== 2:
            a.remove(a[i])
    print(a)

def cmp(x,y):
    return y.job_id-x.job_id

def get_min_item_from_list_by_item_key(item_list, item_key):
    min_item = None
    min_value = None
    for idx, item in enumerate(item_list):
        value = getattr(item, item_key)
        if idx==0:
            min_value = value
            min_item = item
        elif value < min_value:
            min_value = value
            min_item = item
    return min_item

def sort_list():
    job_list = []
    j1 = Job(1)
    j2 = Job(2, 2)
    j3 = Job(0, 3)
    j4 = Job(4)
    job_list.append(j1)
    job_list.append(j2)
    job_list.append(j3)
    # print(getattr(j1, 'job_id'))
    # if job_list.index(j4):
    #     print('j3')
    job_list.append(j4)
    print(get_min_item_from_list_by_item_key(job_list, 'job_id'))
    # for j in job_list:
    #     print(j)
    # print('after sort:')
    # # job_list.sort(key='job_id')
    # # job_list.sort(cmp)
    # # job_list.sort(lambda x,y: y.priority-x.priority)
    # for j in job_list:
    #     print(j)

def rv_list():
    job_list = []
    a_list = []
    for i in range(10):
        job_list.append(Job(i))
    for j in job_list:
        print(j)
    print('after')
    len_l = len(job_list)
    for idx in range(len_l):
        j_idx = len_l-1-idx
        job = job_list[j_idx]
        if job.job_id in [2, 3]:
            job_list.remove(job)
    # while len(job_list)!= 0:
    #     j = job_list[0]
    #     print(j)
    #     job_list.remove(j)
    #     a_list.append(j)
    # print(len(job_list))
    for j in job_list:
        print(j)

if __name__ == "__main__":
    # test()
    # reverseList()
    # sort_list()
    rv_list()