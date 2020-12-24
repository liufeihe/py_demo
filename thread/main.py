from threading import Thread,Timer
from time import sleep

time_count = 0

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

def main():
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

if __name__ == "__main__":
    main()