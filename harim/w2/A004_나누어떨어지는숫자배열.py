'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/12910
문제: 나누어떨어지는숫자배열
'''


def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer
