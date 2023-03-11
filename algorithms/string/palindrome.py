def is_palindrome(s) :
    n = len(s)
    l,r = 0,n-1
    while l < r :
        if s[l] != s[r] :
            return False
        l+=1
        r-=1
    return True

def main() :
    s = "racecar"
    print(f"is {s} a palindrome ? {is_palindrome(s)}")
    s = "Issamydobey"
    print(f"is {s} a palindrome ? {is_palindrome(s)}")
    s = ""
    print(f"is {s} a palindrome ? {is_palindrome(s)}")

if __name__ == '__main__' :
    main()