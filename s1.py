import time
import sys
from sys import getsizeof

start = time.time()
class student:
    def __init__(self):
        self.item = []
    def isempty(self):
        return self.item == []
    def push(self,id,name,age):
        self.item.append([id,name,age])
    def pop(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
    def peek(self):
        return self.item[-1]
    def display(self):
        for i in self.item:
            print(i)
end = time.time()
print("program run time: ",end-start)
print("size of program in byts :",getsizeof(student))
s=student()
s.push(1,"prashanth",19)
s.push(2,"sachin",19)
s.push(3,"pavan",20)
s.display()
print("pop",s.pop())
print("peek",s.peek())
print("size",s.size())