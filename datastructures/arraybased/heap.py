class MinHeap :
    def __init__(self,capacity) -> None:
        self.min_heap = [float('inf')]*capacity
        self.MAX_CAPACITY = capacity
        self.size = 0
    
    def parent(self,i) :
        return (i-1)//2
    
    def left_child(self,i) :
        return 2*i+1
    def right_child(self,i) :
        return 2*i+2
    
    def bubble_down(self,i) :
        if i < 0 or i >= self.MAX_CAPACITY :
            return
        min_idx = i
        l_c,r_c = self.left_child(i),self.right_child(i)
        if l_c < self.MAX_CAPACITY and self.min_heap[min_idx] > self.min_heap[l_c] :
            min_idx = l_c
        if r_c < self.MAX_CAPACITY and  self.min_heap[min_idx] > self.min_heap[r_c] :
            min_idx = r_c
        if min_idx != i :
            self.min_heap[i],self.min_heap[min_idx] = self.min_heap[min_idx],self.min_heap[i]
            self.bubble_down(min_idx)

    def bubble_up(self,i) :
        p = self.parent(i)
        if p >= 0 and self.min_heap[i] < self.min_heap[p] :
            self.min_heap[i],self.min_heap[p] = self.min_heap[p],self.min_heap[i]
            self.bubble_up(p)
        

    def get_min(self) :
        if not self.is_empty() :
            return self.min_heap[0]
        else :
            return float('-inf')

    def extract_min(self) :
        if not self.is_empty() :
            min_v = self.min_heap[0]
            self.min_heap[0],self.min_heap[self.size-1] = self.min_heap[self.size-1],self.min_heap[0]
            self.min_heap[self.size-1] = float('inf')
            self.size-=1
            self.bubble_down(0)
            return min_v
        else :
            return float('inf')

    def insert_val(self,v) :
        if not self.is_full() :
            self.size+=1
            self.min_heap[self.size-1] = v 
            self.bubble_up(self.size-1)

    def is_empty(self) :
        return self.size <= 0 
    
    def is_full(self) :
        return self.size >= self.MAX_CAPACITY

def main() :
    min_heap = MinHeap(5)
    min_heap.insert_val(1)
    min_heap.insert_val(2)
    min_heap.insert_val(3)
    min_heap.insert_val(-1)
    print(f"Min in minheap is {min_heap.get_min()}")
    min_heap.insert_val(10)
    min_heap.insert_val(11)
    sorted_val = []
    print(f"Min in minheap is {min_heap.get_min()}")
    for i in range(6) :
        sorted_val.append(min_heap.extract_min())
    print(f"Sorted vals is {sorted_val}")


if __name__ == '__main__' :
    main()