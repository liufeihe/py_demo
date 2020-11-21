#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import numpy
from time import sleep


def usbCamera():
    cap = cv2.VideoCapture(1)# 调整参数实现读取视频或调用摄像头
    while 1:
        sleep(0.1)
        res = cap.read()
        print(res)
        cv2.imwrite('cap.png', res.frame)
        break
        # cv2.imshow("cap", frame)
        # if cv2.waitKey(100) & 0xff == ord('q'):
        #     break
    cap.release()
    # cv2.destroyAllWindows()

def main():
    usbCamera()

if __name__ == "__main__":
    main()