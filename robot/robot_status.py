#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading

class RobotStatus():
  def __init__(self, id):
    self.id = id

  def run(self):
    #通过http从IO接口获取外设状态
    print("[RobotS]get robot status")
    #将外设状态存入mysql
    print("[RobotS]save robot status to mysql")

  def scan(self):
    #定时调用run
    self.run()
    timer = threading.Timer(2, self.scan)
    timer.start()

if __name__ == "__main__":
  robot = RobotStatus(1)
  robot.scan()
  print('robot status thread is running')

