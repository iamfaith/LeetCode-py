class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p, output = 1, []
        for n in nums:
            output.append(p)
            p = p * n
        p = 1
        for i, n in reversed(list(enumerate(nums))):
            output[i] = output[i] * p
            p = p * n
        return output


s = Solution()
print s.productExceptSelf([1, 2, 3, 4])
