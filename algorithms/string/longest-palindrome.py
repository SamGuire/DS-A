def longest_palindrome_naive(s) :

    def is_palindrome(s,l,r) :
        while l < r :
            if s[l] != s[r] :
                return False
            l+=1
            r-=1
        return True

    longest = ""
    for i in range(len(s)) :
        for j in range(i,len(s)) :
            if is_palindrome(s,i,j) :
                longest = max(longest,s[i:j+1],key=len)
    
    return longest


def longest_palindrome_opt(s) :
    
    def expand_from_middle(s,mid1,mid2) :
        if s[mid1] != s[mid2] :
            return ""

        go_left_pt,go_right_pt = mid1,mid2
        while go_left_pt >= 0 and go_right_pt < len(s) and s[go_left_pt] == s[go_right_pt] :
            go_left_pt-=1
            go_right_pt+=1

        go_left_pt+=1
        go_right_pt-=1
        return s[go_left_pt:go_right_pt+1]
    
    longest = ""
    for i in range(len(s)-1) :
        ss_1,ss_2 = expand_from_middle(s,i,i),expand_from_middle(s,i,i+1)
        longest = max(longest,ss_1,ss_2,key=len)
    
    return longest


def main() :
    s = "racecar" 
    print(f"Longest palindrome of {s} is {longest_palindrome_naive(s)}")
    print(f"Longest palindrome of {s} is {longest_palindrome_opt(s)}")


if __name__ == "__main__":
    main()

