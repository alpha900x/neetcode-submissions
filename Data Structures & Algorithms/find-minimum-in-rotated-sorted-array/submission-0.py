import heapq as hq
class Solution:
    def findMin(self, nums: List[int]) -> int:
        hq.heapify(nums)
        return nums[0]
