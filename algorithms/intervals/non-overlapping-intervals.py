from collections import deque


def get_non_overlapping_intervals(intervals) :
    intervals.sort(key=lambda interval : interval[1])
    non_overlapping_intervals = deque()

    for interval in intervals :
        start,finish = interval 
        if len(non_overlapping_intervals) <= 0 or start >= non_overlapping_intervals[-1][1] :
            non_overlapping_intervals.append([start,finish])
    
    return non_overlapping_intervals

def main() :
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(f"If non overlapping intervals in  {intervals} is {get_non_overlapping_intervals(intervals)}")
    intervals = [[1,4],[4,5]]
    print(f"If non overlapping intervals in  {intervals} is {get_non_overlapping_intervals(intervals)}")


if __name__ == '__main__' :
    main()