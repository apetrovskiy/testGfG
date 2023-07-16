# User function Template for python3
class Solution:
    def smallestNumber(ob, S, D):
        # code here
        if S > D * 9 or S < 0:
            return -1
        minimum_remainder = 1
        number_of_digits = D
        result = []
        while S > 0 and number_of_digits > 0:
            current_item = 9 if (S - minimum_remainder) > 9 else S - minimum_remainder
            S -= current_item
            number_of_digits -= 1
            result.append(current_item if number_of_digits > 0 else S + current_item)
        result_value = 0
        for index in range(len(result) - 1, -1, -1):
            result_value += result[index] * 10 ** (index)
        return result_value


"""
#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):

        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends
"""
