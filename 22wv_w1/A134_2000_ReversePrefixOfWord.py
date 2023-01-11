class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        else:
            front = word[:idx+1]
            back = word[idx+1:]
            re_word = front[::-1]+back
            return re_word


test = Solution()
print(test.reversePrefix("abcdefg", "d"))
