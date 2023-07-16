# User function Template for python3


# Complete this function
def convertToWave(A, N):
    # Your code here
    for index in range(1, N if N % 2 == 1 else N + 1, 2):
        previous = A[index - 1]
        A[index - 1] = A[index]
        A[index] = previous


"""
#{
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():

    T=int(input())

    while(T>0):

        N=int(input())

        A=[int(x) for x in input().split()]
        convertToWave(A,N)
        for i in A:
            print(i,end=" ")

        print()

        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
"""
