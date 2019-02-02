class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        trans_dict = set([w for words in wordList for w in words])
        reach, dicts, distance, visited = {beginWord}, set(wordList), 1, set()
        # print trans_dict, reach, dicts
        while not reach.__contains__(endWord):
            to_add = set()
            for word in reach:
                if not visited.__contains__(word):
                    for i, w in enumerate(word):
                        for trans in trans_dict:
                            new_word = list(word)
                            new_word[i] = trans
                            new_word = ''.join(new_word)
                            if dicts.__contains__(new_word):
                                to_add.add(new_word)
                                dicts.remove(new_word)
                    visited.add(word)
            distance = distance + 1
            if len(to_add) == 0:
                return 0
            # print to_add
            reach = to_add
        return distance


s = Solution()
print s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
