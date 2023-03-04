import random
def insert_position(a,v) :
    if a[0] >= v :
        return 0
    elif a[-1] < v :
        return len(a)
    else :
        n = len(a)
        l,r = 0,n-1
        while l < r :
            m = l+(r-l)//2
            if a[m] >= v :
                r = m
            else :
                l = m+1
        return l



def main() :
    min_v,max_v = -100,100
    a = [1,1,1,1]
    a.sort()
    v = 2
    idx = insert_position(a,v)
    print(f'v = {v} in {a} ? {idx}')

if __name__ == '__main__' :
    main()