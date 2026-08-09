class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1 or len(s)==0:
            return True
        s=s.casefold()
        i=0
        j=len(s)-1
        while i<j:
            if s[i].isalnum()==False:
                while s[i].isalnum()==False and i<j:
                    i+=1
            if s[j].isalnum()==False and i<j:
                while s[j].isalnum()==False:
                    j-=1
            if s[i]==s[j] :
                i+=1
                j-=1
                continue
            else:
                return False
        return True
        
       
        