class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        for s,e in intervals[1:]:
            last=result[-1][1]
            if s<=last:
                result[-1][1]=max(e,last)
            else:
                result.append([s,e])
        return result
        