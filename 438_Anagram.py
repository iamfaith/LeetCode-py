import collections


# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m = collections.defaultdict(lambda: 0)
        for c in p:
            m[c] = m[c] + 1
        begin, end, count, ret = 0, 0, len(m), []
        while end < len(s):
            c = s[end]
            if m.__contains__(c):
                m[c] = m[c] - 1
                if m[c] == 0:
                    count -= 1
            end += 1

            while count == 0:
                c = s[begin]
                if m.__contains__(c):
                    m[c] = m[c] + 1
                    if m[c] > 0:
                        count += 1
                    if end - begin == len(p):
                        ret.append(begin)

                begin += 1
        print ret
        return ret


s = Solution()
s.findAnagrams("cbaebabacd", "abc")
