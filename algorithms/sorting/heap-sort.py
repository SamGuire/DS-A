import random
import sys
from datastructures.arraybased.heap import MinHeap

def heap_sort(a) :
    n = len(a)
    min_heap = MinHeap(n)
    sorted_v = [0]*n
    for i in range(n) :
        min_heap.insert_val(a[i])
    
    for i in range(n) :
        sorted_v[i] = min_heap.extract_min()
    
    return sorted_v




def main() :
    print('heap sort')
    min_num,max_num = 0,100
    a = [random.randint(min_num,max_num) for _ in range(20)]
    print(f'Before sorting:  {a}')
    a = heap_sort(a)
    print(f'After sorting {a}')

if __name__ == '__main__' :
    main()
    