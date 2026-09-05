class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        max_len = 0
        f =[0] * 26
        f[ord(s[i])-ord('A')]+=1
        while j<len(s):
            if j-i+1 - max(f) <= k:
                max_len = max (j-i+1,max_len)              
                j+=1
                if j<len(s):
                    f[ord(s[j])-ord('A')]+=1                  
            else:
                f[ord(s[i])-ord('A')]-=1
                i+=1     
        return max_len
            
                
                

                
                    
            