# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = 0
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                w = 1
                c+=1
            if s[i] == " " and w ==1:
                break
        return c
            
        
        