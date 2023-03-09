import random
def search_min_rotated_array(a) :
    n = len(a)
    l,r = 0,n-1
    while l < r :
        m = l+(r-l)//2
        if a[m] > a[m+1] :
            return m+1
        elif a[m] < a[m-1] :
            return m
        elif a[l] < a[m] :
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
    a = [random.randint(min_v,max_v) for _ in range(10)]
    a.sort()
    rotate_array(a,8)
    idx_of_max = search_min_rotated_array(a)
    print(f'max in {a} ? {idx_of_max}')

if __name__ == '__main__' :
    main()