from collections import deque


def get_combination_sum(target,numbers):
    def dfs(current_sum,target,idx,numbers,candidates,solutions) :
        if current_sum > target or idx >= len(numbers) :
            return
        elif current_sum == target :
            solutions.append(candidates[::])
            return
        else :
            for j in range(idx,len(numbers)) :
                candidates.append(numbers[j])
                dfs(current_sum+numbers[j],target,j,numbers,candidates,solutions)
                candidates.pop()
    
    solutions = deque()
    dfs(0,target,0,numbers,[],solutions)
    return solutions

def main() :
    target = 7
    numbers = [2,3,6,7]
    print(F'Combinations that add up to {target} using {numbers} is {get_combination_sum(target,numbers)}')

if __name__ == '__main__' :
    main()