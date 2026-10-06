class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            nums1[m+n-1] = max(nums1[m-1], nums2[n-1])
            if nums1[m+n-1] > nums2[n-1]:
                m -= 1
            else:
                n -= 1
        
        # nums1: 1,1,1,1,0
        # nums2: 4
        # nums1: 1,1,1,1,4

        # nums1: 4,0,0,0,0
        # nums2: 1,1,1,1
        # nums1: 0,0,0,0,4
        
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1