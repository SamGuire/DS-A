def palindrome_partition(s) :

    def is_palindrome(s,l,r) :
        while l < r :
            if s[l] != s[r] :
                return False
            l+=1
            r-=1
        return True
    
    def dfs(s,i,candidates,solutions) :
        if i >= len(s) :
            solutions.append(candidates[::])
            return
        for j in range(i,len(s)) :
            if is_palindrome(s,i,j) :
                dfs(s,j+1,candidates+[s[i:j+1]],solutions)
    
    solutions = []
    dfs(s,0,[],solutions)
    return solutions

def main() :
    s = "aaaa"
    print(f"{s} can be partition as {palindrome_partition(s)}")

if __name__ == '__main__' :
    main()

