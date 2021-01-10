#User function Template for python3

class Solution:
    def maximumWeight(self, n, edges, q, queries):
        # code here
        return [1]



'''
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())

        edges = [[0 for j in range(3)] for i in range(n-1)]
        for i in range(n-1):
            input_line = [int(x) for x in input().strip().split()]       
            for j in range (3):
                edges[i][j]=input_line[j]

        q = int(input())
        queries = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.maximumWeight(n, edges, q, queries)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends
'''
