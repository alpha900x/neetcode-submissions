class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {}
        for i in s1:
            if i not in h1:
                h1[i]=1
            else:
                h1[i]+=1
        i=0 
        j=len(s1)-1
        h={}
        for c in s2[i:j+1]:
            if c not in h:
                h[c]=1
            else:
                h[c]+=1
        while j<len(s2):
            if h==h1:
                return True
            else:
            #i
                if h[s2[i]]==1:
                    del h[s2[i]]
                else:
                    h[s2[i]]-=1
                i+=1
            #j
                j+=1
                if j<len(s2) and s2[j] not in h:
                    h[s2[j]]=1
                else:
                    if j<len(s2):
                        h[s2[j]]+=1
                print(h)
        return False
                
                    