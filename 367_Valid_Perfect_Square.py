class Solution(object):
    def isPerfectSquare(self, n):
        """
        :type num: int
        :rtype: bool
        """
        left=0
        right=n+1
        middle=(left+right)//2

        output=False

        while (right-left)>1:
            #print(middle**2)
            if middle**2 ==n: 
                output=True
                break
            elif middle**2 > n:
                right=middle
                middle=(left+right)//2
            elif middle**2 < n:
                left=middle
                middle=(left+right)//2
        return output

##Test case
assert isPerfectSquare(16)==True 
assert isPerfectSquare(14)==False 