class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        length=float("infinity")
        currentsum=0
        for r in range(len(nums)):
            currentsum+=nums[r]
            while currentsum>=target:
                l=r-left+1
                if length>l:
                    length=l
                currentsum-=nums[left]
                left+=1
        return length if length!=float("infinity") else 0

      
