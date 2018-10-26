class WordDictionary:
    def __init__(self):
        self.map = {}

    def addWord(self, word):
        k = len(word)
        if self.map.__contains__(k):
            self.map.get(k).add(word)
        else:
            self.map.setdefault(k, set([word]))

    def search(self, word):
        k = len(word)
        if self.map.__contains__(k):
            ls = list(self.map.get(k))

            if word in ls:
                return True
            for i, w in enumerate(word):
                if w == '.':
                    continue
                ls = [words for words in ls if words[i] == w]
                if not ls:
                    return False
            return True

        else:
            return False


            # for compare_word in ls:
            #     for i, w in enumerate(compare_word):
            #         if word[i] == '.':
            #             if i == k - 1:
            #                 return True
            #             else:
            #                 continue
            #         elif word[i] != w:
            #             break
            #         elif i == k - 1:
            #             return True
            # return False


class WordFilter:
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.map = {}
        self.words = words[:]
        self.len = len(words)
        words.reverse()
        for index, word in enumerate(words):
            newStr = ''
            for i, w in enumerate(word):
                if i == 10:
                    break
                newStr = newStr + w
                self.map.setdefault("^" + newStr, self.len - 1 - index)
            newStr = ''
            for k, w in enumerate(reversed(word)):
                if k == 10:
                    break
                newStr = w + newStr
                self.map.setdefault("$" + newStr, self.len - 1 - index)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        # print(self.map)
        if prefix == "" and suffix == "":
            return self.len - 1
        elif prefix == "":
            return self.map.get("$" + suffix, -1)
        elif suffix == "":
            return self.map.get("^" + prefix, -1)
        pre = self.map.get("^" + prefix, -1)
        suf = self.map.get("$" + suffix, -1)
        if pre == suf:
            return self.map.get("^" + prefix, -1)
        else:
            if pre < suf:
                pre, suf = suf, pre

            if self.words[pre].startswith(prefix) and \
                    self.words[pre].endswith(suffix):
                return pre
            elif self.words[suf].startswith(prefix) and \
                    self.words[suf].endswith(suffix):
                return suf
        return -1


