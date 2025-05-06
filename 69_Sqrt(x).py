class Solution(object):
    def mySqrt(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n

        left = 0
        right = n

        while (right - left) > 1:
            middle = (left + right) // 2
            if middle * middle == n:
                return middle
            elif middle * middle > n:
                right = middle
            else:
                left = middle

        return left  

# ✅ Test cases
s = Solution()
assert s.mySqrt(4) == 2
assert s.mySqrt(8) == 2
assert s.mySqrt(0) == 0
assert s.mySqrt(1) == 1
assert s.mySqrt(10) == 3