from collections import deque


def get_combination_sum_2(target,numbers):
    def dfs(current_sum,target,idx,numbers,candidates,solutions) :
        if current_sum > target or idx >= len(numbers) :
            return
        elif current_sum == target :
            solutions.append(candidates[::])
            return
        else :
            for j in range(idx,len(numbers)) :
                if j == idx or numbers[j] != numbers[j-1] :
                    candidates.append(numbers[j])
                    dfs(current_sum+numbers[j],target,j+1,numbers,candidates,solutions)
                    candidates.pop()
    
    solutions = deque()
    numbers.sort()
    dfs(0,target,0,numbers,[],solutions)
    return solutions

def main() :
    target = 8
    numbers = [10,1,2,7,6,1,5]
    print(F'Combinations that add up to {target} using {numbers} is {get_combination_sum_2(target,numbers)}')

if __name__ == '__main__' :
    main()