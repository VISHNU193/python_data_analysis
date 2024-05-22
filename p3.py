import random as r
class FourthSem:
    def __init__(self,rNum,t1,t2,t3):
        self.rNum = rNum
        self.t1=t1
        self.t2=t2
        self.t3= t3
        
    def classAvg(self):
        t1Avg = sum(self.t1)/len(self.t1)
        t2Avg = sum(self.t2)/len(self.t2)
        t3Avg = sum(self.t3)/len(self.t3)
        print(f"Avergage : sub1={t1Avg},sub2={t2Avg},sub3={t3Avg}")
    def studAvg(self):
        studAvg = []
        for i in range(20):
            studAvg.append((self.t1[i]+self.t2[i]+self.t3[i])/3)
        print(studAvg)
    
    def maxMin5(self):
        t1 = self.t1.copy()
        t2 = self.t2.copy()
        t3 = self.t3.copy()
        
        t1.sort()
        t2.sort()
        t3.sort()
        
        print(f"test1 :max5={t1[-5:]},min5:{t1[:5]}")
        print(f"test1 :max5={t2[-5:]},min5:{t2[:5]}")
        print(f"test1 :max5={t3[-5:]},min5:{t3[:5]}")
rno = [i for i in range(1,21)]
l1 = [r.randint(0,100) for _ in range(20)]
l2 = [r.randint(0,100) for _ in range(20)]
l3 = [r.randint(0,100) for _ in range(20)]
sem = FourthSem(rno,l1,l2,l3)
sem.classAvg()
sem.studAvg()
sem.maxMin5()
