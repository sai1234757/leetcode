class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==0:
            return []
        s=[''.join(sorted(i)) for i in strs]
        h={}
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]]=[]
            h[s[i]].append(strs[i])
        return list(h.values())

     