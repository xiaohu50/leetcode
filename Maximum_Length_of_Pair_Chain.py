class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = lambda x: x[1])
        end = pairs[0][1]
        l = 1
        for s, e in pairs:
            if s>end:
                l += 1
                end = e         
        
        return l
