class Solution:

    def encode(self, strs: List[str]) -> str:
        op=""
        for i in range(len(strs)):
            if strs[i]=="":
                op+=str(0)+"|"
            else:
                op+=str(len(strs[i]))+"|"
                op+=strs[i]
        return op
    def decode(self, s: str) -> List[str]:
        if len(s)==1:
            return [""]
        op=[]
        i=0
        j=0
        while j<len(s):
            leng="" 
            st=""
            while s[i]!="|":
                leng+=s[i]
                i+=1
            leng=int(leng)
            if leng==0:
                st=""
                j=i+1
            else:
                j=i+1
                leng=leng+j
                while j<(leng) and j<len(s):
                    st+=s[j]
                    j+=1
            i=j
            op.append(st)
        return op

           
        


     
       


