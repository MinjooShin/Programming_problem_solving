'''
출처: https://leetcode.com/problems/plus-one/submissions/879820892/
문제: 66_PlusOne
=> (Sol1) 메모리 13.7 MB (96% beats) & 시간 35 ms (77% beats)
'''


class Solution:
    def plusOne(self, digits):
        r_str = "".join(map(str, digits))
        rst = str(int(r_str)+1)
        rst = list(map(int, rst))
        return rst


'''
=> (Sol2) 메모리 13.8 MB (54.37% beats) & 시간 27 ms (97.39% beats)
'''


class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9 and i == 0:
                digits[i] = 0
                digits.insert(0, 1)
                break
            elif digits[i] == 9 and digits[i-1] != 9:
                digits[i] = 0
                digits[i-1] += 1
                break
            elif digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        return digits
