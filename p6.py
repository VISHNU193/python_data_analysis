class Shape:
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2
    
class Rect(Shape):
    def __init__(self,s1,s2):
        super().__init__(s1,s2)
    def calcArea(self):
        print("Area : ",self.s1*self.s2)
    def display(self):
        print("length : ",self.s1)
        print("breadth : ",self.s2)

class Triangle(Shape):
    def __init__(self,s1,s2):
        super().__init__(s1,s2)
    def calcArea(self):
        print("Area : ",self.s1*self.s2*0.5)
    def display(self):
        print("base : ",self.s1)
        print("height : ",self.s2)

s = Rect(10,20)
s.calcArea()
s.display()

t = Triangle(10,10)
t.calcArea()
t.display()
