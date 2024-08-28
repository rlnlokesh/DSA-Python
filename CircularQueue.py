class CircularQueue:
    def __init__(self,size):

        self.size=size
        self.queue=[None]*size
        self.front=self.rear=-1

    def is_empty(self):
        return self.front==-1
    def is_full(self):
        return (self.rear+1)%self.size==self.front
    def enqueue(self,data):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        data = self.queue[self.front]

        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size

        return data


    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[self.front]
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        i=self.front
        while True:
            print(self.queue[i], end=" ")
            if i==self.rear:
                break
            i=(i+1)%self.size
        print()

    def find__index(self,data):
        i=self.front
        while (True):
            if self.queue[i]==data:
                break
            i=(i+1)%self.size
        print(i)
    def remove_at_index(self,index):
        if self.is_empty():
            print("Queue is empty")
            return
        if self.front == self.rear == 0:
            self.front = self.rear = -1
        else:
            i = index+1
            while True:
                self.queue[i] = self.queue[(i + 1) % self.size]
                i = (i + 1) % self.size
                if i == (self.rear + 1) % self.size:
                    break
            self.rear = (self.rear - 1) % self.size



if __name__ == '__main__':
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.display()
    cq.find__index(4)
    cq.dequeue()
    cq.display()
    cq.remove_at_index(2)
    cq.display()