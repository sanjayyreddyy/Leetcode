# link : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i] = 1
            elif i in d and d[i]<2:
                d[i]+=1
        nums [:] = [x for x,y in d.items() for _ in range(y)]
            
        