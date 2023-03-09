import random

"""
properties : O(n2) worst case, inplace
when to use : good for small datasets and almost sorted datasets
"""
def insertion_sort(a) :
    n = len(a)
    i = 1
    while i < n :
        j = i
        while j >= 0 and a[j-1] > a[j] :
            a[j],a[j-1] = a[j-1],a[j]
            j-=1
        i+=1


def main() :
    print('insertion sort')
    min_num,max_num = 0,100
    a = [random.randint(min_num,max_num) for _ in range(20)]
    print(f'Before sorting:  {a}')
    insertion_sort(a)
    print(f'After sorting {a}')

if __name__ == '__main__' :
    main()
    