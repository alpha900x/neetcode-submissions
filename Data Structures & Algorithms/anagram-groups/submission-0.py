class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            op=[]
            op.append(strs)
            return op
        hp={}
        for i in strs:
            j =''.join(sorted(i))
            if j not in hp:
                hp[j]=[i]
            else:
                hp[j].append(i)
        return (list(hp.values()))

            
