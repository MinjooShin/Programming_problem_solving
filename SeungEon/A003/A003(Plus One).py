class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit ,tmp= 0,0
        digits.reverse()
        ans=[]
        for i in range (len(digits)):
            digit*=10
            digit=digit+digits.pop()
        """for i in range (len(digits)):"""
        digit=digit+1
        while 1 :
            if(digit<=0) :break
            tmp = digit%10
            ans.append(tmp)
            digit=digit/10
        ans.reverse()
        return ans
