class Solution(object):
    def maximumSubarraySum(self, nums, k):
        s = 0
        m = 0
        j = 0

        for i in range(k):
            s += nums[i]

        if len(set(nums[:k])) == k:
            m = s

        for i in range(k, len(nums)):
            s += nums[i] - nums[j]
            j += 1

            if len(set(nums[j:i+1])) == k:
                if m < s:
                    m = s

        return m