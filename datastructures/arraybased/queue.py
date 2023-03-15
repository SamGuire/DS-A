class Queue :
    def __init__(self,capacity) -> None:
        self.queue = [0]*capacity
        self.MAX_CAPACITY = capacity
        self.front,self.back = -1,0
    def is_full(self) :
        return (self.front-self.back+1) >= self.MAX_CAPACITY
    def is_empty(self) :
        return (self.front-self.back+1) <= 0
    def enqueue(self,v) :
        if not self.is_full() :
            self.front += 1
            idx = self.front % self.MAX_CAPACITY
            self.queue[idx] = v
    def dequeue(self) :
        if not self.is_empty() :
            idx = self.back % self.MAX_CAPACITY
            v = self.queue[idx]
            self.back+=1
            return v
        else :
            return float('-inf')
    
    def first(self) :
        if not self.is_empty() :
            idx = self.back % self.MAX_CAPACITY
            v = self.queue[idx]
            return v
        else :
            return float('-inf')
    
    def __repr__(self) -> str:
        return str(self.queue)


def main() :
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(f'Front of the queue is {q.first()}')
    q.dequeue()
    q.dequeue()
    print(f'Front of the queue is {q.first()}')
    q.dequeue()
    q.dequeue()
    print(f'Front of the queue is {q.first()}')
    q.dequeue()
    print(f'Front of the queue is {q.first()}')

if __name__ == '__main__' :
    main()