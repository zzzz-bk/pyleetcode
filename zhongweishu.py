class Solution(object):
    max_int = 9223372036854775807
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        l = (m+n+1) // 2
        r = (m+n+2) // 2
        return (self.findKth(nums1,0,nums2,0,l) + self.findKth(nums1,0,nums2,0,r)) / 2

    def findKth(self,nums1,i,nums2,j,k):
        if i>=len(nums1):
            return nums2[j+k-1] #返回nums2的第k位
        if j>=len(nums2):
            return nums1[i+k-1] #返回nums1的第k位
        if k == 1:
            return min(nums1[i],nums2[j])
        midval1 = nums1[i+k//2-1] if i+k//2-1 < len(nums1) else Solution.max_int
        midval2 = nums2[j+k//2-1] if j+k//2-1 < len(nums2) else Solution.max_int
        if midval1 < midval2:
            return self.findKth(nums1,i+k//2,nums2,j,k-k//2)
        else:
            return self.findKth(nums1,i,nums2,j+k//2,k-k//2)

if __name__ == '__main__':
    obj = Solution()
    midval = obj.findMedianSortedArrays([1,2],[3,4])
    print(midval)