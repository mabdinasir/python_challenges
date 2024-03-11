# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Example 1:

# Input: n = 3, k = 3
# Output: "213"
# Example 2:

# Input: n = 4, k = 9
# Output: "2314"

from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n+1)]
        res = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, factorial(n))
            res += nums.pop(index)
        return res

print(Solution().getPermutation(3, 3))
print(Solution().getPermutation(4, 9))