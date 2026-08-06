class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp={}
        for i in nums:
            if i not in hp:
                hp[i]=1
            else:
                hp[i]+=1
        lst=sorted(hp.items(),key=lambda x:x[1],reverse=True)
        op=[]
        for i in range(k):
            op.append(lst[i][0])
        return op