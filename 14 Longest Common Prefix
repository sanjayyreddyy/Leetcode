# link: https://leetcode.com/problems/longest-common-prefix/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        e=0
        n= len(strs)
        if n<2:
            return strs[0]
        try:
            for i in range(len(strs[0])):
                c=strs[0][i]
                if e==1:
                    break
                for j in range(1,n):
                    if c==strs[j][i]:
                        if j==n-1:
                            s+=c
                    else:
                        e=1
                        break
        except:
            return s
        return s
                        
                    


        