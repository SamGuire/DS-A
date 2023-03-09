def get_majority_element(a) :
    if len(a) <= 0 :
        return -1
    n = len(a)
    majority_element = None
    vote_count = 0
    for v in a :
        if vote_count == 0 :
            majority_element = v
        vote_count += 1 if v == majority_element else -1
    
   ## Sanity check -> Must check if potential majority element has more than n/2 votes.
    count = 0
    for v in a :
        if v == majority_element :
            count+=1
    
    return majority_element if count > n//2  else None


def main() :
    a = [1,1,2,2,2,3,3,3,3,3,3]
    print(f'Majority element in {a} is {get_majority_element(a)}')


if __name__ == '__main__' :
    main()