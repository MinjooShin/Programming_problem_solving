'''
출처: https://www.acmicpc.net/problem/2108
문제: 2108. 통계학
=> 메모리 52136 KB & 시간 1532 ms 미쳤누
'''
import sys

N = int(sys.stdin.readline())

num_list = []
count_dic = {}
mode = 0

for i in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)

num_list.sort()

for num in num_list:
    if num in count_dic:
        count_dic[num] += 1
    else:
        count_dic[num] = 1

mode_list = []
for num in count_dic:
    if count_dic[num] == max(count_dic.values()):
        mode_list.append(num)

if len(mode_list) > 1:
    mode = mode_list[1]
else:
    mode = mode_list[0]

print(round(sum(num_list)/N + 0.01))
print(num_list[(N-1)//2])
print(mode)
print(num_list[-1]-num_list[0])

# # test input 1
# 5
# -1
# -2
# -3
# -1
# -2
# # test output 1
# -2
# -2
# -1
# 2

# # test input 2
# 1
# 4000
# # test output 2
# 4000
# 4000
# 4000
# 0


'''
failed code
실패: 시간 초과 -> https://puleugo.tistory.com/44 참고
=> input() + 파이썬의 round() 함수 오사오입 + dictionary sort
'''
# N = int(input())

# num_list = []
# count_dic = {}
# mode = 0

# for i in range(N):
#     num = int(input())
#     if num in num_list:
#         count_dic[num] += 1
#     else:
#         count_dic[num] = 1
#     num_list.append(num)

# num_list.sort()
# count_list = sorted(count_dic.items(), key=lambda it: it[1])

# if len(count_list) == 1 or count_list[-1][1] != count_list[-2][1]:
#     mode = count_list[-1][0]
# else:
#     min1 = min2 = 500000
#     for tup in count_list:
#         if tup[1] == count_list[-1][1]:
#             if tup[0] < min1:
#                 min2 = min1
#                 min1 = tup[0]
#             if min1 < tup[0] < min2:
#                 min2 = tup[0]
#             if tup[0] > min2:
#                 pass
#     mode = min2

# print(round(sum(num_list)/N))
# print(num_list[(N-1)//2])
# print(mode)
# print(num_list[-1]-num_list[0])
