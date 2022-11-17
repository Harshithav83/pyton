import time
print("Enter to start the timer")
while True:
    try:
        input()
        starttime=time.time()
        print("started")
        while True:
            print("Time elaspsed:",round(time.time()-starttime,0),'secs',end='\r')
            time.sleep(1)
    except keyboardInterrupt:
        print('stopped')
        endtime=time.time()
        print('totaltime:',round(endtime-starttime,2),'sec')
        break

