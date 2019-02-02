class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = len(s)
        dp = [[1 if x == y else 0 for x in range(count + 1)] for y in range(count + 1)]
        ri, rj, max = 0, 0, 0
        for i in range(count):
            for j in range(i + 1):
                if i != j:
                    if j + 1 <= i - 1 and dp[j + 1][i - 1] == 1 and s[i] == s[j]:
                        dp[j][i] = 1
                        if i - j + 1 > max:
                            ri, rj, max = i, j, i - j + 1
                    elif j + 1 == i and s[i] == s[j]:
                        dp[j][i] = 1
                        if i - j + 1 > max:
                            ri, rj, max = i, j, i - j + 1
        # print dp
        return s[rj: ri + 1]


s = Solution()
print s.longestPalindrome('aaaa')
# for i in range(5):
#     for j in range(i + 1):
#         print i, j
