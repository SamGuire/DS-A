class Stack :
    def __init__(self,capacity) -> None:
        self.stack = [0]*capacity
        self.MAX_CAPACITY = capacity
        self.front,self.back = -1,0
    def is_full(self) :
        return (self.front-self.back+1) >= self.MAX_CAPACITY
    def is_empty(self) :
        return (self.front-self.back+1) <= 0
    def push(self,v) :
        if not self.is_full() :
            self.front += 1
            idx = self.front % self.MAX_CAPACITY
            self.stack[idx] = v
    def pop(self) :
        if not self.is_empty() :
            idx = self.front % self.MAX_CAPACITY
            v = self.stack[idx]
            self.front-=1
            return v
        else :
            return float('-inf')
    
    def peek(self) :
        if not self.is_empty() :
            idx = self.front % self.MAX_CAPACITY
            v = self.stack[idx]
            return v
        else :
            return float('-inf')
    
    def __repr__(self) -> str:
        return str(self.stack)



def main() :
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    print(s)
    print(f'Top of the stack is {s.peek()}')
    s.pop()
    s.pop()
    print(f'Top of the stack is {s.peek()}')
    s.pop()
    s.pop()
    s.pop()
    print(f'Top of the stack is {s.peek()}')


if __name__ == '__main__' :
    main()