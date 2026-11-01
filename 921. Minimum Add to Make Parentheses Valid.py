class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        m=0
        suma=0
        for i in s:
            if i=="(":
                c+=1
            if i==")":
                m+=1
        if m>c:
            suma=m-c
        else:
            suma=c-m
        return suma
        

            

        