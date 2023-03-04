
    
def rotate_array(a,k) :
    def reverse_array(a,i,j) :
        while i < j :
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1
        
    n = len(a)
    k%=n
    reverse_array(a,0,k-1)
    reverse_array(a,k,n-1)
    reverse_array(a,0,n-1)



def main() :
    a = [i for i in range(1,11)]
    k = 3
    print(f'before -> {a}')
    rotate_array(a,k)
    print(f'rotated by {k} -> {a}')


if __name__ == '__main__' :
    main()