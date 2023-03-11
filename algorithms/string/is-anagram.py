from collections import Counter


def is_anagram_simple(s,t) :
    if len(s) != len(t) :
        return False
    
    return Counter(s) == Counter(t)

def is_anagram_language_agnostic(s,t) :
    if len(s) != len(t) :
        return False
    
    dict_1,dict_2 = {},{}

    for c in s :
        if c not in dict_1 :
            dict_1[c] = 0
        dict_1[c]+=1
    
    for c in t :
        if c not in dict_2 :
            dict_2[c] = 0
        dict_2[c]+=1
    
    if len(dict_1) != len(dict_2) :
        return False
    else :
        for k in dict_1 :
            if k not in dict_2 or dict_1[k] != dict_2[k] :
                return False
        return True


def main() :
    s,t = 'aabbcc','ccaabb'
    print(f"is {s} an anagram of {t} ? {is_anagram_simple(s,t)}")
    print(f"is {s} an anagram of {t} ? {is_anagram_language_agnostic(s,t)}")

if __name__ == '__main__' :
    main()
    


    