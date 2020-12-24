from threading import Thread,Timer
from time import sleep

time_count = 0
thread_count = 0

def thread1_run(*args):
    global thread_count
    while True:
        sleep(0.1)
        print("t1, {0}, {1}".format(args, thread_count))
        thread_count = thread_count+1

def thread2_run(*args):
    global thread_count
    while True:
        sleep(0.1)
        print("t2 {0}, {1}".format(args, thread_count))
        thread_count = thread_count+1
    
def timer_run():
    global time_count
    print('time')
    time_count = time_count+1
    if time_count>30:
        return
    timer = Timer(0.1, timer_run)
    timer.start()
    timer.join()

def run(*args):
    print("run, {0}".format(args))
    timer_run()
    print('run done')

def test_args():
    count = 0
    thread = None
    a = [1]
    b= [2]
    while True:
        sleep(0.1)
        count = count+1
        print('main, {0}'.format(count))
        if thread is None:
            thread = Thread(target=run, args=(a,b))
            thread.start()
        if count>=100:
            break

def test_threads():
    t1 = Thread(target=thread1_run)
    t1.start()
    t2 = Thread(target=thread2_run)
    t2.start()

def main():
    test_threads()

if __name__ == "__main__":
    main()