class Solution(object):
    def firstUniqChar(self, str):
        """
        :type s: str
        :rtype: int
        """
        if str == '':
            return -1
        dict = {}
        for s in str:
            if s in dict:
                dict[s] = dict[s] + 1
            else:
                dict[s] = 1
        for i, s in enumerate(str):
            if dict[s] == 1:
                return i
        return -1

s = Solution()
print s.firstUniqChar('')
