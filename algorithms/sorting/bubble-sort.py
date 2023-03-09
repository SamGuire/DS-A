import random

"""
properties : O(n2) worst case, inplace, worst than insertion sort (more swaps)
when to use : good for small datasets and almost sorted datasets, 
"""
def bubble_sort(a) :
    n = len(a)
    for i in range(n) :
        is_sorted = True
        for j in range(n-1) :
            if a[j] > a[j+1] :
                a[j],a[j+1] = a[j+1],a[j]
                is_sorted = False
        if is_sorted :
            break



def main() :
    print('bubble sort')
    min_num,max_num = 0,100
    a = [random.randint(min_num,max_num) for _ in range(20)]
    print(f'Before sorting:  {a}')
    bubble_sort(a)
    print(f'After sorting {a}')

if __name__ == '__main__' :
    main()
    