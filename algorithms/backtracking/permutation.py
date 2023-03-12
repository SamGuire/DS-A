"""
                          [1,2,3]

      1,[2,3],               2,[1,3],                  3,[1,2]

1,2,[3], 1,3,[2]       2,1,[3], 2,3,[1]           3,1,[2], 3,2,[1]

1,2,3    1,3,2           2,1,3    2,3,1               3,2,1    3,2,1

IN GENERAL permutation based algo time complexity -> O(cost*(n*)n!), space complexity -> O(n*n!) + O(n) (space for permuation + recursion stack)
"""
from collections import Counter


def permutation(a) :
    def dfs(a,i,solutions) :
        if i >= len(a) :
            solutions.append(a[::])
            return
        for j in range(i,len(a)) :
            a[j],a[i] = a[i],a[j] 
            dfs(a,i+1,solutions)
            a[j],a[i] = a[i],a[j]

    all_permutation = []
    dfs(a,0,all_permutation)
    return all_permutation


def permutation_with_duplicates(a) :
    def dfs(counter,candidate,solutions) :
        if len(candidate) == len(a) :
            solutions.append(candidate[::])
            return
        for v in counter :
            if counter[v] > 0 :
                candidate.append(v)
                counter[v]-=1
                dfs(counter,candidate,solutions)
                candidate.pop()
                counter[v]+=1

    all_permutation = []
    counter = Counter(a)
    dfs(counter,[],all_permutation)
    return all_permutation

def main() :
    a = [i for i in range(1,4)]
    print(f'all permutation of {a}:\n{permutation(a)}')
    a =  [1,1,2]
    print(f'all permutation of {a}:\n{permutation_with_duplicates(a)}')

if __name__ == '__main__' :
    main()