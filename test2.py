class Solution:

    def buildTrie(self, words):
        # tmp = []
        # for word in words:
        #     tmp.extend([word[:i] for i, w in enumerate(word) if i > 0])
        #     tmp.append(word)

        dictionary = {}
        for word in words:
            d = dictionary
            for char in word:
                if char not in d:
                    d[char] = {}
                d = d[char]
            d[1] = True
        return dictionary
        # return set(tmp)

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row, col = len(board), len(board[0])
        start = [w[0] for w in words]
        visited = [[0 for x in range(col)] for y in range(row)]
        trie = self.buildTrie(words)

        def DFS(board, words, i, j, row, col, ret, tmp, visited, trie):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] not in trie:
                return
            if visited[i][j] == 1:
                return
            tmp += (board[i][j])
            if tmp in words:
                ret.add(tmp)
            trie = trie[board[i][j]]
            visited[i][j] = 1
            DFS(board, words, i + 1, j, row, col, ret, tmp, visited, trie)
            DFS(board, words, i - 1, j, row, col, ret, tmp, visited, trie)
            DFS(board, words, i, j + 1, row, col, ret, tmp, visited, trie)
            DFS(board, words, i, j - 1, row, col, ret, tmp, visited, trie)
            visited[i][j] = 0

        ret = set()
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] in start:
                    tmp = ""
                    DFS(board, words, i, j, row, col, ret, tmp, visited, trie)

        print(visited)
        return list(ret)


s = Solution()
ret = s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
["oath","pea","eat","rain"])
print(ret)
