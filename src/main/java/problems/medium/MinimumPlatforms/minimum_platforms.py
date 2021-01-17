# User function Template for python3
from typing import List


def convert(time: str) -> List[int]:
    return [int(time[:2]), int(time[2:])]


def is_later(period1: List[int], period2: List[int]) -> bool:
    return period1[0] > period2[0] or (period1[0] == period2[0] and period1[1] > period2[1])


def is_earlier(period1: List[int], period2: List[int]) -> bool:
    return period1[0] < period2[0] or (period1[0] == period2[0] and period1[1] < period2[1])


def is_time_in(interval: List[List[int]], time: List[int]) -> bool:
    if len(interval) == 0:
        return False
    return is_later(time, interval[0]) and is_earlier(time, interval[1])


def is_interval_in(interval: List[List[int]], interval_to_check: List[List[int]]) -> bool:
    return is_time_in(interval, interval_to_check[0]) or is_time_in(interval, interval_to_check[1])


def is_interval_in_schedule(schedule: List[List[List[int]]], interval_to_check: List[List[int]]) -> bool:
    if len(schedule) == 0:
        return False
    # result = [True for x in schedule if is_interval_in(x, interval_to_check)]
    # return len(result) > 0
    return sum((1 for x in schedule if is_interval_in(x, interval_to_check))) > 0


def minimumPlatformSlow(n, arr, dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    # code here
    # arrivals = [convert(x) for x in arr]
    # departures = [convert(x) for x in dep]
    # platform_times: List[List[int]] = list(zip(arrivals, departures))
    platform_times = list(zip((convert(x) for x in arr), (convert(x) for x in dep)))
    platforms: List[List[List[int]]] = [[]]
    for time in platform_times:
        time_inserted_into_schedule = False
        for platform in platforms:
            if not is_interval_in_schedule(platform, time):
                platform.append(time)
                time_inserted_into_schedule = True
                break
        if not time_inserted_into_schedule:
            platforms.append([time])
    return len(platforms)


'''
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(str,input().strip().split()))
        departure = list(map(str,input().strip().split()))
        print(minimumPlatform(n,arrival,departure))
# } Driver Code Ends
'''
