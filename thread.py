import threading
import time
import signal

def timer():
    print()
    count = 0
    
    while True:
        if stop_event.is_set():
            break
            
        time.sleep(1)
        count += 1
        print("Logged in for ", count, " Seconds")
        
def handle_kb_interrupt(sig, frame):
    stop_event.set()
        
if __name__ == '__main__':
    stop_event = threading.Event()
    signal.signal(signal.SIGINT, handle_kb_interrupt)
    
    x = threading.Thread(target=timer,  daemon=True)

    # x.setDaemon(True)

    # print(x.isDaemon())

    x.start()
    x.join()
    
    answer = input("Do you want to exit ? ")