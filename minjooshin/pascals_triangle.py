'''
출처 - https://leetcode.com/problems/pascals-triangle/
문제 - 118. Pascal's Triangle
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        child_lst = []
        super_lst = []
        for i in range(numRows):
            if i == 0:
                super_lst.append([1])
            elif i == 1:
                super_lst.append([1,1])
            else:
                for j in range(len(super_lst[i-1])-1):
                    child_lst.append(super_lst[i-1][j] + super_lst[i-1][j+1])
                child_lst.insert(0, 1)
                child_lst.append(1)
                super_lst.append(child_lst)
                child_lst = []    

        return super_lst