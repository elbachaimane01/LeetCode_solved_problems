class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open=['(','[','{']
        close=[')',']','}']
        temp=[]
        for bracket in s:
            if bracket in open:
                temp+=close[open.index(bracket)]
            elif bracket in close: 
                #get the last item of tem if there is 
                if temp==[]:
                    return False
                else:
                    last=temp[-1]
                    if bracket==last:
                        temp=temp[:-1]
                    else:
                        return False

        if temp==[]:
            return True
        return False     