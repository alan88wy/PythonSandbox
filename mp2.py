from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1
        
def main():
    a = Process(target=counter, args = (100000000000,))
    b = Process(target=counter, args = (100000000000,))
    a.start()
    b.start()
    a.join()
    b.join()
    
    print("Finished in ", time.perf_counter(), " seconds")
    
    
    
if __name__ == '__main__':
    main()