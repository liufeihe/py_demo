from time import sleep
from threading import Thread
import grpc
import robot_controller_pb2 as rcs_pb2
import robot_controller_pb2_grpc as rcs_pb2_grpc
from google.protobuf.empty_pb2 import Empty

rcs = None

def generate_cmd(cmd, internal=0.1):
    while True:
        sleep(internal)
        yield cmd

def print_io(io_type, ios):
    for io in ios:
        print('{0}, pin: {1}, value: {2}'.format(io_type, io.pin, io.value))

def get_robot_ios():
    global rcs
    print('read robot ios')
    try:
        num = 0
        res = rcs.GetRobotIOData(generate_cmd(rcs_pb2.RobotDataCmd()))
        for r in res:
            num = num+1
            print(num)
            print_io('di', r.robotDIOIn)
            print_io('d0', r.robotDIOOut)
            print_io('ai', r.robotAIOIn)
            print_io('ao', r.robotAIOOut)
    except Exception as e:
        print(e)
        sleep(1)
        t = Thread(target=get_robot_ios)
        t.start()

def get_external_ios():
    global rcs
    print('get external ios')
    try:
        res = rcs.GetExternalIOs(rcs_pb2.ExternalDevice(id=10001))
        print_io('dis', res.dis)
        print_io('dos', res.dos)
        print_io('ais', res.ais)
        print_io('aos', res.aos)

        sleep(1)
        t = Thread(target=get_external_ios)
        t.start()
    except Exception as e:
        print('error, {0}'.format(e))
        sleep(1)
        t = Thread(target=get_external_ios)
        t.start()
    

def run():
    global rcs
    print('create channel')
    channel = grpc.insecure_channel('192.168.1.5:5181')
    rcs = rcs_pb2_grpc.RobotControllerStub(channel)
    print('send request')
    # res = rcs.GetJointTemp(rcs_pb2.IntRequest(index=1))
    # print(res.degree)
    
    # res = rcs.GetGravity(Empty())
    # if res is not None:
    #     print('x:{0}, y:{1}, z:{2}'.format(res.x, res.y, res.z))
    
    # t = Thread(target=get_robot_ios)
    # t.start()

    t = Thread(target=get_external_ios)
    t.start()
    
        
    print('end')

if __name__ == "__main__":
    run()