class BankAccount:
    def __init__(self,name,accNum,bal,Acctype,addr):
        self.name = name
        self.accNum = accNum
        self.bal = bal
        self.Acctype = Acctype
        self.addr = addr
        
    def deposit(self,amt):
        self.bal += amt
        
    def withdraw(self,amt):
        if self.bal-amt > 0:
            self.bal -= amt
        else:
            print("Insufficient balance")
    
    def display(self):
        print(f"Name:{self.name},AccountNumber:{self.accNum},Balance:{self.bal},AccountType:{self.Acctype},Address:{self.addr}")
    
    
p1 = BankAccount("vishnu",123,10000,"regular","Bangalore")
p2 = BankAccount("krishna",12,10000,"regular","Bangalore")

p1.display()
p2.display()

p1.deposit(1500)
p1.display()

p2.withdraw(1000)
p2.display()
