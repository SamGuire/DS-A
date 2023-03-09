import random
def prev_number_sorted(a,v) :
    if a[0] > v :
        return -1
    n = len(a)
    l,r = 0,n-1
    while l < r :
        m = l+(r-l)//2+1
        if a[m] < v :
            l = m
        else :
            r = m-1
    return a[l]

def prev_number_unsorted(a,v) :
    prev_number = float('-inf')
    for num in a :
        if prev_number < num < v :
            prev_number= num
    return prev_number


def main() :
    min_v,max_v = -10,10
    a = [random.randint(min_v,max_v) for _ in range(10)]
    b = [random.randint(min_v,max_v) for _ in range(10)]
    a.sort()
    v = random.randint(min_v,max_v) 
    n1 = prev_number_sorted(a,v)
    n2 = prev_number_unsorted(b,v)
    print(f'prev numbe {v} {a} -> {n1}')
    print(f'prev number {v} {b} -> {n2}')


if __name__ == '__main__' :
    main()