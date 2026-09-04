class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {}
        for i in s1:
            if i not in h1:
                h1[i]=1
            else:
                h1[i]+=1
        for c in range(len(s2)):
            if s2[c] in h1.keys():
                h={}
                h[s2[c]]=1
                j=c     
                while j-c+1<len(s1) and j<len(s2)-1 and s2[j+1] in h1.keys():
                    j+=1
                    if s2[j] not in h:
                        h[s2[j]]=1
                    else:
                        h[s2[j]]+=1
                print(h)
                if h==h1:
                    return True
        return False
                
                    