class Employee:
    
    def __init__(self,empId,name,desig,experience,age):
        self.empId = empId
        self.name = name
        self.desig = desig
        self.exp = experience
        self.age = age
    def displayDetails(self):
        print(f"Name:{self.name},Id:{self.empId},Designation:{self.desig},Experince:{self.exp},Age:{self.age}")
    
    def addEmployee(self,empId,name,desig,experience,age):
        return Employee(empId,name,desig,experience,age)
    
    def calcSal(self,amt):
        if self.age < 30 and self.exp>5:
            print(f"Salary:{amt*1.5}")
        elif self.age<40 and self.age>5:
            print(f"Salary:{amt*1.75}")
        elif self.age<40 and self.age>10:
            print(f"Salary:{amt*2}")
        elif self.age<50 and self.age>20:
            print(f"Salary:{amt*2.25}")
        elif self.age<50 and self.age>25:
            print(f"Salary:{amt*2.5}")
        elif self.age<58 and self.age>30:
            print(f"Salary:{amt*3}")
            
e1 = Employee(1,"vishnu","juior developer",5,27)
e2 = Employee(2,"krisha","dev",3,25)

e3 = e1.addEmployee(2,"krisha","dev",3,25)

e1.displayDetails()
e2.displayDetails()
e3.displayDetails()

e1.calcSal(2000000)
e2.calcSal(1500000)
