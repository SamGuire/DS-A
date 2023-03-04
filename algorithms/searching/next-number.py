import random
def next_number_sorted(a,v) :
    if a[-1] < v :
        return -1
    n = len(a)
    l,r = 0,n-1
    while l < r :
        m = l+(r-l)//2
        if a[m] <= v :
            l = m+1
        else :
            r = m
    return a[l]

def next_number_unsorted(a,v) :
    next_biggest = float('inf')
    for num in a :
        if v < num < next_biggest :
            next_biggest = num
    return next_biggest


def main() :
    min_v,max_v = -10,10
    a = [random.randint(min_v,max_v) for _ in range(10)]
    b = [random.randint(min_v,max_v) for _ in range(10)]
    a.sort()
    v = random.randint(min_v,max_v) 
    n1 = next_number_sorted(a,v)
    n2 = next_number_unsorted(b,v)
    print(f'next biggest {v} {a} -> {n1}')
    print(f'next biggest {v} {b} -> {n2}')


if __name__ == '__main__' :
    main()