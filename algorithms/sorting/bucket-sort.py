import random

"""
properties : O(n2) worst case (all elements same bucket), O(n+k) average case (bucket size tends toward O(1) size -> sorting is  basically 
constant time) 
when to use : good for datasets between 0.0 and 1.0 (not included) and uniformally distributed data between fixed rangeS
"""
def bucket_sort(a,num_of_buckets) :
    min_v,max_v = min(a),max(a)
    bucket_range = (max_v-min_v )// num_of_buckets
    buckets = []
    for _ in range(num_of_buckets) :
        buckets.append([])
    
    for v in a :
        buckets[(v-min_v)//(bucket_range+1)].append(v)
    
    for b in buckets :
        b.sort()
    
    print(buckets)
    
    k = 0
    for b in buckets :
        for v in b :
            a[k] = v
            k+=1




def main() :
    print('bucket sort')
    min_num,max_num = 0,100
    a = [random.randint(min_num,max_num) for _ in range(20)]
    print(f'Before sorting:  {a}')
    bucket_sort(a,5)
    print(f'After sorting {a}')

if __name__ == '__main__' :
    main()
    