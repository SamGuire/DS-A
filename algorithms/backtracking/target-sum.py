from collections import deque


def get_number_of_sums(target,numbers):
    memo = {}
    def dfs(current_sum,target,idx,numbers) :
        if idx >= len(numbers):
            return 1 if current_sum == target else 0
        elif (current_sum,idx) in memo :
            return memo[(current_sum,idx)]
        else :
            memo[(current_sum,idx)] =  dfs(current_sum+numbers[idx],target,idx+1,numbers) + dfs(current_sum-numbers[idx],target,idx+1,numbers) 
            return memo[(current_sum,idx)]
        
    dfs(0,target,0,numbers)
    return memo[(0,0)]

def get_number_of_sums_knapsack(target,numbers) :
    dp = [[False for _ in range(target)] for _ in range(numbers)]

def main() :
    target = 3
    numbers = [1,1,1,1,1]
    print(F'number of sums for target={target} using {numbers} is {get_number_of_sums(target,numbers)}')

if __name__ == '__main__' :
    main()