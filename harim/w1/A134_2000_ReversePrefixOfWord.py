'''
출처: https://leetcode.com/problems/reverse-prefix-of-word/submissions/875413993/
=> 메모리 13.8MB & 시간 28 ms 
'''


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
