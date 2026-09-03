class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev=""
        
        rev3=""
        for j in s:
            if j==" ":
                continue
            elif ord(j)>=65 and ord(j)<=90:
                rev+=chr(ord(j)+32)
            elif ord(j)>=97 and ord(j)<=122:
                rev+=j
            elif ord(j) >= 48 and ord(j) <= 57: 
                rev += j
            else: 
                continue
        i=0
        j=len(rev)-1
    
            
        while i < j:
            if rev[i] != rev[j]:
                return False
            i += 1
            j -= 1
        
        return True
            
            
       

        
        