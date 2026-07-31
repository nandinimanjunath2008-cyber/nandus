class queue:
    def __init__(self):
        self.item=[]
    def enqueue(self,item):
        self.item.append(item)
    def dequeue(self):
        if len(self.item)<1:
            return None
        return self.item.pop(0)
    def display(self):
        print(self.item)
    def size(self):
        return len(self.item)
q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print("elements in queue:")
q.display()
print("after removing elements:")
q.dequeue()
q.dequeue()
q.display()
print("size:",q.size())
print("hii")
