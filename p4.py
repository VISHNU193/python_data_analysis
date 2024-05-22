import math 
class TimeClass():
    def __init__(self,h:int,m:int,s:int):
        self.s=s
        self.m=m
        self.h=h

    def displayTime(self):
        print(f"Time - {self.h}:{self.m}:{self.s}")
    def addTime(self,t1,t2):
        h = t1.h + t2.h
        m = t1.m + t2.m
        s = t1.s + t2.s
        print(f"Added time : {h}:{m}:{s}")
    def subTime(self,t1,t2):
        h = math.fabs(t1.h - t2.h)
        m = math.fabs(t1.m - t2.m)
        s = math.fabs(t1.s - t2.s)
        print(f"Subtraced time : {int(h)}:{int(m)}:{int(s)}")
    
    def countSec(self):
        print(f"Total seconds : ",(self.h*3600+self.m*60+self.s))

t1 = TimeClass(3,50,55)
t2 = TimeClass(4,5,8)

t1.displayTime()
t1.addTime(t1,t2)
t1.subTime(t1,t2)
t1.countSec()
