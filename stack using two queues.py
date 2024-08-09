from queue import Queue
  
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.currentSize = 0

    def top(self):
        if self.q1.empty():
            return -1
        while self.q1.qsize() != 1:
            x = self.q1.get()
            self.q2.put(x)
        topEle = self.q1.get()
        self.q2.put(topEle)
        self.q1,self.q2 = self.q2,self.q1
        return topEle

    def push(self, val):
        self.q1.put(val)

    def pop(self):
        if not self.q1.empty():
            while self.q1.qsize() != 1:
                x = self.q1.get()
                self.q2.put(x)
            last = self.q1.get()
            self.q1,self.q2 = self.q2,self.q1
            return last
        else:
            return 

    def is_empty(self):
        if self.q1.empty() and self.q2.empty():
            return True
        else:
            return False   

s=Stack()

print('Menu')
print('push <value>')
print('pop')
print('top')
print('exit')
 
while True:
    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'top':
        x=s.top()
        print("Top element is ",x)
    elif operation == 'exit':
        break
