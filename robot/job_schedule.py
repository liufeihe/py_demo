#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
from robot_status import RobotStatus
from device_status import DeviceStatus

class JobSchedule():
  def __init__(self, name, id):
    self.name = name
    self.id = id
    self.taskList = []
    self.ds = DeviceStatus(id, self)
    self.rs = RobotStatus(id)

  def startDeviceStatusScan(self):
    self.ds.scan()

  def startRobotStatusScan(self):
    self.rs.scan()

  def run(self):
    print(self.ds.statusList)
    self.getTaskList()
    self.schedule()

  def getTaskList(self):
    # 从mysql中获取该job id的task
    # get task list info from mysql
    print("[JobS]get task list")

  def schedule(self):
    # 根据task list进行调度
    print("[JobS]schedule")

  def scan(self):
    #定时调用run
    self.run()
    timer = threading.Timer(2, self.scan)
    timer.start()

if __name__ == "__main__":
  js = JobSchedule('js', 1)
  js.startDeviceStatusScan()
  js.startRobotStatusScan()
  # js.scan()
