class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        seen={}
        maxi=0
        for i in range(len(s)):
            ch=s[i]
            if ch in seen:
                start=max(start,seen[ch]+1)
            maxi=max(maxi,i-start+1)
            seen[ch]=i
        return maxi
        