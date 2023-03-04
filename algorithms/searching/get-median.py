import random
def get_median(a) :
    a.sort()
    return a[len(a)//2]



def main() :
    min_v,max_v = -100,100
    a = [random.randint(min_v,max_v) for _ in range(20)]
    a.sort()
    print(f'median value in {a} ? {get_median(a)}')

if __name__ == '__main__' :
    main()