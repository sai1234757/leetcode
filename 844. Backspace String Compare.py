class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st=[]
        bt=[]
        for i in range(len(s)):
            if s[i]!="#":
                st.append(s[i])
            else:
                if st:
                    st.pop()
        for i in range(len(t)):
            if t[i]!="#":
                bt.append(t[i])
            else:
                if bt: 
                    bt.pop()

        if bt==st:
            return True 
        return False
        
        

        