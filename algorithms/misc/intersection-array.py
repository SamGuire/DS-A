from collections import Counter


def intersection_sorted(a,b) :
    a.sort()
    b.sort()
    intersection_of_array = []
    i = j = 0
    while i < len(a) and j < len(b) :
        if a[i] == b[j] :
            intersection_of_array.append(a[i])
            i+=1
            j+=1
        elif a[i] < b[j] :
            i+=1
        else :
            j+=1
    return intersection_of_array

def intersection_sorted_without_duplicates(a,b) :
    a.sort()
    b.sort()
    intersection_of_array = []
    i = j = 0
    while i < len(a) and j < len(b) :
        if a[i] == b[j] :
            if len(intersection_of_array) <=0 or intersection_of_array[-1] != a[i] :
                 intersection_of_array.append(a[i])
            i+=1
            j+=1
        elif a[i] < b[j] :
            i+=1
        else :
            j+=1
    return intersection_of_array

def intersection_unsorted(a,b) :
    if len(a) > len(b) :
        return intersection_unsorted(b,a)
    
    frequency = Counter(a)
    intersection_array = []
    for v in b :
        if v in frequency and frequency[v] > 0 :
            intersection_array.append(v)
            frequency[v]-=1
    return intersection_array





def main() :
    a = [1,1,1,3,4,4]
    b = [1,1,1,1,2,3,4,5,4,4]
    print(f"Intersection of {a} and {b} is {intersection_sorted(a,b)}")
    print(f"Intersection (no duplicates) of {a} and {b} is {intersection_sorted_without_duplicates(a,b)}")
    print(f"Intersection of {a} and {b} is {intersection_unsorted(a,b)}")


if __name__ == '__main__' :
    main()