# Given a list of 24-hour clock time points in "HH:MM" format,
# return the minimum minutes difference between any two time-points in the list.

def findMinDifference(timePoints):
    time_list = []
    for time_point in timePoints:
        hours, minutes = time_point.split(':')
        time_list.append(int(hours) * 60 + int(minutes))
    time_list.sort()
    diff = float('inf')
    for i, time in enumerate(time_list):
        if i == len(time_list) - 1:
            diff = min(diff, (1440 - time + time_list[0]))
        else:
            diff = min(diff, (time_list[i + 1] - time))
    return diff

if __name__ == '__main__':

    print(findMinDifference(["23:59", "00:01", "02:00"]))