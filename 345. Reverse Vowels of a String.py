
       
class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        left=0
        right=len(s)-1
        sa="AEIOUaeiou"

        while left<right:
            if s[left] in sa and s[right] in sa:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif s[right] not in sa:
                right-=1
            else:
                left+=1

        return "".join(s)
