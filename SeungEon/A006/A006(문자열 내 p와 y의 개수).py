def solution(s):
    answer = True
    count_P=s.count("P")
    count_p=s.count("p")
    count_Y=s.count("Y")
    count_y=s.count("y")
    Sum_P= count_P+count_p
    Sum_Y= count_Y+count_y
    
    if(Sum_P==Sum_Y):answer=True
    else : answer = False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer