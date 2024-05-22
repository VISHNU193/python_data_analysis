class Invoice:
    def __init__(self,items,p):
        self.items = items
        self.price = p
        self.tax =[]
        self.total = []
    def calcTax(self):
        
        for index,value in enumerate(self.items):
            if value == 1:
                self.tax.append(self.price[index]*0.05)
            elif value == 2:
                self.tax.append(self.price[index]*0.12)
            elif value == 3:
                self.tax.append(self.price[index]*0.18)
            elif value == 4:
                self.tax.append(self.price[index]*0.28)
        print("Cost of each item : ",self.price)
        print("Tax on each item : ",self.tax)
    def printInvoice(self):
        for i in range(len(self.tax)):
            self.total.append(self.tax[i]+self.price[i])
        print("Final price of items:",self.total)
        print("Total Amount :",sum(self.total))
        
items = [1,2,3,4,2,3,1]
price = [100,200,300,400,500,600,700]

i = Invoice(items,price)
i.calcTax()
i.printInvoice()
