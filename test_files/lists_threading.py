from threading import Thread
import time

x = 0

nums = []

def adding():
    x=0
    while True:
        nums.append(x)
        x += 1
        print nums

def checking(num):
    if num > 99:
        print 'yay', num
        time.sleep(5)

def Main():
    t1 = Thread(target=adding)
    t1.daemon = True
    t1.start()

    while True:
        try:
            currNum = nums[-1]
        except IndexError:
            currNum = 1

        checking(currNum)

if __name__ == '__main__':
    Main()
