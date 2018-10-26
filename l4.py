class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = '$'

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def f(node, word):
            if len(word) == 0:
                if node.get('$', '') == '$':
                    return True
                else:
                    return False
            elif len(word) > 0 and node == '$':
                return False
            begin = word[0]
            if begin == '.':
                ret = False
                for n in node:
                    if node[n] == '$':
                        continue
                    ret = f(node[n], word[1:])
                    if ret:
                        break
                return ret
            else:
                snode = node.get(begin, '$')
                if snode == '$':
                    return False
                else:
                    return f(snode, word[1:])

        return f(self.root, word)


if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("at")
    # obj.addWord("and")
    # obj.addWord("an")
    # obj.addWord("add")

    print(obj.search("a"))
