# User function Template for python3
# import sys
# import io
# import atexit


def minimumPlatform(n, arr, dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    # code here
    # based on
    # https://practice.geeksforgeeks.org/viewSol.php?subId=
    # 977bb4a7a0e36b42e6248dc358e5d0f5&pid=701368&user=prachiagrawal7
    arr.sort()
    dep.sort()
    platforms = 1
    add_platform = 1
    arr_index = 1
    dep_index = 0
    while arr_index < n and dep_index < n:
        if arr[arr_index] <= dep[dep_index]:
            add_platform += 1
            arr_index += 1
        elif arr[arr_index] > dep[dep_index]:
            add_platform -= 1
            dep_index += 1
        if (add_platform > platforms):
            platforms = add_platform
    return platforms


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arrival = list(map(str, input().strip().split()))
        departure = list(map(str, input().strip().split()))
        print(minimumPlatform(n, arrival, departure))
# } Driver Code Ends
