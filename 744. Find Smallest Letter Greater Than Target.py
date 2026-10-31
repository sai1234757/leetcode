class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        s=sorted(letters)
        for ch in range(len(letters)-1):
            if letters[ch]==target:
                return letters[ch+1]
        return letters[0]
        

        