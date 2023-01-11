'''
출처 - https://leetcode.com/problems/assign-cookies/
문제 - 455. Assign Cookies
'''

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt=0
        g.sort()
        s.sort()
        #각 child가 원하는 쿠키 수와 같거나 큰 쿠키가 쿠키리스트에 존재하는지 확인
        for i in g:
            for j in s:
                if i <= j:
                    #존재할 경우, 기록했다가 삭제하고 그 다음 루프를 돌지 않고 나가기
                    rmv_idx = j
                    cnt += 1
                    s.remove(j)
                    break
        print(cnt)
        return cnt