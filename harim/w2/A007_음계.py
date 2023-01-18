'''
출처: https://www.acmicpc.net/status?user_id=achel03&problem_id=2920&from_mine=1
문제: 2920. 음계
=> 메모리 30616 KB & 시간 36 ms 
'''
a = list(input().split(" "))
sort_a = sorted(a)
rev_a = list(reversed(sort_a))
if (a == sort_a):
    print("ascending")
elif (a == rev_a):
    print("descending")
else:
    print("mixed")
