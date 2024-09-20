import threading
import time
def function1():
    print("Thread1 running")
    time.sleep(2)
    print("Thread1 ends")

def function2():
    print("Thread 2 running")
    print("Thread 2 ends")

t1 = threading.Thread(target=function1(), daemon=True)
t2 = threading.Thread(target=function2(), daemon=True)

t1.start()
t2.start()
print("Main thread execution")