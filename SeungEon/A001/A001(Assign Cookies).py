class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i,j,ans=0,0,0
        while i<len(g) and j<len(s) :
            if s[j]>=g[i]  :
                del s[j]
                del g[i]
                ans=ans+1
            else :
                j=j+1
        return ans