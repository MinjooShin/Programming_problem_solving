def solution(skill, skill_trees):
    answer = 0
    lst = []
    for skt in skill_trees:
        for ch in skt:
            if ch in skill:
                lst.append(ch)
        str_skt = "".join(lst)
        # if str_skt == skill:
        #     answer += 1
        if str_skt == skill[0:len(str_skt)]:
            answer += 1
        lst = []
    return answer