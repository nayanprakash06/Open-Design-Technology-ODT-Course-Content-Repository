import time
#Using time.time()
t1 = time.time()
print("Time t1 recorded @ :",t1)
time.sleep(5)
t2 = time.time()
print("Time t2 recorded @ :",t2)
t = t2 - t1
print("Time interval between t1 & t2 in :",t,"seconds")

#Using time.ticks_ms()
ti1 = time.ticks_ms()
print("Time t1 recorded @ :",ti1)
time.sleep(5)
ti2 = time.ticks_ms()
print("Time t2 recorded @ :",ti2)
ti = time.ticks_diff(ti2,ti1) #using time_diff is better than mathematical subtraction beacuse time_diff considers time reset
print("Time interval between ti1 & ti2 :",ti,"milliseconds")

#Using time.ticks_us()
tu1 = time.ticks_us()
print("Time tu1 recorded @ :",tu1)
time.sleep(5)
tu2 = time.ticks_us()
print("Time tu2 recorded @ :",tu2)
tu = time.ticks_diff(tu2,tu1) #using time_diff is better than mathematical subtraction beacuse time_diff considers time reset
print("Time interval between ti1 & ti2 :",tu,"microseconds")



