from collections import deque


def merge_intervals(intervals) :
    intervals.sort(key=lambda interval : interval[0])
    merged_intervals = deque()

    for interval in intervals :
        start,finish = interval 
        if len(merged_intervals) <= 0 or start > merged_intervals[-1][1] :
            merged_intervals.append([start,finish])
        else :
            merged_intervals[-1] = [min(start,merged_intervals[-1][0]),max(finish,merged_intervals[-1][1])]
    
    return merged_intervals

def main() :
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(f"If we merged {intervals}, we get {merge_intervals(intervals)}")
    intervals = [[1,4],[4,5]]
    print(f"If we merged {intervals}, we get {merge_intervals(intervals)}")


if __name__ == '__main__' :
    main()