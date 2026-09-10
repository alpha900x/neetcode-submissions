class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        window,T = {},{}

        for i in t:
            if i not in T:
                T[i] = 1
            else:
                T[i] += 1
        window = {key:0 for key in T}

        res = [float("-inf"),float("inf")]
        i,j=0,-1
        count = 0
        valid = False

        while j<len(s)-1:
            while j<len(s)-1 and valid == False:
                j+=1
                if s[j] in window:
                    window[s[j]]+=1
                    count+=1
                if count >=len(t):
                    for key in window:
                        if window[key]<T[key]:
                            valid = False
                            break
                        valid = True
            #print(i,j,valid)
            while i<=j and valid == True:
                if (j-i+1)<(res[1]-res[0]+1):
                    res = (i,j)
                if s[i] in window:
                    window[s[i]]-=1
                    count -= 1
                i+=1
                if count >=len(t):
                    for key in window:
                        if window[key]<T[key]:
                            valid = False
                            break
                        valid = True
                else:
                    valid = False
                #print(i,j,res)
        if res[0] == float("-inf"):
            return ""
        else:
            return s[res[0]:res[1]+1]

            

        
        
        


                
                                



                
                