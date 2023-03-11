def longest_ss_repeating_char(s) :
    if not s :
        return ""
    
    longest_ss = s[0]
    pos_cache = {s[0]:0}
    j = 0
    for i in range(1,len(s)) :
        if s[i] in pos_cache and pos_cache[s[i]] >= j:
            j = pos_cache[s[i]]+1
        pos_cache[s[i]] = i
        longest_ss = max(longest_ss,s[j:i+1],key=len)
    return longest_ss

def main() :
    s = "abccabcd"
    print(f"Longest ss with no repeating char in {s} is {longest_ss_repeating_char(s)}")

if __name__ == '__main__' :
    main()