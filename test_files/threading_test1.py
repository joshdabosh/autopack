from threading import Thread
from queue import Queue

funcResult = Queue.Queue()

def firstFunc():
    x=0
    while True:
        x += 1
        funcResult.put(x)

def secFunc():
    print('yay it worked')

def Main():
    t1 = Thread(target=firstFunc)
    t2 = Thread(target=secFunc)

    t1.start()
    print(t1)

    while t1 != 50:
        print('nope')

    secFunc.start()

if __name__ == '__main__':
    Main()
