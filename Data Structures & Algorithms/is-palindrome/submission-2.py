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
                
        for m in rev:
            rev3=m+rev3
        if rev3==rev:
            return True
        else:
            return False
        

        
        