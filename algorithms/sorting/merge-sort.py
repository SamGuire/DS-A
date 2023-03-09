import random

"""
properties : O(nlgn) every case, O(n) space, stable (keep relative order)
when to use : if memory is not expensive but need efficient sorting and keep relative order. also good for linked lists.
"""
def merge_sort(a,l,r) :
    if  l > r :
        return []
    if l == r :
        return [a[l]]

    m = l+(r-l)//2
    l_sorted = merge_sort(a,l,m)
    r_sorted = merge_sort(a,m+1,r)
    return merge(l_sorted,r_sorted)

def merge(a,b) :
    res = [0]*(len(a)+len(b))
    i = j = k = 0
    while i < len(a) and j < len(b) :
        if a[i] < b[j] :
            res[k] = a[i]
            i+=1
        else :
            res[k] = b[j]
            j+=1
        k+=1
    
    while i < len(a) :
        res[k] = a[i]
        i+=1
        k+=1
    
    while j < len(b) :
        res[k] = b[j]
        j+=1
        k+=1
    return res


def main() :
    print('merge sort')
    min_num,max_num = 0,100
    a = [random.randint(min_num,max_num) for _ in range(20)]
    print(f'Before sorting:  {a}')
    sorted_arr = merge_sort(a,0,len(a)-1)
    print(f'After sorting {sorted_arr}')

if __name__ == '__main__' :
    main()
    