# User function Template for python3

class Solution:
    def minStep(self, H, U, D):
        # code here
        one_step_progress = U - D
        almost_height = H - U + 1
        steps_before_end = int(
            almost_height / one_step_progress) \
            if almost_height % one_step_progress == 0 \
            else int(almost_height / one_step_progress) + 1
        return steps_before_end + 1


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
