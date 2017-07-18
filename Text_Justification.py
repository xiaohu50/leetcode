class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret = []
        
        wordlens=[]
        ss = []
        tmp = []
        tmpl = -1
        lastline =[]
        for i in range(len(words)):
            word = words[i]
            l = len(word)
            wordlens.append(l)
            if tmpl+l+1>maxWidth:
                ss.append(tmp)
                tmp=[]
                tmpl=-1
            tmp.append(i)
            tmpl += l+1
        lastline = tmp
        
        for s in ss:
            num = len(s)
            spaces = maxWidth - sum([wordlens[i] for i in s])
            sentence = ''
            if num>1:
                spaceLeft = spaces % (num-1)
                spaceEach = spaces / (num-1)
                spaceOne = 0
                for wi in s:
                    if spaceLeft>0:
                        spaceOne = spaceEach+1
                        spaces -= spaceOne
                        spaceLeft -= 1
                    else:
                        if spaces>0:
                            spaceOne = spaceEach
                            spaces -= spaceOne
                        else:
                            spaceOne = 0
                    sentence += words[wi] + ' '*spaceOne
            else:
                sentence =words[s[0]] + ' '*spaces
            ret.append(sentence)
            
        num = len(lastline)
        spaces = maxWidth - sum([wordlens[i] for i in lastline])
        spaceLast = spaces-(num-1)
        sentence = ''
        for i in range(num):
            wi = lastline[i]
            if i<num-1:
                sentence += words[wi] + ' '
            else:
                sentence += words[wi] + ' '*spaceLast
        
        ret.append(sentence)
        return ret
