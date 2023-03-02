import random

"""
properties : O(n2) worst case, O(nlgn) average, inplace, not stable (does not keep relative order)
when to use : if memory is expensive but need efficient sorting.
"""
def quick_sort(a,l,r) :
    if l >= r :
        return

    rand_idx = random.randint(l,r)
    a[r],a[rand_idx] = a[rand_idx],a[r]

    i = l 
    for j in range(l,r) :
        if a[j] < a[r] :
            a[i],a[j] = a[j],a[i]
            i+=1
    
    a[r],a[i] = a[i],a[r]

    quick_sort(a,l,i-1)
    quick_sort(a,i+1,r)

def main() :
    print('quick sort')
    min_num,max_num = 0,100
    a = [random.randint(min_num,max_num) for _ in range(20)]
    print(f'Before sorting:  {a}')
    quick_sort(a,0,len(a)-1)
    print(f'After sorting {a}')

if __name__ == '__main__' :
    main()
    