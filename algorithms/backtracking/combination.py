from collections import deque


def combination_without_duplicates(a) :
    def dfs(a,i,candidates,solutions) :
        solutions.append(list(candidates)[::])
        for j in range(i,len(a)) :
            candidates.append(a[j])
            dfs(a,j+1,candidates,solutions)
            candidates.pop()
    
    solutions = deque()
    dfs(a,0,deque(),solutions)
    return solutions

def combination_with_duplicates(a) :
    def dfs(a,i,candidates,solutions) :
        solutions.append(list(candidates)[::])
        for j in range(i,len(a)) :
            if (j == i or a[j] != a[j-1]) :
                candidates.append(a[j])
                dfs(a,j+1,candidates,solutions)
                candidates.pop()
    
    a.sort()
    solutions =deque()
    dfs(a,0,deque(),solutions)
    return solutions

def main() :
    a = [i for i in range(1,4)]
    b = [1,2,2,3,3]
    print(f'all comb of {a} -> {combination_without_duplicates(a)}')
    print(f'all comb of {b} -> {combination_with_duplicates(b)}')

if __name__ == '__main__' :
    main()