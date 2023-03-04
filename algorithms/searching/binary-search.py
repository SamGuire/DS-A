import random
def binary_search(a,v) :
    n = len(a)
    l,r = 0,n-1
    while l <= r :
        m = l+(r-l)//2
        if a[m] == v :
            return True
        elif a[m] > v :
            r = m-1
        else :
            l = m+1
    return False



def main() :
    min_v,max_v = -100,100
    a = [random.randint(min_v,max_v) for _ in range(20)]
    a.sort()
    v = random.randint(min_v,max_v)
    found = 'yes' if binary_search(a,v) else 'no'
    print(f'found v = {v} in {a} ? {found}')

if __name__ == '__main__' :
    main()