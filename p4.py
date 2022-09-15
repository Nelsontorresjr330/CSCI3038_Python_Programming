from multiprocessing.dummy import freeze_support
import sys, time, math, signal
import multiprocessing as mp

signal.alarm(120)

def rootroot(low,high,Q):
    count = 0
    for n in range(low,high+1):
        n = math.sqrt(n)
        n = math.sqrt(n)
        n = n % 1
        if (n > 0.93):
            count = count + 1

    Q.put(count)

if __name__ == "__main__" :
    freeze_support()
    print("cpu count: ", mp.cpu_count())

    processes = []
    Q = mp.Queue()
    cores = int(sys.argv[3])

    tasks = range(int(sys.argv[1]),(int(sys.argv[2])+1))
    jobs = len(tasks)

    chunks = int(jobs/cores)

    for task in range(cores):
        low = task * chunks + 1
        high = (task+1) * chunks + 1
        p = mp.Process(target=rootroot, args=(low,high,Q)) 
        processes.append(p)

    startTime = time.time()
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("%0.2f" % (time.time() - startTime))

    count = 0
    for p in processes:
        count = count + Q.get()

    print("Total: ", count)