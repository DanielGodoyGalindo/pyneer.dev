def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    output = []
    for interval in intervals:
        if len(output) == 0 or interval[0] > output[-1][1]:
            output.append(interval)
            print("Not mergin")
        else:
            output[-1][1] = max(output[-1][1], interval[1])
            print("Merging")
    return output


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
