import math as Math
class Quad:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def findQuadraticRoots(self):
        D = self.b**2 - 4*self.a*self.c
        if D > 0:
            x1 = (-self.b+Math.sqrt(D))/(2*self.a)
            x2 = (-self.b-Math.sqrt(D))/(2*self.a)
            print(f"First root is {x1}")
            print(f"Second root is {x2}")
        elif D == 0 :
            x1 = (-self.b+Math.sqrt(D))/(2*self.a)
            x2 = (-self.b-Math.sqrt(D))/(2*self.a)
            print(f"First root is {x1}")
            print(f"Second root is {x2}")
        else :
            re = -self.b/(2*self.a)
            Im = Math.sqrt(Math.fabs(D))/(2*self.a)
            print(f"First root is {re} + i {Im}")
            print(f"First root is {re} - i {Im}")
eq = Quad(1,2,1)
eq.findQuadraticRoots()
