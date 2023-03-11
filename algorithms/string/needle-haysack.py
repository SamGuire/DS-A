from collections import deque


def needle_haystack_naive(text,word) :
    for i in range(len(text)-len(word)) :
        found = True
        for j in range(len(word)) :
            if text[i+j] != word[j] :
                found = False
                break
        if found : return True
    return False


def needle_haystack_opt(text,word) :
    def generate_lps(pattern) :
        lps = [0] * len(pattern)
        
        len_of_prefix = 0
        for i in range(1,len(lps)) :

            while len_of_prefix and pattern[len_of_prefix] != pattern[i] :
                last_ch_matched = len_of_prefix-1
                len_of_prefix = lps[last_ch_matched]

            if pattern[len_of_prefix] == pattern[i] :
                len_of_prefix +=1
                lps[i] = len_of_prefix

        return lps

    lps = generate_lps(word)
    j = 0
    indices = deque()

    for i,ch in enumerate(text) :
        while j and word[j] != ch :
            last_ch_matched = j-1
            longest_prefix_thats_also_suffix = lps[last_ch_matched]
            j = longest_prefix_thats_also_suffix
        
        if word[j] == ch :
            j += 1
            if j == len(word) :
                indices.append(i-j+1)
                longest_prefix_thats_also_suffix = lps[-1]
                j = longest_prefix_thats_also_suffix
    
    return indices





def main() :
    text = 'abcabc'
    word = 'abc'
    print(f"Is {word} in the text ? {needle_haystack_opt(text,word)}")
    word = 'issam'
    print(f"Is {word} in the text ? {needle_haystack_opt(text,word)}")

if __name__ == '__main__' :
    main()