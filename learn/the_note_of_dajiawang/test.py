__author__ = 'huajw'
#coding=utf-8

#!/usr/bin/env python
import subprocess
import threading
def ping(num):
        for b in range(1,256):
                if subprocess.call('ping -c1 -W 1 192.168.%s.%s > /dev/null' %(num,b)) == 0:
                        print '192.168.%s.%s is up'%(num,b)
                else:
                        print '192.168.%s.%s is down'%(num,b)



threads =[]
t=threading.Thread(target=ping,args=(16))
threads.append(t)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
