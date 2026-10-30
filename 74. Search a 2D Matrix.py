class Solution(object):
    def searchMatrix(self, a, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not a or not a[0]:
            return False
        c=len(a[0])
        r=len(a)
        t=0
        b=r-1
        while t<=b:
            m=(t+b)//2
            if target<a[m][0]:
                b=m-1
            elif target>a[m][c-1]:
                t=m+1
            else: break
        if t>b:
            return False
        l=0
        r=c-1
        while l<=r:
            mm=(l+r)//2
            if target == a[m][mm]:

                return True
            elif target<a[m][mm]:
                r=mm-1
            else:
                l=mm+1
        return False
