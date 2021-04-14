from collections import Counter


def frequencycount(A, N):
    # code here
    counter = Counter(A)
    for index in range(1, N + 1):
        A[index - 1] = counter[index]


'''
#{
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
    T=int(input())
    while(T>0):
        N=int(input())
        A=[int(x) for x in input().strip().split()]
        frequencycount(A,N)
        for i in range (len (A)):
            print(A[i], end=" ")
        print()
        T-=1



# } Driver Code Ends
'''
