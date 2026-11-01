class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack=[]
    
        for i in range(len(prices)):
            j=i+1
            while j<len(prices) :
                if prices[j]<=prices[i]:
                    stack.append(prices[i]-prices[j])
                
                    break
                j+=1
            if j ==len(prices):
                stack.append(prices[i])
        return stack

        