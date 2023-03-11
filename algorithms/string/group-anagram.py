def group_anagrams(list_of_strings) :
    def sorted_string(s) :
        return "".join(list(s))
    groups = {}
    for s in list_of_strings :
        group_key = sorted_string(s)
        if group_key not in groups :
            groups[group_key] = []
        groups[group_key].append(s)
    return groups

def main() :
    list_of_strings = ["eat","tea","tan","ate","nat","bat"]
    print(f"Anagram grousp for {list_of_strings}:\n\t{group_anagrams(list_of_strings)}")

if __name__ == "__main__" :
    main()