class Stack:
    def __init__(self):
        self.top = -1
        self.st = list()
    def push(self,item):
        self.top = self.top + 1
        self.st.insert(self.top,item)
    def pop(self):
        item = self.st[self.top]
        del self.st[self.top]
        self.top = self.top - 1
        return item
    def display(self):
        print(self.st)

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = -1
        self.q=[]
    def enque(self,item):
        self.rear = self.rear + 1
        self.q.insert(self.rear,item)
    def deque(self):
        
        item = self.q[self.front]
        del self.q[self.front]
        self.front = self.front + 1
        return item
    def display(self):
        print(self.q)

print("Stack")
st = Stack()
st.push(20)
st.push(4567.90)
st.push("hello")
st.push(20)
st.push(4567.90)
st.push("hello")
st.pop()
st.display()


print("queue")
Q = Queue()
Q.enque(10)
Q.enque(40)
Q.enque(60)
Q.display()
print(Q.deque())
Q.display()