if __name__ == '__main__':
    obj = WordFilter(
        ["babbabbaab", "babaabbaba", "bbbbabbaaa", "baaaaababb", "aaabbababa", "babbbbbaab", "bbbbaabaaa", "abaababbab",
         "abbbaabaab", "babbabbbba", "aaaaabbaaa", "aababbabbb", "abbbbababb", "abbaabbbbb", "baababbbab", "bbababbaaa",
         "bbbbaaabaa", "aabbabbbba", "baabbabbab", "abbbbaaaba", "aabbababab", "ababbbbaba", "bbbabbbaaa", "abbaabaaba",
         "aabbbaaaab", "aabbbbabab", "aabaaabbab", "baaabbbbbb", "abbaaabbbb", "abaaaababa", "aabbbababa", "babaababab",
         "aaabaaaaab", "aaabaabaab", "aaaaababba", "bbaaaabaaa", "bbabbaaabb", "bbbbabaaaa", "aaabaaaaba", "bbbbbaaaba",
         "aababbaaab", "bbaaaabbaa", "bbbabbabab", "aaababaaba", "bbbbabbbaa", "babaabbabb", "abbabbbbbb", "aabbababaa",
         "bbaaabbbba", "aabbaabbab", "bbabaaaaba", "ababaabbaa", "abbaabbabb", "bbaabbbabb", "abbbbbabaa", "baababaaab",
         "bbbaaaaaaa", "abbaabaaaa", "aabababaaa", "ababababba", "aabbabaaba", "babaabaaba", "baabbaabaa", "baaabaabaa",
         "abbabbabab", "baaaaaaaaa", "aaabbabbba", "baabaabaab", "aaababbaab", "bbbaabbbaa", "baababaabb", "aababaaaba",
         "bbaabbbaba", "ababababab", "aabaabbabb", "bbbbbbbbba", "ababbababb", "baabababba", "aabbbaaaba", "aaaabababa",
         "abaabaabab", "abbbbbbabb", "bbabaaaaab", "bababaaaaa", "abbbaaaaaa", "aaaabbabaa", "aaabaaaabb", "aaabaabbba",
         "ababbaabab", "bababaaaba", "ababababbb", "bbabbbabba", "aabbabbabb", "babaaaaaab", "aababababa", "abaabbaabb",
         "bbabbbaaba", "aabbaaaaba", "aabbabbaba", "abbabbbabb", "abbbbabbba", "baabaabaaa", "aaaababbba", "aabaaaaaaa",
         "bbabaaaaaa", "aaaaababab", "baababbaaa", "abbaaabbaa", "bbbbbaabaa", "abbbabaaab", "babaaababb", "abababaabb",
         "aababbabab", "abbbaabbbb", "abbbbbaaba", "babbbabbba", "abbabbbaaa", "bbbaaaaaab", "baabbbbbab", "bbbbbaabab",
         "aaabbabbbb", "aabaababbb", "abaabbabbb", "baabaaabab", "babbaaaabb", "baaaaabbaa", "abbabaabbb", "babbabbbaa",
         "abaaabbbab", "bbaabbaaaa", "bababbaabb", "abaaaababb", "bbaababbbb", "ababbaaaab", "babaabaaaa", "bababababa",
         "abbababbaa", "aaabbaabbb", "abbabbabbb", "abbbbbaabb", "aaaaaabaaa", "aaaababaab", "ababaaaaab", "bbabababab",
         "bbaaabaaab", "aaaabaabaa", "baabaabbab", "aaababbaaa", "babababbab", "bbaabbbbbb", "baababbbaa", "abaaaaabab",
         "bbbbababba", "baabbbbbbb", "abaabbbaba", "aaababaabb", "aaabbbabba", "aaaaabbbbb", "aabaabbbba", "bbaaaabbbb",
         "bbbaabbbab", "baabbbaaaa", "bbbabbbabb", "baabbaabbb", "aaaaaababb", "abbbaaaaba", "abbbbbbaba", "aaabbaaaba",
         "bbaaaaabba", "bbabbbbbba", "abaaaaabbb", "bbabbabbba", "aabbaaaabb", "bbbaabbaba", "abbbbbbbbb", "bbbababbab",
         "aabbbbbbbb", "babbbabaaa", "bbabbabbbb", "aabaabbbbb", "bbaabaabba", "aababbabaa", "bbaabaaabb", "ababbaabbb",
         "abaabbabaa", "babbbabbbb", "abbaaabbba", "aaaaaabbaa", "aaababbbba", "aababbabba", "ababbbbbaa", "baabababab",
         "bbabaaabaa", "baabaaabbb", "abbbabaabb", "ababbbabab", "ababaabbab", "bbbaaaabbb", "baaaabbbba", "ababbbaaab",
         "baaabbbbaa", "baabababbb", "abababbbab", "babaabbaaa", "baababbaba", "bbbbababab", "baaabababa", "baabaabbba",
         "bbbbabaabb", "bbbbabbbbb", "bbaabbaabb", "bbaababaab", "aaaababbbb", "bbaabbbbba", "bbbbbbaaaa", "aaaabbbbbb",
         "babaaabaaa", "baaababbaa", "ababbbbbba", "aabaaaaaba", "bababbbaba", "aababaabab", "ababbaaaaa", "bbaabbabab",
         "bbabbbaaaa", "aabbabaaaa", "aabaababba", "bbbbbabbab", "abaaaaabaa", "abbbabbbaa", "baaabababb", "abaaaabaab",
         "aabaaabbbb", "bbbbabbaba", "bbaaaaabbb", "abbbbbabbb", "babbabaaba", "abbaaaabab", "babbaaaaaa", "abbaabbaba",
         "bbaaababbb", "ababaaabaa", "babbbaaaaa", "bbbaabbabb", "aaabbabbab", "baabbabaab", "baaabbaaaa", "bbabbbbaab",
         "aaaababbab", "baabbbaaab", "ababbbaaaa", "baabbbaabb", "abababbaba", "bbbaaabbab", "bbbbbbbaab", "aaababbbaa",
         "aabababbbb", "baabbaaabb", "bbaabaabab", "baabaababa", "ababbabbab", "bbbabbaaab", "abbabababb", "bbaaaabbba",
         "aaaabbaaba", "bababbbaaa", "aabbbabaab", "abababbaab", "aababbaabb", "bbbaaabaab", "abbbababaa", "babbaabaaa",
         "aabbaaaaab", "aaaaababaa", "aaaaaaaaaa", "aaaabbabab", "bbbbbbaabb", "ababbbaabb", "abbaabaaab", "abababaaba",
         "babaaabbbb", "bbaababbaa", "aaaabbaaaa", "aaabababaa", "babaaabbba", "bbbbabbaab", "bbbaabaaba", "babaabbaab",
         "abaabbbbab", "aabaaaabba", "baabbbbabb", "bababaabbb", "bbababbbaa", "aabbbbabaa", "babbbababb", "aabbbbabbb",
         "aabbbaabbb", "bbabaabaaa", "baabbabaaa", "aaaaabaabb", "bbaaababab", "bbbabbaaba", "aabaabbbab", "abaabbbbaa",
         "abbaaabaab", "abaaaaaaab", "aabbabbbab", "abaaababba", "bababaabaa", "abaababaab", "abbaababba", "baaaababab",
         "bbbbaaaaaa", "bbabaabaab", "bbabbbabab", "aaaabbbaaa", "abbbbbbbaa", "aaaaaababa", "abaabaaaba", "baabbbbaab",
         "aaaaabbaab", "abababbbbb", "abababbbba", "abababaaaa", "aaabaaabab", "bbabaaaabb", "ababaabbbb", "aaababbabb",
         "babaabbbbb", "abbbababba", "bbabababba", "bbababbbab", "bbaababaaa", "abaabaabaa", "bbbbbbabbb", "ababaaaaba",
         "abbbbaaaab", "babaabaaab", "aaaabaaabb", "bbaaabbaaa", "bbaaaabbab", "aaabbbabaa", "baaababbab", "bbbaabaaaa",
         "babbbbaaba", "aabbaabbba", "abbaababab", "baabaaaaab", "abaabbbaaa", "bababbaaab", "bbaaabbabb", "bbbaabbaaa",
         "aaababaaab", "ababbbabbb", "abbaaaaabb", "aababbbabb", "aaaaabbabb", "baaaaabaaa", "baabbbaaba", "bbbbaaabbb",
         "ababbbbbab", "bbaabababb", "abbabbabaa", "abbabbaaaa", "baabbaabab", "aabaabaaab", "bbabbabaab", "babbabbbbb",
         "bbaabaaaaa", "baabbbabba", "babababbaa", "abaaaaaaaa", "ababababaa", "aabbabaabb", "abbabbaaba", "bababbbbab",
         "baaabaabbb", "bbbabaabba", "aaababbbbb", "abbbbabaaa", "baabaaabaa", "baabbbabbb", "bbbbabbabb", "babaabbbaa",
         "baabbabbaa", "baaabaabab", "bbaabbbaaa", "aaabbaaaaa", "bbbaabbbba", "aabaaababa", "abbbbbaaaa", "bbbbaaaabb",
         "abbaabbaaa", "bbbbbbabba", "bbabbaaaab", "aabbabbbbb", "baabbaaaba", "abbbabaaba", "abbbbaaabb", "abbabbaabb",
         "ababaaabab", "aabaababaa", "aabbbbbbaa", "aabbbabbba", "bbbabbabbb", "aaabbbbaaa", "bbabbabbaa", "abbbabbbbb",
         "aabaaaabaa", "abbbabbaba", "abbbbbabba", "bbaabbaaba", "babbbaaaba", "bbaabbabba", "baaaabaaaa", "aababbaaba",
         "bbbababaab", "aabaaaaabb", "bbbbababaa", "bbababaaaa", "babbbaabbb", "abbbbbbaab", "baaabbbbba", "aabbbbbaaa",
         "bbbbbababb", "aabbaabbaa", "aaaaaabbbb", "bbbabaaabb", "ababbbbabb", "aabbaababa", "aaabaabbaa", "aaaaabbaba",
         "baaabbaabb", "baaabbabbb", "babbabbabb", "ababbabaaa", "bababbaaaa", "aabaabbaaa", "bbababaabb", "abababaaab",
         "abbaaaaaba", "aaaabbbaab", "bbaabaabbb", "bbbbabaaab", "baaaaabbba", "baaabaaaaa", "babbbbbbaa", "aababababb",
         "bbaabbabbb", "bbbababbaa", "aabaaabbaa", "abaabbbbbb", "bbaabaaaba", "baaabbbaba", "bbbbbaaabb", "abbbabbaab",
         "abbaaaabba", "baaaabbaaa", "abbabababa", "aabababbba", "bbbabaabab", "bbabbbbbab", "bbbaaabbaa", "abbabbbaab",
         "abbbbabbaa", "bbabbaabbb", "baaaaabbbb", "abaabaaaab", "aabbaaabba", "bbaabaabaa", "abbaabbaab", "bbabbbbabb",
         "babbaababb", "bababbbbbb", "babaaaaabb", "abbaabbbba", "babbbaabab", "bbababbaba", "abbaaaabbb", "baabbbbbba",
         "babbababab", "baaaabbbbb", "aabaaaaaab", "aaaaabaaba", "ababbaaabb", "aaabaaaaaa", "aaabbabbaa", "babababbba",
         "babbaaabaa", "bbabbababa", "baabbaabba", "aabbababbb", "babbbaaabb", "abbaabbbaa", "abbbaababa", "babaaaabab",
         "bbbbbaabbb", "aababbbbbb", "aabbbbaaaa", "abaabababb", "abaabbbbba", "aaaaabbbba", "abbbaaabbb", "babbbbabba",
         "abbbaaabba", "bbbababaaa", "aabbbabbab", "baaaaabaab", "babbbbabbb", "bbaaabaaaa", "baabbbbaba", "aabbbbbbba",
         "bbbaababab", "bababbbaab", "aabbaabaaa", "baaaaabbab", "abaabbabba", "bbbbbabbbb", "ababaababa", "aaaaaaaaba",
         "bbbbaaabba", "bbababbbba", "bbbbaabbbb", "abbaaaaaaa", "abbaababaa", "bbbaaababb", "babbaaabab", "bababbbbaa",
         "bbabbbabbb", "babbbabbaa", "bababbabbb", "baaaabbaba", "aaabbbbbaa", "baaaabaaab", "aaaaabaaaa", "babbbaabba",
         "aaaabbaabb", "aabaaabaab", "abbababbba", "aababbbaba", "bbabbaaaaa", "bbbbaabaab", "babbabaabb", "abaaabaabb",
         "bbbabbbbaa", "bbbbaababa", "abbabbbbab", "babbbabaab", "aaaaaaabab", "ababbabbbb", "aabbbbbaab", "baabaaaaaa",
         "baabbaaaaa", "baabaabbbb", "aaaaaaabbb", "bbbbbbbaaa", "babbbaabaa", "aabababaab", "abaaaaabba", "baabbababa",
         "aabbbaabba", "abaabbbaab", "aaaabaabab", "aaaabbbaba", "ababbaabba", "abbabaabba", "aabaabaabb", "bababaaaab",
         "baababbabb", "bababbabab", "abaaabbaba", "abaababbba", "bbbabbabba", "aaabbbbaab", "bbbbaaabab", "abbbaababb",
         "bbbaaababa", "aabbbaabab", "aaaababbaa", "bbbbaaaaba", "bbbaababaa", "abaaabaaaa", "aabbababba", "baaaabbbaa",
         "aabbbabaaa", "aabaaababb", "aaabbabaab", "bbbabababa", "bbabaaabab", "aaabaaabba", "ababbbabba", "abbaaaabaa",
         "abaaaabbab", "babbababbb", "aaabbbbbab", "ababbabaab", "abbaababbb", "bbabbbbaaa", "aaaaaabbba", "bbbbaabbaa",
         "abbababaaa", "aaaabaaaaa", "aabaaabbba", "bbaaabbbaa", "abaaaabbaa", "baaabbabba", "aabbaabaab", "babbaabbab",
         "babbbabbab", "baabbababb", "ababbabbba", "bbababaaab", "babbbbbbba", "ababbbaaba", "abbbababbb", "baabababaa",
         "baabbabbba", "bbabbabbab", "bbaabaaaab", "aabbabaaab", "bbbbaaaaab", "aaababbbab", "bbabbaabba", "bbabbaabaa",
         "aaaabbbbab", "bbbaaaabab", "abbabbaaab", "babbaabbaa", "baaabaaabb", "babbababba", "bbababbbbb", "aabaaabaaa",
         "abbbbababa", "babaaaabbb", "aaaaabbbaa", "bbbaaabbba", "bbbaababba", "abbbbabbbb", "aabbbbbabb", "babaaaaaba",
         "bbaababbba", "aaabaabaaa", "aaaabaabbb", "aabbbaabaa", "ababbbbaaa", "abbaaababb", "bbaaaaaaaa", "abbbaabaaa",
         "aaabbaabaa", "aaaaabbbab", "baababbaab", "ababaaabba", "aaabbbaaaa", "aabbbaaaaa", "babaaaabba", "aaababaaaa",
         "bbbabbbbab", "abbbaaaabb", "bbbbababbb", "aabaababab", "bbaabbaaab", "aabbabbaaa", "aaaabbbbba", "bbbabaabbb",
         "abbababbab", "abbbabbabb", "aabaabaaba", "abbbabbbab", "aababbbaab", "aabaaaabbb", "bbbabbbaba", "bbabbbbbbb",
         "bbbaababbb", "abaababbaa", "bbbbbaabba", "aaabbaabba", "bbbbabaaba", "abaabbaaab", "aaaabaaaab", "aaaaababbb",
         "aaabbababb", "aaababbaba", "bbbaaaaabb", "abaaaabaaa", "baaaaaabaa", "abaaaaaaba", "aaabbaaabb", "baaabbaaab",
         "bbaaaababa", "bbabaaabba", "aabababbab", "bbabbbbaba", "baababaaaa", "aaaaabaaab", "abbbbaabba", "bbbabbbaab",
         "aaabababba", "baabbaaaab", "bbbaaaaaba", "babaabaabb", "bababbbabb", "bababababb", "aababbbbab", "bbbbbababa",
         "ababaaaaaa", "aaabababab", "abbbabbbba", "ababbaaaba", "babaaabbab", "abaaabaaba", "aababaabbb", "aaaaaabaab",
         "baababbbbb", "abbbaaaaab", "aabbbaaabb", "bbabbaabab", "aaabbbbbba", "abbbaabbab", "abababbbaa", "abaababbbb",
         "bbaaaaabaa", "aabbbbaaba", "abbbaaabaa", "babbbbaabb", "aabbbbaaab", "abbbbbbbba", "aabbabbaab", "bbabbbabaa",
         "abaabaaabb", "abbbbbbaaa", "aaaabbbbaa", "baabaaaaba", "abbbbabaab", "bbaaaabaab", "bbabaabbbb", "aababaaaaa",
         "ababaaabbb", "baaaababba", "baabbbbbaa", "aaabbaabab", "aaaabbabbb", "bbbabaaaba", "aabbbbbaba", "abaaababab",
         "bbabaababb", "abaaaabbba", "aabbaababb", "ababaababb", "bbaaaaaabb", "abbaabaabb", "abbaaababa", "bbbabaabaa",
         "aaaabbbabb", "baaabbbaab", "ababaabbba", "ababbbbbbb", "babbbbabab", "babaababaa", "bbabbabaaa", "bbaaabbaba",
         "aababaabaa", "abbabbbbaa", "bbabaaabbb", "aaaabbaaab", "aaaaaabbab", "babaaaaaaa", "babbaaabbb", "aaaabaaaba",
         "aababbaaaa", "aababaaaab", "baaaaababa", "aabababbaa", "baaababaaa", "abaabbbabb", "bbaabbbaab", "baaabbbbab",
         "bbabaabbaa", "babbbbaaaa", "bbaaabbbab", "bbbbabbbba", "abaabbabab", "abababbaaa", "babaaaabaa", "aaabaabbab",
         "abbabbbaba", "babbbbbbab", "abaaababaa", "abaabaabba", "babababaab", "bbaaaaaaab", "bbaabababa", "abaabababa",
         "bababaabba", "bababaaabb", "babbabbaba", "bbbabbaabb", "aaabbbbaba", "bbbababbbb", "babbaababa", "ababbababa",
         "abaaabbbbb", "ababaabaaa", "babbbbaaab", "aaabbaaaab", "bbabababaa", "bbaaabbbbb", "aabbbbbbab", "bbabaabbba",
         "aaaababaaa", "babbbababa", "baaaaaabab", "bbaaababba", "babaababba", "aabbbbaabb", "bababbabba", "abbabaaaab",
         "babbaaaaab", "bbababbabb", "baaabbbabb", "aababbbaaa", "abbabaaaaa", "bbbaaabaaa", "bbbbbabbba", "babbaaabba",
         "abbababbbb", "bbbbaabbab", "aababbbbaa", "abbbaaabab", "aaaaaaabba", "aaabaabbbb", "aabbaaaaaa", "aaabaaabaa",
         "bbaaaaabab", "ababaabaab", "aaabbbbabb", "bbababaaba", "abbbaabbaa", "baaabbaaba", "abaaabbaab", "baabaababb",
         "abbaaabbab", "aaabbbaaab", "abbaaabaaa", "babbaabaab", "baaaababaa", "abbbaabbba", "baaaabaabb", "abbaaaaaab",
         "aaabaababa", "abaaabaaab", "babbababaa", "bbaabbbbaa", "ababaaaabb", "abbbababab", "abbbabaaaa", "aabaabbaba",
         "abbbbbbbab", "abbbbaaaaa", "baaabaaaba", "abbbbaabab", "ababbbbaab", "bbabbbaabb", "babbabbaaa", "babaaababa",
         "babbabaaaa", "babbaaaaba", "bbbbbbbbaa", "baabaaaabb", "bababbabaa", "abbbbabbab", "bbbababbba", "aabbbababb",
         "bababbbbba", "baaabbabaa", "aababaaabb", "bbbabababb", "bbbbaababb", "baaababbba", "bbababbaab", "babaaabaab",
         "baaababaab", "aaabababbb", "bbaaabaabb", "abaababaaa", "aababaabba", "babbbbbaaa", "abbabbbbba", "aaabbabaaa",
         "aaabaababb", "bbbbbbbabb", "babbbbbaba", "abaaabbbba", "baaabaaaab", "baaabbabab", "aaaaaaabaa", "aabaabbaab",
         "babbaabbba", "bbbaabaabb", "baaabbbaaa", "babaaabbaa", "bbabababbb", "bababaabab", "aabbaaabaa", "bbabbbbbaa",
         "bbbabbbbbb", "bbbaabaaab", "babababaaa", "babababbbb", "babbbaaaab", "abaabaabbb", "bbbbbbbbab", "aababbbbba",
         "abbabaaabb", "bbabaabbab", "baaaaaaabb", "abbbbaabbb", "baaaabbabb", "bbbabbabaa", "abaabaaaaa", "aaaaaaaabb",
         "bbaaaaaaba", "aabbbabbaa", "aaabaaabbb", "abaaabbaaa", "bbbbbbbaba", "bbabbaaaba", "abaaababbb", "aaabbbabab",
         "bbbaaabbbb", "bbaaababaa", "baaaababbb", "aabbaaabbb", "babaabbbab", "bbbaabbaab", "bbabbbaaab", "aabbaabbbb",
         "bbbbbbabaa", "ababbbabaa", "abaabbaaaa", "abbabaaaba", "baababbbba", "baabaaabba", "bbaaaababb", "aaabbbabbb",
         "baababaaba", "baabbbbaaa", "babbabbbab", "aabbabbbaa", "baabbabbbb", "bbbbbabaaa", "bbbbbbbbbb", "baaaaaabba",
         "bbbabaaaaa", "baaaaaaaba", "abbbbbaaab", "baaaabaaba", "abbbbbabab", "ababbaabaa", "abbbabbaaa", "abbabaabab",
         "aabaaaabab", "bbaabbbbab", "aaabbbaaba", "abaaabbabb", "abbaabbbab", "abababbabb", "bbbbbabbaa", "bbbbbabaab",
         "bbaababbab", "abbabaabaa", "bbbaaaabba", "bbbbbbaaba", "aabbaaabab", "aaabbbbbbb", "aabbbabbbb", "abbbbaabaa",
         "baabaabbaa", "baaaabbaab", "abbababaab", "baaaabbbab", "babbabaaab", "ababbabbaa", "bbbaaaabaa", "bbbbbbabab",
         "abbabbabba", "bbbbbaaaaa", "aabbbbabba", "baabbbabaa", "babbbbbabb", "babbaabbbb", "aaabbbaabb", "abaaaabbbb",
         "baaabaabba", "baaaaaaaab", "bbabaababa", "bbbbabbbab", "bbbbbbaaab", "abaaaaaabb", "bbbbbaaaab", "aaaabbabba",
         "abaabbaaba", "babbbbabaa", "aabaabbbaa", "bbbabaaaab", "bbbabbaaaa", "bbaaabaaba", "bbabbababb", "bbaabbabaa",
         "aaaabaabba", "bbbabbbbba", "baaaaaabbb", "babbbbbbbb", "aaaaaaaaab", "babaabbbba", "baabbbabab", "bbbaabbbbb",
         "bbaaabbaab", "bbbbaabbba", "baaababbbb", "aaaabababb", "aabaabaaaa", "bababbaaba", "abaaabbbaa",
         "babaababbb"])
    print(obj.f("aaaababba","aababbab"))
