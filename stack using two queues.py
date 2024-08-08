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
        self.tempQ = self.q1
        self.q1 = self.q2
        self.q2 = self.tempQ
        return topEle

    def getSize(self):
        return self.currentSize

    def push(self, val):
        self.q1.put(val)
        self.currentSize += 1

    def pop(self):
        if not self.q1.empty():
            while self.q1.qsize() != 1:
                x = self.q1.get()
                self.q2.put(x)
            last = self.q1.get()
            self.currentSize -= 1
            self.tempQ = self.q1
            self.q1 = self.q2
            self.q2 = self.tempQ
        else:
            return

        

s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.pop()