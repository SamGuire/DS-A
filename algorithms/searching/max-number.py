import random
def get_max(a) :
    n = len(a)
    if len(a) <= 0:
        return float('-inf')
    max_v = a[0]
    for i in range(1,n) :
        max_v = max(max_v,a[i])
    return max_v



def main() :
    min_v,max_v = -100,100
    a = [random.randint(min_v,max_v) for _ in range(20)]
    print(f'max value in {a} ? {get_max(a)}')

if __name__ == '__main__' :
    main()