class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #Using backtracking method

        res=[]

        def backtrack(current, open_count, close_count):
            #check if current already has the 2*n parentheses we want 
            #in this case we add it to res
            if len(current)==2*n:
                res.append(current)
                return
            if open_count<n:
                backtrack(current+'(',open_count +1, close_count)
            if close_count<open_count:
                backtrack(current+')',open_count, close_count +1)
        
        backtrack('',0,0)
        return res
        
