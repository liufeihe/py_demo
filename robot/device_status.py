#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import random

class DeviceStatus():
  def __init__(self, id, js=None):
    self.id = id
    self.statusList = []
    self.js = js

  def run(self):
    # #通过http从IO接口获取外设状态
    # print("[DeviceS]get device status")
    # #将外设状态存入mysql
    # print("[DeviceS]save device status to mysql")
    self.statusList = []
    for _ in range(10):
      self.statusList.append(random.randint(0,1))
    if self.js:
      self.js.run()

  def scan(self):
    #定时调用run
    self.run()
    timer = threading.Timer(2, self.scan)
    timer.start()

if __name__ == "__main__":
  dev = DeviceStatus(1)
  dev.scan()
  print('device status thread is running')

