import random
from collections import Counter
def most_frequent_using_counter(a) :
    most_common = Counter(a).most_common()[0]
    return most_common


def most_frequent(a) :
    frequencies  = {}
    for v in a :
        if v not in frequencies :
            frequencies[v] = 0
        frequencies[v]+=1
    
    most_common = (-1,-1)
    for v in frequencies :
        if frequencies[v] > most_common[1] :
            most_common = (v,frequencies[v])
    return most_common
def most_frequent_in_place(a) :
    if len(a) == 0 :
        return (-1,-1)
    a.sort()
    n= len(a)
    value,frequency = a[0],1
    most_common = (-1,-1)
    for i in range(1,n) :
        if a[i] == value :
            frequency+=1
        else :
            if frequency > most_common[1] :
                most_common = (value,frequency)
            value,frequency = a[i],1
    
    return most_common if most_common[1] > frequency else (value,frequency)

def main() :
    min_v,max_v = 0,5
    a = [random.randint(min_v,max_v) for _ in range(20)]
    print(f'most common in {a} ? {most_frequent_using_counter(a)}')
    print(f'most common in {a} ? {most_frequent(a)}')
    print(f'most common in {a} ? {most_frequent_in_place(a)}')

if __name__ == '__main__' :
    main()