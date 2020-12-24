import threading
import time

semaphore = threading.BoundedSemaphore(value = 5)

def access(thread_num):
    print("{} is tring to access".format(thread_num))
    semaphore.acquire()
    print("{} was granted".format(thread_num))
    time.sleep(10)
    print("{} is now releasing".format(thread_num))
    semaphore.release()
for thread_num in range(1,11):
    t = threading.Thread(target = access, args = (thread_num,))
    t.start()
    time.sleep(1)
    