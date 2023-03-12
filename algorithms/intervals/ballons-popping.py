from collections import deque


def min_number_of_arrows(ballons) :
    ballons.sort(key=lambda interval : interval[1])
    non_overlapping_intervals = deque()

    for interval in ballons :
        start,finish = interval 
        if len(non_overlapping_intervals) <= 0 or start > non_overlapping_intervals[-1][1] :
            non_overlapping_intervals.append([start,finish])
    
    return len(non_overlapping_intervals)

def main() :
    ballons = [[1,3],[2,6],[8,10],[15,18]]
    print(f"you need {min_number_of_arrows(ballons)} arrows top pop  {ballons}")
    ballons = [[1,4],[4,5]]
    print(f"you need {min_number_of_arrows(ballons)} arrows top pop  {ballons}")


if __name__ == '__main__' :
    main()