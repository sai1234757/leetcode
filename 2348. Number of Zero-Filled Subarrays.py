class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                s+=1
                c+=s
            elif nums[i]!=0:
                s=0
        return c
 
            
       
        