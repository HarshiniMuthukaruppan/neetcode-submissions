class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s) !=len(t):
            return False

        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        for i in t:
            if i in d and d[i]>0 :
                d[i]-=1
            else:
                return False

        return    True    
               

        