class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1+nums2)
        length = len(nums)
        print(length)
        print(nums)
        if length%2 == 0 and len(nums1) <= 1000 and len(nums2) <= 1000:
            print("indice1: ",int(length/2)-1)
            print("indice2: ",int(length/2))
            print(nums[int(length/2)-1])
            print(nums[int(length/2)])
            print((nums[int(length/2)-1] + nums[int(length/2)])/2)
        else:
            print(nums[length//2])

sol= Solution()
# sol.findMedianSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1])
sol.findMedianSortedArrays([1,3],[2,4])
        