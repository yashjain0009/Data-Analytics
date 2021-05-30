import threading
import time


def print_time(delay):
    count = 0
    while count < 1:
        time.sleep(delay)
        count += 1
        print(" %s" % (time.ctime(time.time())))


def thread(threadName, delay, element):
    count = 0
    while count < 1:
        time.sleep(delay)
        count += 1
        print('{} is executing: {}'.format(threadName, element), end=" ")
        print_time(0)


def schedule():
    x = input("Enter Schedule:")
    y = x.split()
    for i in range(len(y)):
        if i != 0:
            temp = y[i - 1]
        else:
            temp = y[i]
        if 'r1x' in y[i] and 'w2x' in temp or 'w1x' in y[i] and 'r2x' in temp or 'w1x' in y[i] and 'w2x' in temp:
            print('Conflict')
            delay = 6
            thread("Thread1", delay, y[i])
        elif 'r1x' in y[i] and 'r2y' in temp or 'w1x' in y[i] and 'r2y' in temp or temp == y[i]:
            delay = 0
            thread("Thread1", delay, y[i])
        elif 'r2x' in y[i] and 'w1x' in temp or 'w2x' in y[i] and 'r1x' in temp or temp == y[i] or 'w2x' in y[i] and 'w1x' in temp:
            delay = 6
            print('Conflict')
            thread("Thread2", delay, y[i])
        else:
            delay = 0
            thread("Thread2", delay, y[i])


def thread_task(lock):
    lock.acquire()
    schedule()
    lock.release()


def main():
    # creating a lock
    lock = threading.Lock()

    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
