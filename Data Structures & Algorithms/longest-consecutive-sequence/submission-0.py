class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numss=set(nums)
        max_len=1
        for i in numss:
            if i-1 not in numss:
                j=1
                while i+j in numss:
                    j=j+1
                if max_len<j:
                    max_len=j
        
        return max_len