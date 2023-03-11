def unique_sort(a) :
    a.sort()
    unique_values = []
    for v in a :
        if len(unique_values) <= 0 or unique_values[-1] != v :
            unique_values.append(v)
    return unique_values

def unique_unsorted(a) :
    unique_values = set()
    for v in a :
        if v not in unique_values :
            unique_values.add(v)
    
    return list(unique_values)

def main() :
    a = [1,1,2,2,3,4,5,5,6]
    print(f"Unique values in {a} are {unique_sort(a)}")
    print(f"Unique values in {a} are {unique_unsorted(a)}")


if __name__ == '__main__' :
    main()