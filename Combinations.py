class Solution(object):
    def subcomb(self, a, b, k):
        res = []
        if k<1 or b-a+1<k:
            return res
        for x in range(a, b+1):
            tmp = [x]
            if k>1:
                ss = self.subcomb(x+1, b, k-1)
                for sss in ss:
                    res.append(tmp + sss)
            else:
                res.append(tmp)
        return res
            
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.subcomb(1, n, k)
