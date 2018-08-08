import multiprocessing

x = 0

def firstFunc():
    x+=1

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=firstFunc)
        p.start()
        p.join
