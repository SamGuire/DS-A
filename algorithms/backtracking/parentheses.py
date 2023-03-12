from collections import deque


def get_valid_parentheses(k) :
    def dfs(n,o_paren,c_paren,candidate,solutions) :
        if o_paren > n or c_paren > n or c_paren > o_paren:
            return
        elif o_paren == c_paren == n :
            solutions.append(candidate)
            return
        else :
            dfs(n,o_paren,c_paren+1,candidate+')',solutions)
            dfs(n,o_paren+1,c_paren,candidate+'(',solutions)
        
    solutions = deque()
    dfs(k,0,0,"",solutions)
    return solutions


def main() :
    k = 2
    print(F'Valid strings for {k} parentheses is {get_valid_parentheses(k)}')
    k = 3
    print(F'Valid strings for {k} parentheses is {get_valid_parentheses(k)}')

if __name__ == '__main__' :
    main()