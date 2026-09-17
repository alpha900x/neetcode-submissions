class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        mid = (total + 1) // 2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        cutA = 0
        cutB = 0
        l = 0
        h = len(nums1)
        Al, Bl, Ar, Br = 0, 0, 0, 0
        while l <= h:
            cutA = (l + h) // 2
            cutB = mid - cutA

            if cutA == 0:
                Al = float("-inf")
            else:
                Al = nums1[cutA - 1]
            if cutA == len(nums1):
                Ar = float("inf")
            else:
                Ar = nums1[cutA]

            if cutB == 0:
                Bl = float("-inf")
            else:
                Bl = nums2[cutB - 1]
            if cutB == len(nums2):
                Br = float("inf")
            else:
                Br = nums2[cutB]

            if Al > Br:
                h = cutA - 1
            elif Ar < Bl:
                l = cutA + 1
            else:
                if total % 2 == 0:
                    return (max(Al, Bl) + min(Ar, Br)) / 2
                else:
                    return max(Al, Bl)
