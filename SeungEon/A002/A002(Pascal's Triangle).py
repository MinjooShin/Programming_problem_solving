class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        for r in range (numRows) :
            row=[]
            for i in range (r+1) :
                if (i==0):
                    row.append(1)
                elif (i==r):
                    row.append(1)
                else : 
                    row.append(ans[r-1][i-1]+ans[r-1][i])
            ans.append(row)
        return ans
