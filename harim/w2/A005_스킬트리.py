'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/49993?language=python3
문제: A005_스킬트리
'''


def solution(skill, skill_trees):
    rst = 0
    for tree in skill_trees:
        flag = 0
        check = []
        for i in range(len(skill)):
            idx = tree.find(skill[i])
            if idx == -1 and i != len(skill)-1 and tree.find(skill[i+1]) != -1:
                flag = 1
                break
            elif idx != -1:
                check.append(idx)
        if flag != 1 and check == sorted(check):
            rst += 1

    return rst


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "C", "CB"]))
