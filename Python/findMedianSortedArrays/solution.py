class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+nums2)
        length = len(nums)
        if length%2 == 0 and len(nums1) <= 1000 and len(nums2) <= 1000:
            return (nums[int(length/2)-1] + nums[int(length/2)])/2
        else:
            return nums[length//2]

sol= Solution()
# sol.findMedianSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1])
sol.findMedianSortedArrays([1,3],[2,4])
        