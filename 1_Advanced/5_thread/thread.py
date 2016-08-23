"""Multi thread concept"""
import time,thread

def print_t(name,delay):
    while 1:
        time.sleep(delay)
        print name

#1st thread
thread.start_new_thread(print_t,("First Thread",1,))

#2nd thread
thread.start_new_thread(print_t,("Second Thread",2,))

time.sleep(4)
print "Mani"


while 1:
    pass
