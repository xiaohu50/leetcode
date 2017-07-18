class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negtive=False
        if x<0:
            negtive=True
            x = -x
        ret = 0 
        while x>0:
            n = x%10
            ret = ret*10 + n
            x /= 10
        if negtive:
            ret = -ret
        if ret<-2**31 or ret>=2**31:
            ret=0
        return ret
