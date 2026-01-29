class Solution:
    def isHappy(self, n: int) -> bool:
        num = set()
        while n not in num:
            num.add(n)
            suma=0
            while n:
                suma+=(n%10)**2
                n//=10
            n=suma
            if n==1:
                return True
        return False
   




       
        
            
