class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0: 
            return 1/self.myPow(x,-n)
        if n%2==0:
            return self.myPow(x*x,n//2)
        if n%2==1:
            return x*self.myPow(x*x,n//2)

#Test Case
s=Solution()
assert s.myPow(2,10)==1024
        