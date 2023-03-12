from collections import deque


def insert_interval(intervals,new_interval) :
    intervals.sort(key=lambda interval : interval[0])
    left_to_new_interval,right_to_new_interval = deque(),deque()
    merged_interval = new_interval

    for interval in intervals :
        start,finish = interval 
        if finish < merged_interval[0] :
            left_to_new_interval.append([start,finish])
        elif start > merged_interval[1] :
            right_to_new_interval.append([start,finish])
        else :
            merged_interval = [min(start,merged_interval[0]),max(finish,merged_interval[1])]
    
    left_to_new_interval.append(merged_interval)
    left_to_new_interval.extend(right_to_new_interval)
    return left_to_new_interval

def main() :
    intervals = [[1,3],[6,9]]
    new_interval = [2,5]
    print(f"If we add {new_interval} to {intervals}, we get {insert_interval(intervals,new_interval)}")
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    print(f"If we add {new_interval} to {intervals}, we get {insert_interval(intervals,new_interval)}")


if __name__ == '__main__' :
    main()