#User function Template for python3

class Solution:
    def minStep(self, H, U, D):
        # code here
        one_step_progress = U - D
        steps_before_end = int((H - U) / one_step_progress)
        return steps_before_end + 2


'''
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        H, U, D = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.minStep(H, U, D))
# } Driver Code Ends
'''
