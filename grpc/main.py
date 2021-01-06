from time import sleep
import grpc
import rcs_pb2
import rcs_pb2_grpc
from google.protobuf.empty_pb2 import Empty

def generate_cmd(cmd):
    while True:
        sleep(0.1)
        yield cmd

def print_io(io_type, ios):
    for io in ios:
        print('{0}, pin: {1}, value: {2}'.format(io_type, io.pin, io.value))

def run():
    num = 0
    print('create channel')
    channel = grpc.insecure_channel('192.168.3.227:5181')
    rcs = rcs_pb2_grpc.RobotControllerStub(channel)
    print('send request')
    # res = rcs.GetJointTemp(rcs_pb2.IntRequest(index=1))
    # print(res.degree)
    
    # res = rcs.GetGravity(Empty())
    # if res is not None:
    #     print('x:{0}, y:{1}, z:{2}'.format(res.x, res.y, res.z))

    res = rcs.GetRobotIOData(generate_cmd(rcs_pb2.RobotDataCmd()))
    for r in res:
        num = num+1
        print(num)
        print_io('di', r.robotDIOIn)
        print_io('d0', r.robotDIOOut)
        print_io('ai', r.robotAIOIn)
        print_io('ao', r.robotAIOOut)
        
    print('end')

if __name__ == "__main__":
    run()