# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, maxNum = len(nums), 0
        if count == 0:
            return 0
        elif count == 1:
            return nums[0]
        dp1 = [0 for x in range(count)]
        dp2 = [0 for x in range(count)]

        def cal_max(begin, end, nums, dp):
            for i in range(begin, end):
                if i > 1:
                    dp[i] = max(dp[begin:i - 1]) + nums[i]
                else:
                    dp[i] = nums[i]
            # print(dp)
            return max(dp)

        return max(cal_max(0, count - 1, nums[:count - 1], dp1), cal_max(0, count - 1, nums[1:], dp2))


s = Solution()
print(s.rob([1, 2, 3, 1]))
