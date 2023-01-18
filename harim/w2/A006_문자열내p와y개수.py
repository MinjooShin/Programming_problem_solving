'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=python3
문제: A006_문자열내p와y개수
'''


def solution(s):
    s = s.lower()
    return s.count("p") == s.count("y")


p = "pwePPwefqyYY"
print(solution(p))
