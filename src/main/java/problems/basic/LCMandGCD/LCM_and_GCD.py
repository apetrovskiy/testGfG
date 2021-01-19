# User function Template for python3

class Solution:
    def lcmAndGcd(self, A, B):
        # code here
        return [self.lowest_common_multiple(A, B), self.greatest_common_divisor(A, B)]

    def greatest_common_divisor(self, A: int, B: int) -> int:
        while B != 0:
            remainder = A % B
            if remainder == 0:
                return B
            A = B
            B = remainder
        return A

    def lowest_common_multiple(self, A: int, B: int) -> int:
        gcm = self.greatest_common_divisor(A, B)
        return int(A / gcm * B)


'''
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends
'''
