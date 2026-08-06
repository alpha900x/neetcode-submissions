class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map={}
        for i in s:
            if i not in map:
                map[i]=1
            else:
                map[i]+=1
        for i in t:
            if i in map:
                map[i]-=1
            else:
                return False
        for i in map:
            if map[i]!=0:
                return False
        return True

