class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        maxNum = max(nums)
        ret = -1
        idx = -1
        for i, n in enumerate(nums):
            if n == maxNum:
                continue
            else:
                if maxNum >> 1 >= n and ret < n:
                    ret = n
                    idx = i
        if ret != -1:
            for i, n in enumerate(nums):
                if n == maxNum:
                    return i
        return -1


s = Solution()
ret = s.dominantIndex([0, 0, 2, 3])
print(ret)
