def solution(s):
    p_cnt = 0
    y_cnt = 0
    answer = True
    s = s.lower()
    for i in s:
        if i == 'p':
            p_cnt += 1
        if i == 'y':
            y_cnt += 1
    if p_cnt is not y_cnt:
        answer = False
        
    return answer