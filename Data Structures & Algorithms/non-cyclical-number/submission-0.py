def sumdig(n):
    s=0
    while n>0:
        s+=(n%10)**2
        n//=10
    return s    

        
        

class Solution:

    def isHappy(self, n: int) -> bool:
        s=set()
       
    
       
        while n!=1 :
            n=sumdig(n)
            if n in s:
                return False
            
            s.add(n)    

        return True    
        