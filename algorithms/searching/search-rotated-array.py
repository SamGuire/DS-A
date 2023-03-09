import random
def search_rotated_array(a,v) :
    n = len(a)
    l,r = 0,n-1
    while l < r :
        m = l+(r-l)//2
        if a[m] == v:
            return m
        elif a[l] <=  a[m] :
            if a[l] <= v < a[m] :
                r = m-1
            else :
                l = m+1
        else :
            if a[m] < v <= a[r] :
                l = m+1
            else :
                r = m-1
    return l

def rotate_array(a,k) :
    def reverse(a,i,j) :
        while i < j :
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1

    n = len(a)
    k%=n
    reverse(a,0,k-1)
    reverse(a,k,n-1)
    reverse(a,0,n-1)


def main() :
    min_v,max_v = 0,100
    a = [i for i in range(1,21)]
    a.sort()
    rotate_array(a,15)
    v = 15
    idx = search_rotated_array(a,v)
    print(f'v={v} in {a} ? {idx}')

if __name__ == '__main__' :
    main()