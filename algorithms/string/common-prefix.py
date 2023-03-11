def longest_common_prefix(list_of_strings) :
    n = len(list_of_strings)
    list_of_strings.sort()
    first_string,last_string = list_of_strings[0],list_of_strings[n-1]
    j = 0
    for i in range(len(first_string)):
        if last_string[j] != first_string[i] :
            return first_string[:i]
        j+=1
    return first_string

def main() :
    list_of_strings = ["flower","flow","flight"]
    print(f"Longest common prefix in {list_of_strings} is {longest_common_prefix(list_of_strings)}")
    list_of_strings = ["dog","racecar","car"]
    print(f"Longest common prefix in {list_of_strings} is {longest_common_prefix(list_of_strings)}")

if __name__ == '__main__' :
    main()